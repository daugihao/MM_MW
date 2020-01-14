import time

from accel import convertAcc

from wii import Wiimote
from effects import Effect

'''Set up Audio'''
wiimote = Wiimote()
effect = Effect()

state = 0

'''Main loop'''
while True:
    acc = convertAcc(wiimote.accel(), 1)
    print('x: {0:.2f}'.format(acc[0]))
    print('y: {0:.2f}'.format(acc[1]))
    print('z: N/A')

    if state == 0:
        if acc[1] > 45:
           wiimote.rumble(True)
           if not effect.busy():
               effect.sound("audio/bubble.wav")
               state += 1

    if state == 1:
        if acc[0] > 45:
            wiimote.rumble(True)
            if not effect.busy():
                effect.sound("audio/bubble.wav")
                state += 1

    if state == 2:
        if acc[1] < -80:
            wiimote.rumble(True)
            if not effect.busy():
                effect.sound("audio/bubbles.wav")
                state = 0

    time.sleep(.2)
    wiimote.rumble(False)

