from hardware.dht.DHT22 import sensor
import time

import pigpio

# Intervals of about 2 seconds or less will eventually hang the DHT22.
INTERVAL=3

pi = pigpio.pi()
s = sensor(pi, 24, LED=None, power=None,DHT11=False)
s.trigger()
time.sleep(0.2)

print(" {} {} {:3.2f} {} {} {} {}".format(
          s.humidity(), s.temperature(), s.staleness(),
         s.bad_checksum(), s.short_message(), s.missing_message(),
         s.sensor_resets()))

s.cancel()
pi.stop()

