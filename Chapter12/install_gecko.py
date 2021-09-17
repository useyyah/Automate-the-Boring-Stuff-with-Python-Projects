from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'C:\Users\Ozgur2\Desktop\geckodriver.exe')

driver.get('https://github.com')