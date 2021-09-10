import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email_username = input("What is your username?\n")
email_password = input("What is your password?\n")
email_recipient = input("Who would you like to send an email to?\n")
email_subject = input("What is the subject of the email?\n")
email_body = input("What would you like to say?\n")

browser = webdriver.Firefox()
browser.maximize_window()
browser.implicitly_wait(30)
browser.get("http://mail.google.com")
login_elem = browser.find_element_by_id("identifierId")
login_elem.send_keys(email_username)
next_elem = browser.find_element_by_id("identifierNext")
next_elem.click()
time.sleep(3)
password_elem = browser.find_element_by_name("password")
password_elem.send_keys(email_password)
pw_next_elem = browser.find_element_by_id("passwordNext")
pw_next_elem.click()
time.sleep()

html_elem = browser.find_element_by_tag_name("html")
html_elem.send_keys("c")
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_recipient)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_subject)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_body)
html_elem.send_keys(Keys.ENTER)

print("Email was sent.")