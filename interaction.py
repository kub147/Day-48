from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--disable-search-engine-choice-screen")


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

counter = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
#counter.click()

# szukanie elementu poprzez Link text
all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
#all_portals.click()

# find search - wpisywanie czegos na stronie
search = driver.find_element(By.NAME, 'search')


# wpisuje python i kilkam enter
search.send_keys("Python", Keys.ENTER)



time.sleep(4)
driver.quit()