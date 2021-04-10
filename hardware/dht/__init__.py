from .DHT22 import sensor
import time

import pigpio


async def poll_once():
    pi = pigpio.pi()
    s = sensor(pi, 24, LED=None, power=None,DHT11=False)
    s.trigger()
    time.sleep(0.2)

    humidity = s.humidity()
    temperature =  s.temperature()

    s.cancel()
    pi.stop()
    return (humidity, temperature)