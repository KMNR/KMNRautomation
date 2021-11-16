import requests
from constants import TOWN_AND_CAMPUS_URL, TOWN_AND_CAMPUS_PRELUDE, TOWN_AND_CAMPUS_BUFFER, TOWN_AND_CAMPUS_ENDING, TOWN_AND_CAMPUS_SUBDIRECTORY, MEDIA_ROOT_DIRECTORY
from bs4 import BeautifulSoup
from gtts import gTTS
import time

def town_and_campus_fetcher():
    page=requests.get(TOWN_AND_CAMPUS_URL)
    town_and_campus_text = TOWN_AND_CAMPUS_PRELUDE

    soup = BeautifulSoup(page.content, "html.parser")
    title_results = soup.find_all("h2")
    body_results = soup.find_all("div", {"class": "span9"})
    if(len(title_results)==len(body_results)):
        for i in range(len(title_results)):
            if(i!=0):
                town_and_campus_text=town_and_campus_text+TOWN_AND_CAMPUS_BUFFER
            town_and_campus_text=town_and_campus_text+(str(title_results[i])[4:-5])+". "+((str(body_results[i])[34:-23]).replace("<br/>",". "))
        town_and_campus_text=town_and_campus_text+TOWN_AND_CAMPUS_ENDING

        filename = "/town-and-campus-{}.mp3".format(time.strftime("%Y-%m-%d-%I-%M-%p"))
        tts = gTTS(town_and_campus_text, lang='en')
        tts.save(MEDIA_ROOT_DIRECTORY+"/"+TOWN_AND_CAMPUS_SUBDIRECTORY+filename)
        return(1)
    else:
        print("error: every town and campus news item should have a body and a title!")
        return(0)


if __name__ == '__main__':
    town_and_campus_fetcher()
