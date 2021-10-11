from backend.constants import MEDIA_ROOT_DIRECTORY, TIME_SUBDIRECTORY, HOUR_SUBDIRECTORY, MINUTE_SUBDIRECTORY, \
    AM_PM_SUBDIRECTORY
import random
import os

random.seed()
test = True


# Prerequisites: Passing hour, minute as integers. am_pm is either AM or PM as string (case insensitive)
# Description: Chooses a random file from the provided media root directory for hour, minute second
# and passes the absolute file path as an argument to the media handler function.
def time_handler(hour, minute, am_pm):
    if test:
        MEDIA_ROOT_DIRECTORY = "../media"
    print(os.listdir(MEDIA_ROOT_DIRECTORY))
    hr_media_folder = MEDIA_ROOT_DIRECTORY + TIME_SUBDIRECTORY + HOUR_SUBDIRECTORY + str(hour)
    min_media_folder = MEDIA_ROOT_DIRECTORY + TIME_SUBDIRECTORY + MINUTE_SUBDIRECTORY + str(minute)
    am_pm_media_folder = MEDIA_ROOT_DIRECTORY + TIME_SUBDIRECTORY + AM_PM_SUBDIRECTORY + str(am_pm).lower()
    if test:
        print(hr_media_folder)
        print(min_media_folder)
        print(am_pm_media_folder)
    hr_audio_to_play = hr_media_folder + "/" + random.choice(os.listdir(hr_media_folder))
    min_audio_to_play = min_media_folder + "/" + random.choice(os.listdir(min_media_folder))
    am_pm_to_play = am_pm_media_folder + "/" + random.choice(os.listdir(am_pm_media_folder))
    if test:
        print(hr_audio_to_play)
        print(min_audio_to_play)
        print(am_pm_to_play)
    audio_player(hr_audio_to_play)
    audio_player(min_audio_to_play)
    audio_player(am_pm_to_play)


if __name__ == "__main__":
    time_handler(12, 30, "pm")
