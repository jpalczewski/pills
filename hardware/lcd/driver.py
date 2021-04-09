import time
from RPLCD.i2c import CharLCD
from typing import AnyStr


def update_LCD(msg: str):
    lcd = CharLCD('PCF8574', 0x27)
    lcd.write_string(msg)
