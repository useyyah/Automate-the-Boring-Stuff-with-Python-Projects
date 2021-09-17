from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
browser.maximize_window()

html_elem = browser.find_element_by_tag_name('html')

while True:
    key = random.randint(1, 4)
    if key == 1:
        html_elem.send_keys(Keys.UP)
    elif key == 2:
        html_elem.send_keys(Keys.DOWN)
    elif key == 3:
        html_elem.send_keys(Keys.RIGHT)
    elif key == 4:
        html_elem.send_keys(Keys.LEFT)

    try:
        retry_elem = browser.find_element_by_class_name('retry-button')
        retry_elem.click()
        continue
    except:
        continue