import RPi.GPIO as GPIO
import time

#GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
#GPIO.output(22, GPIO.HIGH)

def setInProgress():
    GPIO.output(26, True)
    GPIO.output(16, False)

def setReady():
    GPIO.output(16, True)
    GPIO.output(26, False)

def setOff():
    GPIO.output(16, False)
    GPIO.output(26, False)
    #GPIO.cleanup()

