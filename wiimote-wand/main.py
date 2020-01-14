import cwiid 
import time
import pygame

from accel import convertAcc
from effects import Effect


'''Connect to Wiimote'''
print("Press 1+2 on your Wiimote now...")

i = 1
wm = None

while not wm:
    try:
        wm=cwiid.Wiimote()
    except RuntimeError:
        if (i>10):
            quit()
            break
        print("Error opening Wiimote connection")
        print("Attempt No: " + str(i))
        i += 1

print("Successfully connected to Wiimote!")
wm.led = 9  # Show successful connection on Wiimote 

'''Configure Wiimote'''
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
time.sleep(1)  # Wait for configuration to be accepted and true values are returned

'''Set up Audio'''
effect = Effect()

'''Main loop'''
while True:
    acc = convertAcc(wm.state['acc'], 1)
    print('x: {0:.2f}'.format(acc[0]))
    print('y: {0:.2f}'.format(acc[1]))
    print('z: N/A')
    wm.rumble = False
    if acc[1] > 45:
        wm.rumble = True
        if not effect.busy():
            effect.sound("audio/bubbles.wav")
    if wm.state['buttons'] & cwiid.BTN_A:
        wm.led = (wm.state['led'] + 1) % 16
    time.sleep(.2)

