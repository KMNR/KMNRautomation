from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import DJ_KEY
import time

# Prerequisites: Path to playlist folder to log passed to function,
#   this folder must contain a file named "playlist.txt" containing the song info to log
# Description: Logs the playlist at the path provided at klap.kmnr.org
# Returns: None
def music_logging_handler(playlist_path):
    browser = webdriver.Firefox()
    try:
        browser.get('http://klap.kmnr.org/logger/new')
    except:
        print("couldn't open KLAP!")
        browser.quit()
        return

    with open(playlist_path+"/playlist.txt") as f:
        log = f.read()

    #identify everything on the page we need to enter into
    name_box = browser.find_element(By.ID, "id_name")
    show_box = browser.find_element(By.ID, "id_show")
    comment_box = browser.find_element(By.ID, "id_comment")
    key_box = browser.find_element(By.ID, "id_djkey")
    submit_button = browser.find_element(By.XPATH,"//input[@type='submit']")

    #type in the appropriate boxes, and advance to the next page
    name_box.send_keys("DJ Binary Swag")
    show_box.send_keys("Automation")
    comment_box.send_keys("Automation: "+time.strftime("%B %d, %Y (%I:%M %p)"))
    key_box.send_keys(DJ_KEY)
    submit_button.click()

    #switch to spreadsheet entry
    spreadsheet_button = browser.find_element(By.XPATH, "//a[@href='#spreadsheet-add']")
    spreadsheet_button.click()

    #type the song info into the site
    log_box = browser.find_element(By.ID, "playlist-spreadsheet")
    log_box.send_keys(log)

    #upload the song info to klap
    upload_button = browser.find_element(By.XPATH, "//*[contains (text(), 'Upload')]")
    upload_button.click()

    #go back to the page so we can press the commit button
    browser.back()
    browser.refresh()

    commit_button = browser.find_element(By.XPATH, "//*[contains (text(), 'Commit')]")
    commit_button.click()
    browser.quit()

if __name__ == '__main__':
    music_logging_handler("media/playlists/CaleJuic3/")
