from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver import ActionChains
import random
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

commentsDict = [
'menteri investasi, assalammualaikum @anggawira.id',
] #Add or replace words...

#Selenium Wire configuration to use a proxy
proxy_username = '[your_proxy_username]'
proxy_password = '[your_proxy_password]'
seleniumwire_options = {
    'proxy': {
        'http': f'http://{proxy_username}:{proxy_password}@gw.dataimpulse.com:10001',
        'verify_ssl': False,
    },
}

driver = webdriver.Chrome(
    seleniumwire_options=seleniumwire_options
)

# driver= webdriver.Chrome("/media/patusacyber/Data/RschAde/Master/chromedriver")

# #Apabila tidak menggunakan proxy, gunakan line path ini dan hapus block Selenium Wire
# driver = webdriver.Chrome('chromedriver')


driver.maximize_window()
driver.get("https://www.instagram.com")
sleep(3)

driver.find_element_by_name('username').send_keys('[your_username]') #replace with your insta username
sleep(1)
driver.find_element_by_name('password').send_keys('[your_password]') #replace with your insta password
sleep(2)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(6)
driver.get('[your_post_target_url]') #change the url 

sleep(4)
# post_click=driver.find_element_by_class_name("_aagw").click() #click on first post 
# sleep(3)
#like=driver.find_element_by_class_name("xp7jhwk").click() #click on like button
sleep(4)
driver.find_element(By.XPATH, "//textarea[@aria-label='Add a comment…']").click()
sleep(2)
driver.find_element(By.XPATH, "//textarea[@aria-label='Add a comment…']").send_keys(random.choice(commentsDict)) #send the text in comment section
sleep(5)
driver.find_element(By.XPATH, "//textarea[@aria-label='Add a comment…']").click() #click on comment section area
sleep(5)
driver.find_element(By.XPATH, "//textarea[@aria-label='Add a comment…']").send_keys(Keys.ENTER) #send the text in comment section
sleep(5)
