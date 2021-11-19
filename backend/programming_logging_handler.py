from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import KELP_ID, KELP_PW
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def programming_logging_handler():
    browser = webdriver.Firefox()
    browser.get('https://'+KELP_ID+':'+KELP_PW+'@kelp.kmnr.org/show')

    title_box = browser.find_element(By.CLASS_NAME, "typeahead-stationid")
    title_box.send_keys("test1")

    actions = ActionChains(browser)
    actions.send_keys(Keys.TAB+"test2"+Keys.ENTER)
    actions.perform()

    logout_button = browser.find_element(By.XPATH, "//a[@href='/accounts/logout']")
    logout_button.click()

if __name__ == '__main__':
    programming_logging_handler()
