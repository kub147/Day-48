from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--disable-search-engine-choice-screen")


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


# price_whole = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
# price_fraction = driver.find_element(By.CLASS_NAME, 'a-price-fraction').text
# print(price_whole, price_fraction)

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# path sctructre

submit = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(submit.text)

# driver.close() # zamyka aktywną
driver.quit() # zapyka całą przeglądarkę