import time
import board
import pwmio
from adafruit_motor import servo

rightServoPin = pwmio.PWMOut(board.D17, frequency=50)
leftServoPin = pwmio.PWMOut(board.D27, frequency=50)


rightServo = servo.ContinuousServo(rightServoPin)
leftServo = servo.ContinuousServo(leftServoPin)
     
def right_rotate():
    rightServo.throttle = 0.08
    time.sleep(0.1)
    rightServo.throttle = 0.0

def left_rotate():
    leftServo.throttle = 0.08
    time.sleep(0.1)
    leftServo.throttle = 0.0
