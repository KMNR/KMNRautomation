from enum import Enum, unique

MEDIA_ROOT_DIRECTORY = "/this/is/the/media/directory"
TIME_SUBDIRECTORY = "/time"
PLAYLISTS_SUBDIRECTORY = "/playlists"
HOUR_SUBDIRECTORY = "/hours/"
MINUTE_SUBDIRECTORY = "/minutes/"
AM_PM_SUBDIRECTORY = "/ampm/"
IGNORED_FILE_EXTENSIONS = (".txt", ".cfg", ".config")


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
