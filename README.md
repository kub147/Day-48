Cookie Clicker Bot
This Python script automates the "Cookie Clicker" game using Selenium. The bot continuously clicks the cookie while simultaneously checking every 5 seconds to see which upgrades or items can be purchased. It then buys the most expensive item that the player can afford.

Features
Continuous Cookie Clicking: The bot runs an infinite loop to continuously click the main cookie, maximizing the cookie count.
Automated Purchases: Every 5 seconds, the bot checks how much money (cookies) you have and determines which item from the shop you can afford. It automatically buys the most expensive item available to optimize your progression.
Multi-threading: The clicking and purchasing processes run in parallel using Python's threading module, ensuring smooth and efficient gameplay automation.

Requirements
Python 3.x
Selenium
ChromeDriver

How to Run
Clone this repository to your local machine.
Ensure that ChromeDriver is installed and available in your PATH.

Customization
Clicking Duration: The script is currently set to run for 5 minutes. You can adjust the duration by changing the time.sleep(300) value in the script.
Item Purchase Logic: The bot buys the most expensive item you can afford every 5 seconds. This logic can be modified to prioritize different strategies based on your preferences.
Disclaimer
This script is intended for educational purposes and should be used responsibly. Automating games may violate their terms of service, so use this bot at your own risk.
