import daemon, time, asyncio, aiocron
from hardware.dht import poll_once
from hardware.lcd.driver import update_LCD
from config import config
import pyrebase
debugMode : bool = True

async def debugLCD():
    humidity, temperature = await poll_once()
    update_LCD("{:.2f}% {:.2f} C".format(humidity, temperature))
    print("k")

if debugMode:
    cron = aiocron.crontab('*/1 * * * *', func=debugLCD, start=True)




firebase = pyrebase.initialize_app(config)    

asyncio.get_event_loop().run_forever()
    
    
    