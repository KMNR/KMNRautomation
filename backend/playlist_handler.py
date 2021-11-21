import os
import constants
import player

# Prerequisites: Passing the path to the playlist folder as a string, and the index
# of the next song to be played as an integer
# Description: Plays the song with the passed index from the passed playlist directory.
# If the file with the index passed has an ignored file extension, the file will
# be skipped and nothing will be played.
# Return: The index of the next song to be played, or -1 if the playlist is over
def playlist_handler(folderPath, songNum):
    songList=os.listdir(folderPath)
    if songNum>=len(songList):
        return -1
    else:
        if(any(element in songList[songNum] for element in constants.IGNORED_FILE_EXTENSIONS)):
            songNum+=1
            if songNum>=len(songList):
                return -1

        songPath=str(folderPath+"/"+songList[songNum])
        player.play(songPath)
        #return the number of the next song to be played
        return (songNum+1)

if __name__ == "__main__":
    currSong=0
    while(currSong>=0):
        currSong=playlist_handler("media/playlists/GogoJuic3",currSong)
