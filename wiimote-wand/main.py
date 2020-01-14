import time

from math import sqrt
from accel import convertAcc

from wii import Wiimote
from effects import Effect

'''Set up Audio'''
wiimote = Wiimote()
effect = Effect()

state = 0

'''Main loop'''
while True:
    g = convertAcc(wiimote.accel(),0)
    angles = convertAcc(wiimote.accel(), 1)
    accMag = sqrt(g[0]**2 + g[1]**2 + g[2]**2)
    print('x: {0:.2f}'.format(angles[0]))
    print('y: {0:.2f}'.format(angles[1]))
    print('Mag: {0:.2f}'.format(accMag))

    if state == 0:
        if angles[1] > 45:
           wiimote.rumble(True)
           if not effect.busy():
               effect.sound("audio/bubble.wav")
               state += 1
    
    if state == 1:
        if accMag > 3:
            wiimote.rumble(True)
            if not effect.busy():
                effect.sound("audio/bell2.wav")
                state += 1

    if state == 2:
        if angles[0] > 45:
            wiimote.rumble(True)
            if not effect.busy():
                effect.sound("audio/bubble.wav")
                state += 1
    
    if state == 3:
        if accMag > 3:
            wiimote.rumble(True)
            if not effect.busy():
                effect.sound("audio/bell2.wav")
                state += 1

    if state == 4:
        if angles[1] < -80:
            wiimote.rumble(True)
            if not effect.busy():
                effect.sound("audio/bubbles.wav")
                state = 0

    time.sleep(.2)
    wiimote.rumble(False)

