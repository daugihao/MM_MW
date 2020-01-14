import time

from accel import convertAcc

from wii import Wiimote
from effects import Effect

'''Set up Audio'''
wiimote = Wiimote()
effect = Effect()

'''Main loop'''
while True:
    acc = convertAcc(wiimote.accel(), 1)
    print('x: {0:.2f}'.format(acc[0]))
    print('y: {0:.2f}'.format(acc[1]))
    print('z: N/A')
    wiimote.rumble(False)
    if acc[1] > 45:
       wiimote.rumble(True)
       if not effect.busy():
           effect.sound("audio/bubbles.wav")
    time.sleep(.2)

