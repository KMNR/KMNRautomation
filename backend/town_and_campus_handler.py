import os
from constants import MEDIA_ROOT_DIRECTORY, TOWN_AND_CAMPUS_SUBDIRECTORY
from player import play

# Prerequisites: None
# Definition: Finds the most recent town and campus news reading in the town and campus
# Returns:
def town_and_campus_handler():
    town_and_campus_directory = MEDIA_ROOT_DIRECTORY + "/" + TOWN_AND_CAMPUS_SUBDIRECTORY
    articles_in_directory = sorted(os.listdir(town_and_campus_directory), reverse=True)
    if len(articles_in_directory) > 0:
        article_to_play = articles_in_directory[0]
        exit_status = play(town_and_campus_directory+"/"+article_to_play)
        #clean up the directory afterwards
        try:
            for f in os.listdir(town_and_campus_directory):
                os.remove(town_and_campus_directory+"/"+f)
        except e:
            print(e)
        return(exit_status)
    else:
        print("no town and campus news found to play!")
        return(0)

if __name__ == '__main__':
    town_and_campus_handler()
