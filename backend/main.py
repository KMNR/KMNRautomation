#! /usr/bin/env python
from time import localtime, strftime, time, sleep
import signal
import configparser
import random
import os
import weather_fetcher
import news_fetcher
import town_and_campus_fetcher
import playlist_handler
import station_id_handler
import time_handler
import programming_handler
import programming_logging_handler
import music_logging_handler
import constants

def main():
    random.seed()
    # On initial start, assume we haven't played anything
    played_top_hour = False
    played_20_mins = False
    played_40_mins = False

    #start with no playlists or songs played yet
    current_playlist_path = ""
    recent_playlists = ["","","","","","","","","","","","","",""]
    current_song_index = 0

    # set time of last educational segment play to epoch
    last_edu_segment_time = 1
    edu_segs_this_hour = 0

    #start with logging off until we get it from the file
    logging="False"

    # Toggle to gracefully shutdown automation after next iteration of main loop
    run_automation = True

    # Start with logging on
    if os.getenv('LOGGING')==None:
        os.environ['LOGGING']="True"

    #create at least one weather forecast, news article, and town and campus news reading on startup
    news_fetcher.news_fetcher()
    weather_fetcher.main()
    town_and_campus_fetcher.town_and_campus_fetcher()


    # Read configuration file
    cfg = configparser.ConfigParser()
    cfg.read(constants.CONFIG_FILE_PATH)
    edu_time_delay = int(cfg["General"]["edu_time_delay"])
    debug = True if cfg["General"]["debug_logging"] == "true" else False
    print(debug)

    # Terminate any orphaned mpv instances
    # This would apply if we are recovering from an unexpected failure of the python script
    # In this case, the old mpv instance would still be running while the script is reloading
    # Causing double-play, which is pretty gross
    os.system("pkill -f mpv")
    # Core loop begins here
    while True:
        # Check logging status
        f=open(constants.BACKEND_ROOT_DIRECTORY+constants.LOGGING_STATUS_PATH)
        logging=f.read()
        logging=logging.strip()
        f.close()

        # Check current time
        current_epoch_time = time()
        hours, minutes, am_pm = strftime("%I %M %p", localtime(current_epoch_time)).split(" ")
        #print(hours,minutes,am_pm)
        hours = int(hours)
        minutes = int(minutes)
        print(hours, minutes, am_pm)

        # Top of the hour ID
        if minutes < 10 and not played_top_hour:
            print(constants.ConstantStrings.PLAYING_TOP_HOUR)
            played_top_hour = True
            played_20_mins = False
            played_40_mins = False
            edu_segs_this_hour = 0
            station_id_handler.station_id_handler(minutes,logging)
            time_handler.time_handler(hours, minutes, am_pm)

        # 20 minutes past ID
        if 18 < minutes < 25 and not played_20_mins:
            print(constants.ConstantStrings.PLAYING_20_MINS)
            played_20_mins = True
            played_top_hour = False
            played_40_mins = False
            station_id_handler.station_id_handler(minutes,logging)
            time_handler.time_handler(hours, minutes, am_pm)

        # 40 minutes past ID
        if minutes > 38 and not played_40_mins:
            print(constants.ConstantStrings.PLAYING_40_MINS)
            played_40_mins = True
            played_top_hour = False
            played_20_mins = False
            station_id_handler.station_id_handler(minutes,logging)
            time_handler.time_handler(hours, minutes, am_pm)

        # Check for educational segment
        # If we haven't played an educational segment in edu_time_delay seconds
        if (current_epoch_time - edu_time_delay) > last_edu_segment_time:
            print(constants.ConstantStrings.PLAYING_EDU_SEGMENT)

            last_edu_segment_time = current_epoch_time
            # Play educational segment here
            if(programming_handler.programming_handler(edu_segs_this_hour, hours, am_pm,logging)):
                edu_segs_this_hour+=1

        # Choose the next playlist
        while(current_playlist_path in recent_playlists):
            current_playlist_path = constants.MEDIA_ROOT_DIRECTORY + constants.PLAYLISTS_SUBDIRECTORY + "/" + random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY + constants.PLAYLISTS_SUBDIRECTORY))

        current_song_index = playlist_handler.playlist_handler(current_playlist_path, current_song_index)
        print(constants.ConstantStrings.PLAYING_SONG)

        #after a playlist ends,
        if current_song_index==-1:
            #update the list of recently played playlists
            recent_playlists.pop()
            recent_playlists.insert(0,current_playlist_path)
            #log the playlist
            if logging=="True":
                music_logging_handler.music_logging_handler(current_playlist_path)
            #start next playlist from song at index 0
            current_song_index=0
            #print(recent_playlists)

        sleep(1)

        current_song_index = playlist_handler.playlist_handler(current_playlist_path, current_song_index)
        print(constants.ConstantStrings.PLAYING_SONG)

        #after a playlist ends,
        if current_song_index==-1:
            #update the list of recently played playlists
            recent_playlists.pop()
            recent_playlists.insert(0,current_playlist_path)
            #log the playlist
            if logging=="True":
                music_logging_handler.music_logging_handler(current_playlist_path)
            #start next playlist from song at index 0
            current_song_index=0
            #print(recent_playlists)

        sleep(1)

if __name__ == "__main__":
    main()
