# py_button

Add functionality to a button on the raspberry pi:
* Press and hold for two seconds: Shutdown
* Press once: start internet radio and turn on stereo amp
* Press once again: stop internt radio
* Press twice: turn off stereo amp

Add a single script as a cronjob via:
```cron
@reboot python /home/pi/py_button/scripts/py_shutdown.py &
```

oerms, 2020-12-12
