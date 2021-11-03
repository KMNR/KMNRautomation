import time
import os
from datetime import datetime
from mutagen.mp3 import MP3
import platform

def play(filePath):
    played=1
    try:
        opSystem = platform.system()
        if opSystem=="Windows":
            played=(os.system("start "+filePath))
        elif opSystem=="Linux":
            played=(os.system("/usr/bin/mpv --no-terminal"+filePath))

        time.sleep(int(MP3(filePath).info.length)+1)
    except:
        print("Couldn't play file!")
    if played == 0:
        print("File played successfully")

if __name__ == "__main__":
    play("backend/non-legal-station-IDs/afterParty.mp3")
