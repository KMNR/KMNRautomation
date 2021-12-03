import time
import os
from datetime import datetime
from mutagen.mp3 import MP3


def play(filePath):
    played = 1
    try:
        played = (os.system("start " + filePath))
        time.sleep(int(MP3(filePath).info.length))
    except:
        print("Couldn't play file!")
    if played is 0:
        print("File played successfully")


if __name__ == "__main__":
    play("backend/non-legal-station-IDs/afterParty.mp3")
