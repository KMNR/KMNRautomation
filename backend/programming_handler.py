import random, os
from datetime import datetime
from mutagen.mp3 import MP3
import player
import weather_handler
import news_handler
import town_and_campus_handler
import weather_fetcher
import news_fetcher
import town_and_campus_fetcher
import programming_logging_handler
import constants
import csv
from gtts import gTTS

test=True

# Prerequisites: Passing number of segments already played this hour, the current hour, the AM/PM status, and a boolean indicating whether logging is on or not
# Description: Given the current hour and number of programming segments already played this hour,
# reads from the daily_programming_schedule.txt file what programming should be played with this call, if any
# Return: 1 if a programming segment was played, 0 if it was not
def programming_handler(segs_played, hour, am_pm, logging):
    random.seed(datetime.now())
    seg_to_play=""
    #sets number of segments to play to 1 if between 10pm and 6am, and 2 otherwise
    hourly_segs_count=(((hour<6 or hour==12) and am_pm=="am") or (hour>=10 and hour<12 and am_pm=="pm"))
    hourly_segs_count=(hourly_segs_count-2)*-1
    #print(hourly_segs_count)
    fileName=""
    filePath=""
    exit_status=0

    date = datetime.today()

    if (segs_played>=hourly_segs_count):
        print("already played required educational segments for the hour!")
        return 0
    else:
        #put the programming schedule into a list to be parsed easily
        with open(constants.BACKEND_ROOT_DIRECTORY+constants.PROGRAMMING_SCHEDULE_PATH, newline='\n') as f:
            reader = csv.reader(f)
            data = list(reader)

        for set in data:
            #find the time that matches the current time
            if (int(set[0])==int(hour) and set[1].strip().lower()==am_pm.lower()):
                #if there hasn't been a segment played this hour, play the first segment assigned for this hour
                if segs_played==0:
                    seg_to_play=set[2]
                    break
                #if there's already been a segment played this hour, play the second segment assigned for this hour
                elif len(set)>=4 and segs_played==1:
                    seg_to_play=set[3]
                    break
                else:
                    break

        #if it's an mp3 segment, give the file path to the player function
        if seg_to_play.strip() in constants.MP3_SEGS:
            #profile america is special because there are specific ones for each date
            if seg_to_play.strip()==constants.PROFILE_AMERICA_SUBDIRECTORY:
                #make the filename from the date
                profile_america_filename = date.strftime("%Y%m%d")
                profile_america_filename = "pa"+profile_america_filename[2:]+".mp3"
                exit_status=player.play(constants.MEDIA_ROOT_DIRECTORY+constants.PROGRAMMING_SUBDIRECTORY+constants.PROFILE_AMERICA_SUBDIRECTORY+"/"+profile_america_filename)
                if (exit_status and logging=="True"):
                    programming_logging_handler.programming_logging_handler(profile_america_filename,constants.MEDIA_ROOT_DIRECTORY+constants.PROGRAMMING_SUBDIRECTORY+constants.PROFILE_AMERICA_SUBDIRECTORY+"/"+profile_america_filename,constants.PROFILE_AMERICA_SUBDIRECTORY)
                return exit_status

            #if there are subdirectories for that programming type, choose a subdirectory and an mp3 file
            elif seg_to_play in constants.ADDITIONAL_SUBDIRECTORY_SEGS:
                chosen_subdirectory=random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY + constants.PROGRAMMING_SUBDIRECTORY + seg_to_play.strip()))
                fileName=random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY + constants.PROGRAMMING_SUBDIRECTORY + seg_to_play.strip() + '/' + chosen_subdirectory))
                filePath=constants.MEDIA_ROOT_DIRECTORY + constants.PROGRAMMING_SUBDIRECTORY + seg_to_play.strip() + '/' + chosen_subdirectory + '/' + fileName
                exit_status = player.play(filePath)
                if (exit_status and logging=="True"):
                    programming_logging_handler.programming_logging_handler(fileName,filePath,seg_to_play.strip())
                return exit_status
            else:
                fileName=random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY + constants.PROGRAMMING_SUBDIRECTORY + seg_to_play.strip()))
                filePath=constants.MEDIA_ROOT_DIRECTORY + constants.PROGRAMMING_SUBDIRECTORY + seg_to_play.strip() + '/' + fileName
                exit_status=player.play(filePath)
                if (exit_status and logging=="True"):
                    programming_logging_handler.programming_logging_handler(fileName,filePath,seg_to_play.strip())
                return exit_status
        #town and campus news, news and weather, or concert news
        elif seg_to_play.strip() in constants.TTS_SEGS:
            if seg_to_play.strip() == constants.NEWS_AND_WEATHER_ID:
                news_successs = news_handler.news_handler()
                news_fetcher.news_fetcher()
                weather_success = weather_handler.weather_handler()
                weather_fetcher.main()
                exit_status = news_successs and not weather_success
                if (exit_status and logging=="True"):
                    programming_logging_handler.programming_logging_handler(None,None,constants.NEWS_AND_WEATHER_ID)
                return exit_status

            elif seg_to_play.strip() == constants.TOWN_AND_CAMPUS_SUBDIRECTORY:
                exit_status = town_and_campus_handler.town_and_campus_handler()
                town_and_campus_fetcher.town_and_campus_fetcher()
                if (exit_status and logging=="True"):
                    programming_logging_handler.programming_logging_handler(None,None,constants.TOWN_AND_CAMPUS_SUBDIRECTORY)
                return exit_status

            elif seg_to_play.strip() == constants.CONCERT_NEWS_SUBDIRECTORY:
                f = open(constants.BACKEND_ROOT_DIRECTORY+"concert-news.txt")
                concert_news_text = f.read()
                tts = gTTS(concert_news_text, lang='en')
                tts.save(constants.MEDIA_ROOT_DIRECTORY+constants.PROGRAMMING_SUBDIRECTORY+constants.CONCERT_NEWS_SUBDIRECTORY+"/concert_news.mp3")
                exit_status=player.play(constants.MEDIA_ROOT_DIRECTORY+constants.PROGRAMMING_SUBDIRECTORY+constants.CONCERT_NEWS_SUBDIRECTORY+"/concert_news.mp3")
                if (exit_status and logging=="True"):
                    programming_logging_handler.programming_logging_handler(None,constants.MEDIA_ROOT_DIRECTORY+constants.PROGRAMMING_SUBDIRECTORY+constants.CONCERT_NEWS_SUBDIRECTORY+"/concert_news.mp3",constants.CONCERT_NEWS_SUBDIRECTORY)
                return exit_status
            else:
                print("couldn't recognize the path as a valid edu segment!")
                return(0)

        else:
            print("couldn't recognize the path as a valid edu segment!")
            return(0)

if __name__ == '__main__':
    programming_handler(1, 7, "pm", True)
