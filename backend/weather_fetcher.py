import requests
import configparser
from constants import WEATHER_API_URL, WEATHER_SCRIPT


def main():
    cfg = configparser.ConfigParser()
    cfg.read("settings.ini")
    api_key = cfg["Weather"]["owm_api_key"]
    lat = cfg["Weather"]["lat"]
    long = cfg["Weather"]["long"]
    url = WEATHER_API_URL.format(lat, long, api_key)
    response = requests.get(url)
    if response.status_code != 200:
        print(response)
        exit(1)
    else:
        # Good return code, now we process the info
        json_resp = response.json()
        # First, we process today's weather forecast
        # Converts to a float, then rounds to nearest int, then casts as int for later use
        # Yes, we do have to do it like this
        todays_min = int(round(float(json_resp["daily"][0]["temp"]["min"])))
        todays_max = int(round(float(json_resp["daily"][0]["temp"]["max"])))
        todays_forecast = json_resp["daily"][0]["weather"][0]["description"]
        # Current weather
        current_temp = int(round(float(json_resp["current"]["temp"])))
        feels_like = int(round(float(json_resp["current"]["feels_like"])))
        current_humidity = int(round(float(json_resp["current"]["humidity"])))
        current_weather_description = json_resp["current"]["weather"][0]["description"]

        # Generate weather forecast script
        script = WEATHER_SCRIPT.format(todays_max, todays_min, todays_forecast, current_temp, feels_like
                                       , current_humidity, current_weather_description)
        print(script)
        # TODO: Generate TTS file


if __name__ == "__main__":
    main()
