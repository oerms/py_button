#! /usr/bin/env python
# oerms 20200117
import os
import RPi.GPIO as GPIO

# set GPIO channel
channel = 5

GPIO.setmode(GPIO.BCM)
# GPIO3 (pin 5) set up as input. It is pulled up to stop false signals
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
try:
    while True:
        # wait for the pin to be sorted with GND and, if so, halt the system
        GPIO.wait_for_edge(channel, GPIO.FALLING)
        # shut down the rpi
        os.system("/sbin/shutdown -h now")
except:
    GPIO.cleanup()
