from hardware.led import *
from hardware.lcd.driver import update_LCD
from hardware.servo import left_rotate, right_rotate
import time
#setOff()

setInProgress()
update_LCD("Prosze czekac,pracuje :)")
time.sleep(1)
right_rotate()

time.sleep(2)
setReady()
update_LCD("Napracowane :D")
time.sleep(10)
setOff()
