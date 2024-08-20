import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from threading import Timer

# Setting up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--disable-search-engine-choice-screen")

# Initializing the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Locating the cookie element
cookie = driver.find_element(By.ID, 'cookie')

# Extracting product elements and storing their names and prices in a dictionary
shop = {}
product_elements = driver.find_elements(By.CSS_SELECTOR, value=".grayed b")

for i, product in enumerate(product_elements):
    split_text = product.text.split('-')
    if len(split_text) == 2:
        name = split_text[0].strip()
        price = int(split_text[1].strip().replace(',', ''))  # Remove commas and convert to int
        shop[i] = {
            'name': name,
            'price': price
        }
    else:
        print(f"Skipping product due to unexpected format: {product.text}")

print(shop)


# Function to continuously click the cookie
def click_cookie_continuously():
    while True:
        cookie.click()


# Function to check what to buy every 5 seconds
def checking_what_to_buy():
    # Retrieve the current money amount
    money_element = driver.find_element(By.XPATH, '//*[@id="money"]')
    money = int(money_element.text.replace(',', ''))  # Remove commas and convert to int

    # Determine the most expensive item you can afford
    affordable_items = {k: v for k, v in shop.items() if v['price'] <= money}

    if affordable_items:
        most_expensive_item = max(affordable_items.items(), key=lambda x: x[1]['price'])
        print(f"Buying: {most_expensive_item[1]['name']} for {most_expensive_item[1]['price']}")

        # Locate and click the corresponding shop item
        shop_item = driver.find_element(By.ID, f"buy{most_expensive_item[1]['name']}")
        shop_item.click()
    else:
        print("Not enough money to buy anything.")

    # Re-run the check after 25 seconds
    Timer(25, checking_what_to_buy).start()


# Start continuous cookie clicking in a separate thread
import threading

clicking_thread = threading.Thread(target=click_cookie_continuously)
clicking_thread.start()

# Start the checking function
checking_what_to_buy()

# Let the script run for a desired amount of time, e.g., 5 minutes
time.sleep(300)  # 300 seconds = 5 minutes

# After 5 minutes, stop the script
driver.quit()
