import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from hardware.led import *
from hardware.lcd.driver import update_LCD
import hardware.servo
import time

# setOff()


def _initial_msg():
    setInProgress()
    update_LCD("Prosze czekac,pracuje :)")
    time.sleep(1)


def rotate_left():
    _initial_msg()
    hardware.servo.left_rotate()
    _end_msg()

def rotate_right():
    _initial_msg()
    hardware.servo.right_rotate()
    _end_msg


def _end_msg():
    time.sleep(2)
    setReady()
    update_LCD("Napracowane :D")
    time.sleep(10)
    setOff()

