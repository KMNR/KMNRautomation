import time
import os
from datetime import datetime
from mutagen.mp3 import MP3
import platform
import soundfile as sf
import pathlib

test=True

# Prerequisites: Passing file path of a valid mp3 or other audio file as a string
# Description: Uses the OS's native media player to play the audio file at the passed path
# Return: 0 if the file failed to play, 1 if the file played without issue
# Call function in other files using player.play(filePath)
def play(filePath):
    played=1
    if test:
        print("Playing "+filePath)
    try:
        opSystem = platform.system()
        if opSystem=="Windows":
            played=(os.system("start "+filePath))
        elif opSystem=="Linux":
            played=(os.system("/usr/bin/mpv --no-terminal"+filePath))

        #sleep can be removed for testing purposes if we don't want to wait for entire files to play
        #we have to get the length differently depending on the file type
        if(pathlib.Path(filePath).suffix==".mp3"):
            time.sleep(int(MP3(filePath).info.length)+2)
        else:
            f=sf.SoundFile(filePath)
            time.sleep(int((f.frames)/(f.samplerate)+2))

    except:
        print("Couldn't play file!")
        return(0)
    if played == 0:
        print("File played successfully")
        return(1)

if __name__ == "__main__":
    play("media/legalstationid/PewPewRadioSweeperID2.mp3")
