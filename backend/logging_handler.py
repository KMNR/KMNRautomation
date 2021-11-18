from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import DJ_KEY
import time

def logging_handler():
    browser = webdriver.Firefox()
    type(browser)
    browser.get('http://klap.kmnr.org/logger/new')
    name_box = browser.find_element(By.ID, "id_name")
    show_box = browser.find_element(By.ID, "id_show")
    comment_box = browser.find_element(By.ID, "id_comment")
    key_box = browser.find_element(By.ID, "id_djkey")
    #fix this
    #submit_button = browser.find_element(By.Value, "Start Log")

    name_box.send_keys("DJ Binary Swag")
    show_box.send_keys("Automation")
    comment_box.send_keys(time.strftime("%Y-%m-%d-%I-%M-%p"))
    key_box.send_keys(DJ_KEY)

    #submit_button.click()

if __name__ == '__main__':
    logging_handler()
