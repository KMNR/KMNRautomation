import time
import os
from datetime import datetime
from mutagen.mp3 import MP3

def player(filePath):
    os.system("start "+filePath)
    time.sleep(int(MP3(filePath).info.length))
