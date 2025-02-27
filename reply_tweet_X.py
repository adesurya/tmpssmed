from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


commentsDict = [
'[your_tweet_url]'
]

# Set up Chrome WebDriver (make sure you have ChromeDriver installed and in your PATH)
driver = webdriver.Chrome()

# Your Twitter credentials
username = "[your_username]"
password = "[your_password]"

# Tweet URL to reply to
tweet_url = "[your_tweet_url]"

# Reply message
reply_message = random.choice(commentsDict)

# Open Twitter login page
driver.get("https://twitter.com/i/flow/login")
sleep(7)

email = driver.find_element_by_name('text')
email.send_keys("[your_twitter_username]") #replace with your valid twitter username
email.send_keys(Keys.ENTER)
sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("[your_twitter_password]") #replace with your valid twitter password
password.send_keys(Keys.ENTER)
sleep(5)

# Open the tweet to reply to
driver.get(tweet_url)
sleep(3)

# Click on the reply button
reply_button = driver.find_element_by_xpath("//div[@aria-label='Post text']")
reply_button.click()
sleep(2)

# Type the reply message
reply_textarea = driver.find_element_by_xpath("//div[@data-testid='tweetTextarea_0']")
reply_textarea.send_keys(reply_message)
sleep(2)

# Click on the tweet button to send the reply
tweet_button = driver.find_element_by_xpath("//div[@data-testid='tweetButtonInline']")
tweet_button.click()
sleep(2)

# Close the browser
driver.quit()
