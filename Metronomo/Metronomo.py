import winsound
import time 

baud = 60 
freq = baud / 60 
t = 1/ freq 

middle = False
dtime = 0 
while True:
    time_now = time.time() 
    while time.time() - time_now < (t - dtime) : 
        if middle is False and time.time() - time_now > ((t/2)-dtime):
            winsound.Beep(1000, int(t*25) )
            middle = True             
    winsound.Beep(2000, int(t*25) )
    dtime = time.time() - time_now - t  
    middle = False