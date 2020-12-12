#! /usr/bin/env python
# oerms 20201129
# enhance button pressing script to control the pi
# intended functions:
#  - press and hold 2 seconds   shutdown pi
#  - press and release once     if vcl is running:  shut down vld
#                               if not:             start vlc with br klassik mp3 stream
#  - press and release twice    ???TBD

import os
import sys
import RPi.GPIO as GPIO
import time
import signal

def setupGPIO(channel):
    # set channel numbering to standard raspi GPIO nomenclature
    GPIO.setmode(GPIO.BCM)
    # GPIO3 (pin 5) set up as input. It is pulled up to stop false signals
    GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def countEdges(channel):
    # counter
    timesPressed = 0
     
    try:
        while True:
            # wait for the pin to be shorted with GND and, if so, halt the system
            print("top of loop")
            GPIO.wait_for_edge(channel, GPIO.FALLING)
            print("pressed and wait")
            time.sleep(0.1)
            GPIO.wait_for_edge(channel, GPIO.RISING)
            print("released and wait")
            time.sleep(0.1)
            timesPressed += 1
            print("times pressed = " + str(timesPressed))
    except Exception as inst:
        print('passing inst')
        raise inst

def cleanupGPIO():
    print('cleaning up GPIO')
    GPIO.cleanup()

def exit_sigint():
    print("quitting after SIGINT")
    cleanupGPIO()
    sys.exit()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_sigint)
    # set channel for setup and edge detection
    channel = 5
    # set GPIO channel and setup GPIO
    setupGPIO(channel)
    try:
        countEdges(channel)
    except Exception as inst:
        print(inst)
        cleanupGPIO()
        sys.exit()


