import os
import constants
import player

def playlist_handler(folderPath, songNum):
    if songNum==0:
        #call the music logging function with the whole playlist when the first song is played
        pass
    songList=os.listdir(folderPath)
    if songNum>=len(songList):
        #return of -1 means playlist is finished
        return -1
    else:
        if(any(element in songList[songNum] for element in constants.IGNORED_FILE_EXTENSIONS)):
            #don't attempt to play non-audio files
            pass
        else:
            songPath=str(folderPath+"/"+songList[songNum])
            player.play(songPath)
        #return the number of the next song to be played
        return (songNum+1)

if __name__ == "__main__":
    currSong=0
    while(currSong>=0):
        currSong=playlist_handler("media/playlists/CaleJuic3",currSong)
