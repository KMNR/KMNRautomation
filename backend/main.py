from time import localtime, strftime, time, sleep
import configparser

from backend.playlist_handler import playlist_handler
from backend.station_id_handler import station_id_handler
from backend.constants import ConstantStrings


def main():
    # On initial start, assume we haven't played anything
    played_top_hour = False
    played_20_mins = False
    played_40_mins = False

    # set time of last educational segment play to epoch
    last_edu_segment_time = 1

    # Toggle to gracefully shutdown automation after next iteration of main loop
    run_automation = True

    # Read configuration file
    cfg = configparser.ConfigParser()
    cfg.read("settings.ini")
    edu_time_delay = int(cfg["General"]["edu_time_delay"])
    debug = bool(cfg["General"]["debug_logging"])

    # Core loop begins here
    while run_automation:
        # Check current time
        current_epoch_time = time()
        hours, minutes, am_pm = strftime("%I %M %p", localtime(current_epoch_time)).split(" ")
        hours = int(hours)
        minutes = int(minutes)
        print(hours, minutes, am_pm)

        # Top of the hour ID
        if minutes < 10 and not played_top_hour:
            print(ConstantStrings.PLAYING_TOP_HOUR)
            played_top_hour = True
            played_20_mins = False
            played_40_mins = False
            station_id_handler(hours, minutes, am_pm)

        # 20 minutes past ID
        if 18 < minutes < 25 and not played_20_mins:
            print(ConstantStrings.PLAYING_20_MINS)
            played_20_mins = True
            played_top_hour = False
            played_40_mins = False
            station_id_handler(hours, minutes, am_pm)

        # 40 minutes past ID
        if minutes > 38 and not played_40_mins:
            print(ConstantStrings.PLAYING_40_MINS)
            played_40_mins = True
            played_top_hour = False
            played_20_mins = False
            station_id_handler(hours, minutes, am_pm)

        # Check for educational segment
        # If we haven't played an educational segment in edu_time_delay seconds
        if (current_epoch_time - edu_time_delay) > last_edu_segment_time:
            print(ConstantStrings.PLAYING_EDU_SEGMENT)
            last_edu_segment_time = current_epoch_time
            # Play educational segment here
            continue

        # Play song
        playlist_handler()
        print(ConstantStrings.PLAYING_SONG)
        sleep(1)


if __name__ == "__main__":
    main()
