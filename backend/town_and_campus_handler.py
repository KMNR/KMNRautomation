import os
from constants import MEDIA_ROOT_DIRECTORY, TOWN_AND_CAMPUS_SUBDIRECTORY, PROGRAMMING_SUBDIRECTORY
from player import play

# Prerequisites: None
# Definition: Finds the most recent town and campus news reading in the town and campus
# Returns: 1 if the news was played successfully, 0 if it was not
def town_and_campus_handler():
    town_and_campus_directory = MEDIA_ROOT_DIRECTORY + PROGRAMMING_SUBDIRECTORY + "/" + TOWN_AND_CAMPUS_SUBDIRECTORY
    articles_in_directory = sorted(os.listdir(town_and_campus_directory), reverse=True)
    if len(articles_in_directory) > 0:
        article_to_play = articles_in_directory[0]
        exit_status = play(town_and_campus_directory+"/"+article_to_play)
        #clean up the directory afterwards
        '''
        try:
            for f in os.listdir(town_and_campus_directory):
                os.remove(town_and_campus_directory+"/"+f)
        except:
            print("Error removing old town and campus news mp3 files")
        '''
        return(exit_status)
    else:
        print("no town and campus news found to play!")
        return(0)

if __name__ == '__main__':
    town_and_campus_handler()
