import configparser
import constants
from gtts import gTTS
from newsapi import NewsApiClient
import time

# Prerequisites: None
# Description: Fetches a news article from NewsAPI and saves a reading of it as an mp3 file in the appropriate folder
# Returns: None
def news_fetcher():
    foundArticle = False
    articleNum=0
    cfg = configparser.ConfigParser()
    cfg.read(constants.CONFIG_FILE_PATH)
    api_key = cfg["News"]["news_api_key"]

    #call the api for the top English United States stories
    newsapi = NewsApiClient(api_key=api_key)
    top_headlines = newsapi.get_top_headlines(language="en",country="us")

    while not foundArticle:
        #make sure the article doesn't contain any blacklisted keywords,
        #is not from a blacklisted source, and has a body
        if not ((any(content in str(top_headlines['articles'][articleNum]['content']) for content in constants.BLOCKED_NEWS_KEYWORDS))
            or (any(source in str(top_headlines['articles'][articleNum]['source']['name']) for source in constants.BLOCKED_NEWS_SOURCES))
            or (top_headlines['articles'][articleNum]['content'])==None):
                foundArticle=True
        else:
            articleNum=articleNum+1

    #clean up the text of the article
    article_text = top_headlines['articles'][articleNum]['title']+"."+top_headlines['articles'][articleNum]['content']
    split_string = article_text.split("[",1)
    article_text = split_string[0]
    article_source = top_headlines['articles'][articleNum]['source']['name']
    script = constants.NEWS_SCRIPT.format(article_text,article_source)

    try:
        tts = gTTS(script, lang='en')
    except:
        print("error: gtts refused the request!")
        return

    filename = "news-{}.mp3".format(time.strftime("%Y-%m-%d-%I-%M-%p"))
    tts.save(constants.MEDIA_ROOT_DIRECTORY+constants.PROGRAMMING_SUBDIRECTORY+constants.NEWS_SUBDIRECTORY+filename)

    print("added news article titled: ",top_headlines['articles'][articleNum]['title'],
        " from source: ",top_headlines['articles'][articleNum]['source']['name'])

if __name__ == "__main__":
    news_fetcher()
