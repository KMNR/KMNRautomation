import random, os
from datetime import datetime
from mutagen.mp3 import MP3
import player
import constants
import csv
random.seed(datetime.now())

test=True

# Prerequisites: Passing number of segments already played this hour, the current hour, and the AM/PM status
# Description: Given the current hour and number of programming segments already played this hour,
# reads from the daily_programming_schedule.txt file what programming should be played with this call, if any
# Return: 1 if a programming segment was played, 0 if it was not
def programming_handler(segs_played, hour, am_pm):
    seg_to_play=""
    #sets number of segments to play to 1 if between 10pm and 6am, and 2 otherwise
    hourly_segs_count=(((hour<6 or hour==12) and am_pm=="am") or (hour>=10 and hour<12 and am_pm=="pm"))
    hourly_segs_count=(hourly_segs_count-2)*-1
    #print(hourly_segs_count)

    if (segs_played>=hourly_segs_count):
        return 0
    else:
        #put the programming schedule into a list to be parsed easily
        with open(constants.BACKEND_ROOT_DIRECTORY+'daily_programming_schedule.txt', newline='\n') as f:
            reader = csv.reader(f)
            data = list(reader)

        for set in data:
            #find the time that matches the current time
            if (int(set[0])==hour and set[1].strip()==am_pm):
                #if there hasn't been a segment played this hour, play the first segment assigned for this hour
                if segs_played==0:
                    seg_to_play=set[2]
                    break
                #if there's already been a segment played this hour, play the second segment assigned for this hour
                elif segs_played==1:
                    seg_to_play=set[3]
                    break

        #if it's an mp3 segment, give the file path to the player function
        if seg_to_play.strip() in constants.MP3_SEGS:
            #profile america is special because there are specific ones for each date
            if seg_to_play=="profile-america":
                print("play profile america here")
            else:
                return(player.play(constants.MEDIA_ROOT_DIRECTORY + constants.PROGRAMMING_SUBDIRECTORY + seg_to_play.strip() + '/' + random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY + constants.PROGRAMMING_SUBDIRECTORY + seg_to_play.strip()))))
        #otherwise, call the appropriate handler for that programming:
        #   town and campus news, news and weather, or concert news
        else:
            print("play TTS programming here")

if __name__ == '__main__':
    programming_handler(0, 11, "am")
