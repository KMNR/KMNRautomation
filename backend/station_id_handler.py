import random, os
import time
from datetime import datetime
from mutagen.mp3 import MP3
import player
import constants
random.seed(datetime.now())

def station_id_handler(min):
    #if close to the top of the hour, play a legal id
    if min<10 or min>50:
        player.play(constants.MEDIA_ROOT_DIRECTORY+constants.LEGAL_STATION_ID_SUBDIRECTORY+random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY+constants.LEGAL_STATION_ID_SUBDIRECTORY)))
    else:
        #play a non-legal ID
        player.play(constants.MEDIA_ROOT_DIRECTORY+constants.NONLEGAL_STATION_ID_SUBDIRECTORY+random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY+constants.NONLEGAL_STATION_ID_SUBDIRECTORY)))

if __name__ == '__main__':
    station_id_handler(0)
