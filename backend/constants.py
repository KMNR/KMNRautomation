from enum import Enum, unique

MEDIA_ROOT_DIRECTORY = "/home/kmnr/automation-rework/media"
BACKEND_ROOT_DIRECTORY = "/home/kmnr/automation-rework/backend/"
CONFIG_FILE_PATH = "/home/kmnr/automation-rework/backend/settings.ini"
TIME_SUBDIRECTORY = "/time"
PLAYLISTS_SUBDIRECTORY = "/playlists"
TIMEIS_SUBDIRECTORY = "/timeis"
HOUR_SUBDIRECTORY = "/hours/"
MINUTE_SUBDIRECTORY = "/minutes/"
AM_PM_SUBDIRECTORY = "/ampm/"
AT_NIGHT_SUBDIRECTORY = "/at_night/"
WEATHER_SUBDIRECTORY = "/weather/"
NEWS_SUBDIRECTORY = "/news/"
LEGAL_STATION_ID_SUBDIRECTORY = "/legalstationid/"
NONLEGAL_STATION_ID_SUBDIRECTORY = "/nonlegalstationid/"
PROGRAMMING_SUBDIRECTORY = "/programming/"
MP3_SEGS = ("PSA","ad-council","profile-america","ascertainment","earth-date","science-and-the-sea")
TTS_SEGS = ("town-and-campus","news-and-weather","concert-news")
ADDITIONAL_SUBDIRECTORY_SEGS = ("ad-council")
PROFILE_AMERICA_SUBDIRECTORY = "profile-america"
NEWS_AND_WEATHER_ID = "news-and-weather"
TOWN_AND_CAMPUS_SUBDIRECTORY = "town-and-campus"
CONCERT_NEWS_SUBDIRECTORY = "concert-news"
PROGRAMMING_SCHEDULE_PATH = "daily_programming_schedule.txt"
LOGGING_STATUS_PATH = "logging.txt"
IGNORED_FILE_EXTENSIONS = (".txt", ".cfg", ".config")
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=imperial&appid={}"

WEATHER_SCRIPT = "Now for today's weather. The high today is {} degrees, and the low is {}. I would best describe" \
                 " the forecast as {}. Currently, it is {} degrees, and it feels like {}. The humidity is {}" \
                 " percent, and I would say the current conditions are {}."

NEWS_SCRIPT = "Here's one of the top stories for today: {}." \
              "The full story can be read at {}."

BLOCKED_NEWS_KEYWORDS = ("sex","suicide","assault","gun","body","weapon")
BLOCKED_NEWS_SOURCES = ("YouTube","The Verge","Breitbart News","CNN Spanish","Crypto Coins News","Reddit /r/all")

TOWN_AND_CAMPUS_URL = "https://kmnr.org/townandcampus"
TOWN_AND_CAMPUS_PRELUDE = "Town & Campus News: "
TOWN_AND_CAMPUS_BUFFER = ". The next event is: "
TOWN_AND_CAMPUS_ENDING = ". Town & Campus News is read five times daily on the air, and is also available on our webpage (kmnr.org). Organizations may submit announcements to be read by filling out our online forms."

DJ_KEY = "c6a4a5ae"
KELP_ID = "djbs"
KELP_PW = "snap1man"


# Email Configuration
EMAIL_TO_SEND_FROM = "kmnrtesting@gmail.com"
EMAIL_TO_SEND_FROM_PASS = "MichaelGosnell"
ALERT_RECIPIENTS = ["anotheremail@example.com","realemail@example.com"]
ALERT_MESSAGE = "KUMM crash detected. Supervisor crash log below.\n\n{}"
@unique
class ConstantStrings(Enum):
    PLAYING_TOP_HOUR = "Playing top of the hour ID"
    PLAYING_20_MINS = "Playing 20 mins past ID"
    PLAYING_40_MINS = "Playing 40 mins past ID"
    PLAYING_EDU_SEGMENT = "Playing educational segment"
    PLAYING_SONG = "Playing song"

    def __str__(self):
        return self.value
