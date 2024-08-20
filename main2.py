from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--disable-search-engine-choice-screen")


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

events = {}
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

for i in range(len(event_names)):
    events[i] = {
        'time': event_times[i].text,
        'name': event_names[i].text
    }

print(events)

driver.quit()