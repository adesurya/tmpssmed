from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random


commentsDict = ['your_comment_here',
                'your_comment_here']

# Set up Chrome WebDriver (make sure you have ChromeDriver installed and in your PATH)
driver = webdriver.Chrome()

# Navigate to Facebook
driver.get("https://www.facebook.com/")

# Enter your email/phone and password
email_input = driver.find_element_by_id("email")
email_input.send_keys('[your_username]')
password_input = driver.find_element_by_id("pass")
password_input.send_keys('[your_pass]')
password_input.send_keys(Keys.RETURN)

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.title_contains("Facebook"))

# Navigate to the Facebook page where you want to comment
driver.get("[your_facebook_page]")

sleep(5)

# Switch to the main content frame (if any)
driver.switch_to.default_content()

# Find the comment input field by XPath and type your comment
comment_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'notranslate')]")))
comment_box.click()
# comment_box.send_keys("Your comment here")
comment_box.send_keys(random.choice(commentsDict))

# Find and click the post button by ID
try:
    post_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "focused-state-composer-submit")))
    post_button.click()
    print("Comment posted successfully!")
except:
    print("Failed to find and click the post button.")

sleep(5)

# Close the browser
driver.quit()