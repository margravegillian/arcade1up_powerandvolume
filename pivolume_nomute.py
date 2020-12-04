#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import alsaaudio

#rint alsaaudio.cards()
#print alsaaudio.mixers()

m = alsaaudio.Mixer('HDMI')
# m = alsaaudio.Mixer('PCM', cardindex=1)
vol = m.getvolume()[0]
is_mute = m.getmute()[0]
print vol

GPIO.setmode(GPIO.BCM)


vol_up_pin = 26
vol_dn_pin = 19
GPIO.setup(vol_up_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(vol_dn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    vu = not GPIO.input(vol_up_pin)
    vd = not GPIO.input(vol_dn_pin)
    if vu and not vd:
        if is_mute:
            toggle_mute()
        if vol < 95:
            vol += 5
            m.setvolume(vol)
            vol = m.getvolume()[0]
        print 'Volume up Pressed', vol
    elif vd and not vu:
        if is_mute:
            toggle_mute()
        if vol > 5:
            vol -= 5
            m.setvolume(vol)
            vol = m.getvolume()[0]
        print 'Volume down Pressed', vol
    

    time.sleep(0.2)
