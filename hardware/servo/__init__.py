import time
import board
import pwmio
from adafruit_motor import servo



     
def right_rotate():
    rightServoPin = pwmio.PWMOut(board.D17, frequency=50)
    rightServo = servo.ContinuousServo(rightServoPin)
    rightServo.throttle = 0.08
    time.sleep(0.1)
    rightServo.throttle = 0.0

def left_rotate():
    leftServoPin = pwmio.PWMOut(board.D27, frequency=50)
    leftServo = servo.ContinuousServo(leftServoPin)
    leftServo.throttle = 0.08
    time.sleep(0.1)
    leftServo.throttle = 0.0