import constants
import random
import player
import os

random.seed()
test = True


# Prerequisites: Passing hour, minute as integers. am_pm is either AM or PM as string (case insensitive)
# Description: Chooses a random file from the provided media root directory for hour, minute second
# and passes the absolute file path as an argument to the media handler function.
def time_handler(hour, minute, am_pm):
    if test:
        constants.MEDIA_ROOT_DIRECTORY = "media"
        print(os.listdir(constants.MEDIA_ROOT_DIRECTORY))
    timeis_media_folder = constants.MEDIA_ROOT_DIRECTORY + constants.TIME_SUBDIRECTORY + constants.TIMEIS_SUBDIRECTORY
    hr_media_folder = constants.MEDIA_ROOT_DIRECTORY + constants.TIME_SUBDIRECTORY + constants.HOUR_SUBDIRECTORY + str(hour)
    min_media_folder = constants.MEDIA_ROOT_DIRECTORY + constants.TIME_SUBDIRECTORY + constants.MINUTE_SUBDIRECTORY + str(minute)
    am_pm_media_folder = constants.MEDIA_ROOT_DIRECTORY + constants.TIME_SUBDIRECTORY + constants.AM_PM_SUBDIRECTORY + str(am_pm).lower()
    if test:
        print(timeis_media_folder)
        print(hr_media_folder)
        print(min_media_folder)
        print(am_pm_media_folder)
    timeis_audio_to_play = timeis_media_folder + "/" + random.choice(os.listdir(timeis_media_folder))
    hr_audio_to_play = hr_media_folder + "/" + random.choice(os.listdir(hr_media_folder))
    min_audio_to_play = min_media_folder + "/" + random.choice(os.listdir(min_media_folder))
    am_pm_to_play = am_pm_media_folder + "/" + random.choice(os.listdir(am_pm_media_folder))
    if test:
        print(timeis_audio_to_play)
        print(hr_audio_to_play)
        print(min_audio_to_play)
        print(am_pm_to_play)
    player.play(timeis_audio_to_play)
    player.play(hr_audio_to_play)
    player.play(min_audio_to_play)
    player.play(am_pm_to_play)


if __name__ == "__main__":
    time_handler(12, 30, "pm")
