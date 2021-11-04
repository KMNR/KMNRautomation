import random, os
import time
from datetime import datetime
from mutagen.mp3 import MP3
import player
import constants
random.seed(datetime.now())

test=True

# Prerequisites: Passing min as an integer to denote what minute of the hour it currentlyis
# Description: Chooses a random station ID to play and calls the media player to play it.
# Will always choose a legal station ID if within +/-5 minutes of the top of an hour
def station_id_handler(min):
    if test:
        constants.MEDIA_ROOT_DIRECTORY="media"
    #if close to the top of the hour, play a legal id
    if min<5 or min>55:
        player.play(constants.MEDIA_ROOT_DIRECTORY+constants.LEGAL_STATION_ID_SUBDIRECTORY+random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY+constants.LEGAL_STATION_ID_SUBDIRECTORY)))
    else:
        #player.play(constants.MEDIA_ROOT_DIRECTORY+constants.NONLEGAL_STATION_ID_SUBDIRECTORY+random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY+constants.NONLEGAL_STATION_ID_SUBDIRECTORY)))
        #play a legal or non-legal ID
        if random.choice((0,1))==0:
            player.play(constants.MEDIA_ROOT_DIRECTORY+constants.NONLEGAL_STATION_ID_SUBDIRECTORY+random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY+constants.NONLEGAL_STATION_ID_SUBDIRECTORY)))
        else:
            player.play(constants.MEDIA_ROOT_DIRECTORY+constants.LEGAL_STATION_ID_SUBDIRECTORY+random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY+constants.LEGAL_STATION_ID_SUBDIRECTORY)))

if __name__ == '__main__':
    station_id_handler(30)
