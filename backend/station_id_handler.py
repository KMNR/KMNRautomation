import random, os
import time
from datetime import datetime
from mutagen.mp3 import MP3
import player
random.seed(datetime.now())

def station_id_handler(min):
    #if close to the top of the hour, play a legal id
    if min<10 or min>50:
        player.play("backend/legal-station-IDs/"+random.choice(os.listdir("backend/legal-station-IDs")))
    else:
        #play a non-legal ID
        player.play("backend/non-legal-station-IDs/"+random.choice(os.listdir("backend/non-legal-station-IDs")))
