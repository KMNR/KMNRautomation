import random, os
from datetime import datetime
from mutagen.mp3 import MP3
import player
import constants
import csv
random.seed(datetime.now())

test=True

# Prerequisites:
# Description:
# Return: 1 if a programming segment was played, 0 if it was not
def programming_handler(segs_played, hour, am_pm):
    seg_to_play=""
    #sets hourly_segs_count to 1 if between 10pm and 6am, and 2 otherwise
    hourly_segs_count=(((hour<6 or hour==12) and am_pm=="am") or (hour>=10 and hour<12 and am_pm=="pm"))
    hourly_segs_count=(hourly_segs_count-2)*-1
    #print(hourly_segs_count)

    if (segs_played>=hourly_segs_count):
        return 0
    else:
        with open(constants.BACKEND_ROOT_DIRECTORY+'daily_programming_schedule.txt', newline='\n') as f:
            reader = csv.reader(f)
            data = list(reader)
        #print(data)
        for set in data:
            if (int(set[0])==hour and set[1].strip()==am_pm):
                if segs_played==0:
                    seg_to_play=set[2]
                    break
                elif segs_played==1:
                    seg_to_play=set[3]
                    break

        if seg_to_play.strip() in constants.MP3_SEGS:
            #profile america is special because there are specific ones for each date
            if seg_to_play=="profile-america":
                print("play profile america here")
            else:
                return(player.play(constants.MEDIA_ROOT_DIRECTORY + constants.PROGRAMMING_SUBDIRECTORY + seg_to_play.strip() + '/' + random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY + constants.PROGRAMMING_SUBDIRECTORY + seg_to_play.strip()))))
        else:
            print("play TTS programming here")

if __name__ == '__main__':
    programming_handler(0, 11, "am")
