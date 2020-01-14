import cwiid 
import time
import pygame

from accel import convertAcc


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
pygame.mixer.init()

'''Main loop'''
while True:
    acc = convertAcc(wm.state['acc'], 1)
    print('x: {0:.2f}'.format(acc[0]))
    print('y: {0:.2f}'.format(acc[1]))
    print('z: N/A')
    wm.rumble = False
    if acc[1] > 45:
        wm.rumble = True
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.load("audio/bubbles.wav")
            pygame.mixer.music.play()
    if wm.state['buttons'] & cwiid.BTN_A:
        wm.led = (wm.state['led'] + 1) % 16
    time.sleep(.2)

