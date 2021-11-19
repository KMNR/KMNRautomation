from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import KELP_ID, KELP_PW
import org.openqa.selenium.Keys

def programming_logging_handler():
    browser = webdriver.Firefox()
    browser.get('http://kelp.kmnr.org')

    #form.send_keys(Keys.RETURN)

if __name__ == '__main__':
    programming_logging_handler()
