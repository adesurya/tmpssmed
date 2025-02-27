from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



import time
import random

commentsDict = [
'your_comment_here',
'your_comment_here'
                ] #replace with your words


# Selenium Wire configuration to use a proxy
proxy_username = '[proxy_username]'
proxy_password = '[proxy_passwd]]'
seleniumwire_options = {
    'proxy': {
        'http': f'http://{proxy_username}:{proxy_password}@[host]:[port]',
        'verify_ssl': False,
    },
}

#first account

driver = webdriver.Chrome(
    seleniumwire_options=seleniumwire_options
)

driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(7)
email = driver.find_element_by_name('text')
email.send_keys("[your_username]]") #replace with your valid twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("[your_password]") #replace with your valid twitter password
password.send_keys(Keys.ENTER)
time.sleep(5)


counter = 0
while True:
    try:
        
        # Post the tweet
        send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        send_button.send_keys(random.choice(commentsDict))
        
        time.sleep(1)

        # Click the post button
        driver.execute_script('document.querySelector("#react-root > div > div > div.css-175oi2r.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div.css-175oi2r.r-14lw9ot.r-jxzhtn.r-13l2t4g.r-1ljd8xs.r-1phboty.r-16y2uox.r-184en5c.r-61z16t.r-11wrixw.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div > div.css-175oi2r.r-14lw9ot.r-184en5c > div > div.css-175oi2r.r-14lw9ot.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-175oi2r.r-14lw9ot.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div > div.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19u6a5r.r-2yi16.r-1qi8awa.r-ymttw5.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l > div > span > span").click()')

        time.sleep(2)  

           
        counter += 1
        if counter == 1: #Change '5' to 'how many auto tweet for a acc....
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(2)
driver.close()
