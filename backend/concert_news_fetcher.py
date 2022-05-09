import time
import os
import constants
from gtts import gTTS

def concert_news_fetcher():
    f = open(constants.BACKEND_ROOT_DIRECTORY+"ConcertNews.txt")
    concert_news_text = f.read()
    tts = gTTS(concert_news_text, lang='en')
    tts.save(constants.MEDIA_ROOT_DIRECTORY+constants.PROGRAMMING_SUBDIRECTORY+constants.CONCERT_NEWS_SUBDIRECTORY+"/concert_news.mp3")
    return(0)

if __name__ == "__main__":
    concert_news_fetcher()
