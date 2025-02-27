from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('/media/patusacyber/Data/RschAde/Master/chromedriver')  # Change this path to your webdriver's location

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        username_input = self.driver.find_element(By.NAME, "username")  
        password_input = self.driver.find_element(By.NAME, "password")  
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(4)

    def comment_on_post(self, post_url, comment_text):
        self.driver.get(post_url)
        time.sleep(2)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class ="_aaof _aiam"]//textarea'))
#                (By.XPATH,'//*[@class ="_aaof _aiam"]//textarea').click()
            ).send_keys(comment_text + Keys.ENTER)
            time.sleep(2)
        except Exception as e:
            print("Failed to comment:", e)

    def close(self):
        self.driver.quit()

# Example usage:
if __name__ == "__main__":
    username = [your_username]
    password = [your_password]
    post_url = [your_target_url]
    comment_text = [your_comment]

    bot = InstagramBot(username, password)
    bot.login()
    bot.comment_on_post(post_url, comment_text)
    bot.close()
