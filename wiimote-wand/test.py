import cwiid 
import time 

print("Press 1+2 on your Wiimote now...")

wm = None
i = 2

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

wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
time.sleep(5)

wm.led = 1

while True:
    x = (wm.state['acc'][0]-120)/24.0
    y = (wm.state['acc'][1]-120)/24.0
    z = (wm.state['acc'][2]-120)/24.0
    print('x: {0:.2f}'.format(x))
    print('y: {0:.2f}'.format(y))
    print('z: {0:.2f}'.format(z))
    #wm.rumble = (wm.state['acc'][0] < 126)
    if wm.state['buttons'] & cwiid.BTN_A:
        wm.led = (wm.state['led'] + 1) % 16
    time.sleep(.2)

'''while(True):
    print(wm.state)
    time.sleep(1)'''

'''for i in range(16):
    wm.led = i
    if i%3:
        wm.rumble = False
    else:
        wm.rumble = True
    time.sleep(0.5)
wm.rumble = False'''
