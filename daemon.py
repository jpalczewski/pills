import daemon, time, asyncio, aiocron
from hardware.dht import poll_once
from hardware.lcd.driver import update_LCD
from actions.rotate import rotate_left, rotate_right
from config import config
import pyrebase
debugMode : bool = True


async def debugLCD():
    humidity, temperature = await poll_once()
    update_LCD("{:.2f}% {:.2f} C".format(humidity, temperature))
    print("k")


async def commandPoll():
    global db 
    while True:
        l = db.child("rotate").child("left").get()
        r = db.child("rotate").child("right").get()
        if l.val() is not None:
            rotate_left()
            db.child("rotate").child("left").remove()
        if r.val() is not None:
            rotate_left()
            db.child("rotate").child("right").remove()
            rotate_right()
        
        await asyncio.sleep(5)


@aiocron.crontab('*/1 * * * *')
async def temperature2cloud():
    global db
    humidity, temperature = await poll_once()
    db.child("strasbourg").push({"time": time.time(), "temperature": temperature, "humidity": humidity})


if debugMode:
    cron = aiocron.crontab('*/2 * * * *', func=debugLCD, start=True)




firebase = pyrebase.initialize_app(config)    

db = firebase.database()
startupMessage = {"time": time.time()}
db.child("startup").push(startupMessage)
strasbourg = db.child("strasbourg")

asyncio.run(commandPoll())
asyncio.get_event_loop().run_forever()
    
    
    