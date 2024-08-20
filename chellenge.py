from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--disable-search-engine-choice-screen")


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

name = driver.find_element(By.NAME, 'fName')
name.send_keys('Kuba')

surname = driver.find_element(By.NAME, 'lName')
surname.send_keys('Wilk')

mail = driver.find_element(By.NAME, 'email')
mail.send_keys('kubdhf@gmail.com')


button = driver.find_element(By.CSS_SELECTOR, 'button')
button.click()


time.sleep(4)
driver.quit()