#! /usr/bin/env python

import os
from constants import MEDIA_ROOT_DIRECTORY, WEATHER_SUBDIRECTORY, PROGRAMMING_SUBDIRECTORY
import player

def weather_handler():
    weather_directory = MEDIA_ROOT_DIRECTORY + PROGRAMMING_SUBDIRECTORY + WEATHER_SUBDIRECTORY
    forecasts_in_directory = sorted(os.listdir(weather_directory), reverse=True)
    if len(forecasts_in_directory) > 0:
        forecast_to_play = forecasts_in_directory[0]
        status_code = player.play(weather_directory+forecast_to_play)
        try:
            for f in os.listdir(weather_directory):
                os.remove(weather_directory+f)
        except e:
            print(e)
    else:
        return 1
if __name__ == "__main__":
    weather_handler()
