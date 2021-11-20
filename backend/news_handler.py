import os
from constants import MEDIA_ROOT_DIRECTORY, NEWS_SUBDIRECTORY, PROGRAMMING_SUBDIRECTORY
import player

# Prerequisites: None
# Definition: Finds the most recent news article in the news directory and plays it using the media player
# Returns: 1 if reading the story was successful, 2 if it was not
def news_handler():
    news_directory = MEDIA_ROOT_DIRECTORY + PROGRAMMING_SUBDIRECTORY+ NEWS_SUBDIRECTORY
    articles_in_directory = sorted(os.listdir(news_directory), reverse=True)
    if len(articles_in_directory) > 0:
        article_to_play = articles_in_directory[0]
        exit_status=player.play(news_directory+article_to_play)
        #clean up the directory afterwards
        try:
            for f in os.listdir(news_directory):
                os.remove(news_directory+f)
        except e:
            print(e)
        return(exit_status)
    else:
        print("no news articles found to play!")
        return(0)

if __name__ == "__main__":
    news_handler()
