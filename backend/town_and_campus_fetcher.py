import requests
from constants import TOWN_AND_CAMPUS_URL, TOWN_AND_CAMPUS_PRELUDE, TOWN_AND_CAMPUS_BUFFER, TOWN_AND_CAMPUS_ENDING, TOWN_AND_CAMPUS_SUBDIRECTORY, MEDIA_ROOT_DIRECTORY, PROGRAMMING_SUBDIRECTORY
from bs4 import BeautifulSoup
from gtts import gTTS
import time
import os

# Prerequisites: None
# Description: Pulls town and campus news from kmnr.org and saves an mp3 tts reading
#   of the news
# Returns: 1 if saving the file was a success, 0 if it was not
def town_and_campus_fetcher():
    page=requests.get(TOWN_AND_CAMPUS_URL)
    town_and_campus_text = TOWN_AND_CAMPUS_PRELUDE

    #search for each article's title and text
    soup = BeautifulSoup(page.content, "html.parser")
    title_results = soup.find_all("h2")
    body_results = soup.find_all("div", {"class": "span9"})

    if(len(title_results)==len(body_results)):
        #add each title and article to the text to read
        for i in range(len(title_results)):
            if(i!=0):
                #add separater before all entries but the first
                town_and_campus_text=town_and_campus_text+TOWN_AND_CAMPUS_BUFFER
            #format thearticle as it's added to the text
            town_and_campus_text=town_and_campus_text+(str(title_results[i])[4:-5])+". "+((str(body_results[i])[34:-23]).replace("<br/>",". "))
        town_and_campus_text=town_and_campus_text+TOWN_AND_CAMPUS_ENDING

        filename = "town-and-campus-{}.mp3".format(time.strftime("%Y-%m-%d-%I-%M-%p"))
        try:
            tts = gTTS(town_and_campus_text)
        except:
            print("error: gtts refused the request!")
            return 0
        tts.save(MEDIA_ROOT_DIRECTORY+PROGRAMMING_SUBDIRECTORY+"/"+TOWN_AND_CAMPUS_SUBDIRECTORY+"/"+filename)
        
        for f in os.listdir(MEDIA_ROOT_DIRECTORY+PROGRAMMING_SUBDIRECTORY+"/"+TOWN_AND_CAMPUS_SUBDIRECTORY):
            if f != filename: 
                os.remove(MEDIA_ROOT_DIRECTORY+PROGRAMMING_SUBDIRECTORY+"/"+TOWN_AND_CAMPUS_SUBDIRECTORY+"/"+f)
        
        return(1)
    else:
        print("error: every town and campus news item should have a body and a title!")
        return(0)


if __name__ == '__main__':
    town_and_campus_fetcher()
