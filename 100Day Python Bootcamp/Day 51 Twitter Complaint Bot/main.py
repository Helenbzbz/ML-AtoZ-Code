# Take Away: 1. You can copy XPath directly from broswer
# Take Away: 2. You should copy the path for the button :) Not the text on the button

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 6000
PROMISED_UP = 600
TWITTER_ACCOUNT = "AnnaLee1656639"
TWITTER_PWD = "PWD"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_button.click()
        time.sleep(5)

        download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').get_attribute('textContent')
        upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').get_attribute('textContent')

        while download_speed == "—" or upload_speed == "—":
            download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').get_attribute('textContent')
            upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').get_attribute('textContent')
            
        self.up = float(upload_speed)
        self.down = float(download_speed)
       
    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(3)

        # Log into Twitter
        username = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_ACCOUNT)
        time.sleep(2)
        username.send_keys(Keys.ENTER)
        time.sleep(2)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PWD, Keys.ENTER)
        time.sleep(5)

        # Send Twitter
        message = f'My subscription is UL50 Download {PROMISED_DOWN}Mbps and Upload {PROMISED_UP}Mbps yet my current speed is Download : {self.down}Mbps Upload {self.up}Mbps.'

        twitter_box = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        twitter_box.send_keys(message)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(5)



twitterbot = InternetSpeedTwitterBot()
twitterbot.get_internet_speed()
if PROMISED_DOWN > twitterbot.down or PROMISED_UP > twitterbot.up:
    twitterbot.tweet_at_provider()
twitterbot.driver.close()

