from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import DJ_KEY
import time

def music_logging_handler(playlist_path):
    browser = webdriver.Firefox()
    type(browser)
    browser.get('http://klap.kmnr.org/logger/new')
    with open(playlist_path+"/playlist.txt") as f:
        log = f.read()

    name_box = browser.find_element(By.ID, "id_name")
    show_box = browser.find_element(By.ID, "id_show")
    comment_box = browser.find_element(By.ID, "id_comment")
    key_box = browser.find_element(By.ID, "id_djkey")
    #fix this
    submit_button = browser.find_element(By.XPATH,"//input[@type='submit']")

    name_box.send_keys("DJ Binary Swag")
    show_box.send_keys("Automation")
    comment_box.send_keys("Automation: "+time.strftime("%B %d, %Y (%I:%M %p)"))
    key_box.send_keys(DJ_KEY)
    submit_button.click()

    spreadsheet_button = browser.find_element(By.XPATH, "//a[@href='#spreadsheet-add']")
    spreadsheet_button.click()

    log_box = browser.find_element(By.ID, "playlist-spreadsheet")
    log_box.send_keys(log)

    upload_button = browser.find_element(By.XPATH, "//*[contains (text(), 'Upload')]")
    upload_button.click()

    browser.back()
    browser.refresh()

    commit_button = browser.find_element(By.XPATH, "//*[contains (text(), 'Commit')]")

    #uncomment these lines to make it actually log
    #commit_button.click()
    #browser.quit()

if __name__ == '__main__':
    music_logging_handler("media/playlists/CaleJuic3/")
