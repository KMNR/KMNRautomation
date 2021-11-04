from time import localtime, strftime, time, sleep
import configparser
import random
import os

import playlist_handler
import station_id_handler
import constants

random.seed()

def main():
    # On initial start, assume we haven't played anything
    played_top_hour = False
    played_20_mins = False
    played_40_mins = False

    #start with no playlists or songs played yet
    current_playlist_path = ""
    recent_playlists = ["",""]
    current_song_index = 0

    # set time of last educational segment play to epoch
    last_edu_segment_time = 1

    # Toggle to gracefully shutdown automation after next iteration of main loop
    run_automation = True

    # Read configuration file
    '''
    cfg = configparser.ConfigParser()
    cfg.read("settings.ini")
    edu_time_delay = int(cfg["General"]["edu_time_delay"])
    debug = True if cfg["General"]["debug_logging"] == "true" else False
    print(debug)
    '''
    edu_time_delay = 1500
    # Core loop begins here
    while run_automation:
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
            station_id_handler.station_id_handler(minutes)

        # 20 minutes past ID
        if 18 < minutes < 25 and not played_20_mins:
            print(constants.ConstantStrings.PLAYING_20_MINS)
            played_20_mins = True
            played_top_hour = False
            played_40_mins = False
            station_id_handler.station_id_handler(minutes)

        # 40 minutes past ID
        if minutes > 38 and not played_40_mins:
            print(constants.ConstantStrings.PLAYING_40_MINS)
            played_40_mins = True
            played_top_hour = False
            played_20_mins = False
            station_id_handler.station_id_handler(minutes)

        # Check for educational segment
        # If we haven't played an educational segment in edu_time_delay seconds
        if (current_epoch_time - edu_time_delay) > last_edu_segment_time:
            print(constants.ConstantStrings.PLAYING_EDU_SEGMENT)
            last_edu_segment_time = current_epoch_time
            # Play educational segment here
            continue

        # Play song
        while(current_playlist_path in recent_playlists):
            current_playlist_path = constants.MEDIA_ROOT_DIRECTORY + constants.PLAYLISTS_SUBDIRECTORY + "/" + random.choice(os.listdir(constants.MEDIA_ROOT_DIRECTORY + constants.PLAYLISTS_SUBDIRECTORY))

        current_song_index = playlist_handler.playlist_handler(current_playlist_path, current_song_index)
        print(constants.ConstantStrings.PLAYING_SONG)

        if current_song_index==-1:
            #update the list of recently played playlists
            recent_playlists.pop()
            recent_playlists.insert(0,current_playlist_path)
            #print(recent_playlists)

        sleep(1)

if __name__ == "__main__":
    main()
