from enum import Enum, unique

MEDIA_ROOT_DIRECTORY = "/this/is/the/media/directory/"
BACKEND_ROOT_DIRECTORY = "backend/"
TIME_SUBDIRECTORY = "/time"
PLAYLISTS_SUBDIRECTORY = "/playlists"
TIMEIS_SUBDIRECTORY = "/timeis/"
HOUR_SUBDIRECTORY = "/hours/"
MINUTE_SUBDIRECTORY = "/minutes/"
AM_PM_SUBDIRECTORY = "/ampm/"
LEGAL_STATION_ID_SUBDIRECTORY = "/legalstationid/"
NONLEGAL_STATION_ID_SUBDIRECTORY = "/nonlegalstationid/"
PROGRAMMING_SUBDIRECTORY = "/programming/"
IGNORED_FILE_EXTENSIONS = (".txt", ".cfg", ".config")
MP3_SEGS = ("PSA","ad-council","profile-america","ascertainment","earth-date","science-and-the-sea")
TTS_SEGS = ("town-and-campus","news-and-weather","concert-news")
WEATHER_SUBDIRECTORY = "/weather/"
IGNORED_FILE_EXTENSIONS = (".txt", ".cfg", ".config")
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=imperial&appid={}"

WEATHER_SCRIPT = "Now for today's weather. The high today is {} degrees, and the low is {}. I would best describe" \
                 " the forecast as {}. Currently, it is {} degrees, and it feels like {}. The humidity is {}" \
                 " percent, and I would say the current conditions are {}."


@unique
class ConstantStrings(Enum):
    PLAYING_TOP_HOUR = "Playing top of the hour ID"
    PLAYING_20_MINS = "Playing 20 mins past ID"
    PLAYING_40_MINS = "Playing 40 mins past ID"
    PLAYING_EDU_SEGMENT = "Playing educational segment"
    PLAYING_SONG = "Playing song"

    def __str__(self):
        return self.value
