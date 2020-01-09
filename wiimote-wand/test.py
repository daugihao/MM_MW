import cwiid 
import time
from playsound import playsound

OFFSET = -120.0
GAIN = 1.0/24.0


def convertAcc(raw):
    return tuple([GAIN*(axis + OFFSET) for axis in raw])


print("Press 1+2 on your Wiimote now...")

wm = None
i = 1

'''Connect to Wiimote'''
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

'''Main loop'''
while True:
    acc = convertAcc(wm.state['acc'])
    print('x: {0:.2f}'.format(acc[0]))
    print('y: {0:.2f}'.format(acc[1]))
    print('z: {0:.2f}'.format(acc[2]))
    wm.rumble = (acc[1] > 0.2)
    if wm.state['buttons'] & cwiid.BTN_A:
        wm.led = (wm.state['led'] + 1) % 16
    time.sleep(.2)

