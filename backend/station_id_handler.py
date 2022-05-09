import random, os
from datetime import datetime
#from mutagen.mp3 import MP3
import player
import constants
import programming_logging_handler
import threading

test=False

# Prerequisites: Passing min as an integer to denote what minute of the hour it currently is, passing logging as bool to indicate whether station_id should be logged
# Description: Chooses a random station ID to play and calls the media player to play it.
# Will always choose a legal station ID if within +/-10 minutes of the top of an hour
# Calls logging function to log each legal, top of the hour station ID
def station_id_handler(min,logging):
    random.seed(datetime.now())
    if test:
        constants.MEDIA_ROOT_DIRECTORY="media"
    #if close to the top of the hour, play a legal id
    if min<10:
        fileName=random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY+constants.LEGAL_STATION_ID_SUBDIRECTORY))
        filePath=constants.MEDIA_ROOT_DIRECTORY+constants.LEGAL_STATION_ID_SUBDIRECTORY+fileName
        #if the station ID played properly and we're loggging, log it
        if player.play(filePath) and logging=="True":
            programming_logging_handler.programming_logging_handler(fileName,filePath,constants.LEGAL_STATION_ID_SUBDIRECTORY)
    else:
        #player.play(constants.MEDIA_ROOT_DIRECTORY+constants.NONLEGAL_STATION_ID_SUBDIRECTORY+random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY+constants.NONLEGAL_STATION_ID_SUBDIRECTORY)))
        #play a legal or non-legal ID
        if random.choice((0,1))==0:
            logging_thread = threading.Thread(target=player.play(constants.MEDIA_ROOT_DIRECTORY+constants.NONLEGAL_STATION_ID_SUBDIRECTORY+random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY+constants.NONLEGAL_STATION_ID_SUBDIRECTORY))),name="Logging station ID")
            logging_thread.start()
        else:
            player.play(constants.MEDIA_ROOT_DIRECTORY+constants.LEGAL_STATION_ID_SUBDIRECTORY+random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY+constants.LEGAL_STATION_ID_SUBDIRECTORY)))

if __name__ == '__main__':
    station_id_handler(0,True)
