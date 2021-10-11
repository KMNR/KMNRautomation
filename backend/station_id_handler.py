import random, os
import time
from datetime import datetime
from mutagen.mp3 import MP3
random.seed(datetime.now())

def station_id_handler(hour, min, am_pm):
    #if close to the top of the hour, play a legal id
    if min<10 or min>50:
        ID = "backend/legal-station-IDs/"+random.choice(os.listdir("backend/legal-station-IDs"))
        os.system("start "+ID)
        #wait until it's done playing before doing anything else
        time.sleep(int(MP3(ID).info.length))
    else:
        #play a non-legal ID
        pass

    if hour=1:
        pass
    elif hour=2:
        pass
    elif hour=3:
        pass
    elif hour=4:
        pass
    elif hour=5:
        pass
    elif hour=6:
        pass
    elif hour=7:
        pass
    elif hour=8:
        pass
    elif hour=9:
        pass
    elif hour=10:
        pass
    elif hour=11:
        pass
    elif hour=12:
        pass
