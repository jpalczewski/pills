import daemon, time, asyncio, aiocron
from hardware.dht import poll_once
from hardware.lcd.driver import update_LCD

debugMode : bool = True

async def debugLCD():
    humidity, temperature = await poll_once()
    update_LCD("{:.2f}% {:.2f} C".format(humidity, temperature))
    print("k")

if debugMode:
    cron = aiocron.crontab('*/1 * * * *', func=debugLCD, start=True)


    

asyncio.get_event_loop().run_forever()
    
    
    