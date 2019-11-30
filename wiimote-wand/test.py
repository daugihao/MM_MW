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

#wm.rpt_mode = cwwid.RPT_BIN | cwiid.RPT_ACC

for i in range(16):
    wm.led = i
    if i%3:
        wm.rumble = False
    else:
        wm.rumble = True
    time.sleep(0.5)
wm.rumble = False
