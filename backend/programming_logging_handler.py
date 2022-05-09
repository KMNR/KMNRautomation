from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from constants import KELP_ID, KELP_PW, LEGAL_STATION_ID_SUBDIRECTORY, PROFILE_AMERICA_SUBDIRECTORY, NEWS_AND_WEATHER_ID, TOWN_AND_CAMPUS_SUBDIRECTORY, CONCERT_NEWS_SUBDIRECTORY
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from mutagen.mp3 import MP3

# Prerequisites: name of file to log passed as string, or None if the log will be
#   generic. path of file to log passed as string, or None if the log will be generic.
#   Type of programming passed as string
# Description: Logs the programming of the type specified using kelp.kmnr.org.
#   If appropriate, uses the name of the file to log the programming
# Returns: None
def programming_logging_handler(filename,filepath,programming_type):
    box_id=""
    log_text=""
    programming_len=0

    #choose which box to fill in and what to put in it depending on which type of programming
    if programming_type==LEGAL_STATION_ID_SUBDIRECTORY:
        box_id="typeahead-stationid"
        log_text="Station ID"
    elif programming_type=="PSA":
        box_id="typeahead-psa"
        #remove the extension when logging to KELP
        log_text=filename[:-4]
    elif programming_type==PROFILE_AMERICA_SUBDIRECTORY:
        box_id="typeahead-profileamerica-censusbureau"
        log_text="Profile America"
    elif programming_type=="ascertainment":
        box_id="typeahead-ascertainment"
        log_text=filename[:-4]
    elif programming_type=="ad-council":
        box_id="typeahead-adcouncil"
        log_text=filename[:-4]
    elif programming_type==TOWN_AND_CAMPUS_SUBDIRECTORY:
        box_id="typeahead-townandcampus"
        log_text="Town And Campus News"
    elif programming_type=="earth-date":
        box_id="typeahead-earthdate"
        log_text=filename[:-4]
    elif programming_type==NEWS_AND_WEATHER_ID:
        box_id="news&weather"
        log_text="News & Weather"
    elif programming_type=="science-and-the-sea":
        box_id="typeahead-scienceandthesea"
        log_text=filename[:-4]
    elif programming_type==CONCERT_NEWS_SUBDIRECTORY:
        box_id="typeahead-concertnews"
        log_text="Concert News"
    else:
        print("Couldn't find that type of programming to log!")
        return(0)

    #if we don't know how long the file is, just write the length as 45 second (the average length of news & weather) 
    if filepath==None:
        programming_len=45
    else:
        programming_len=MP3(filepath).info.length

    opts=FirefoxOptions()
    opts.add_argument("--headless")
    browser = webdriver.Firefox(firefox_options=opts)
    
    try:
        browser.get('https://'+KELP_ID+':'+KELP_PW+'@kelp.kmnr.org/show')
    except:
        print("couldn't log in to KELP!")
        browser.quit()
        return
    #find the appropriate box to type into
    #news&weather is a special case because of the ampersand
    if box_id=="news&weather":
        title_box = browser.find_element(By.XPATH, "//*[contains (text(), 'Weather')]")
        title_box.click()
    else:
        title_box = browser.find_element(By.CLASS_NAME, box_id)
        title_box.send_keys(log_text)

    #convert length of the file to minutes and seconds for readability
    len_min=int(programming_len/60)
    len_sec=int(programming_len%60)

    actions = ActionChains(browser)
    if box_id=="news&weather":
        actions.send_keys(Keys.TAB+"News & Weather")
    if len_sec<10:
        len_sec="0"+str(len_sec)
        #actions.send_keys(Keys.TAB+str(0)+Keys.ENTER)
    actions.send_keys(Keys.TAB+str(len_min)+":"+str(len_sec)+Keys.ENTER)
    actions.perform()

    logout_button = browser.find_element(By.XPATH, "//a[@href='/accounts/logout/']")
    logout_button.click()
    browser.quit()

    return(1)

if __name__ == '__main__':
    programming_logging_handler(None,None,"news-and-weather")
