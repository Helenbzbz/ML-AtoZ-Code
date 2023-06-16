from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

INS_USERNAME = "anna5719lee"
INS_PWD = ""
similar_account = "helenzheng7"
follow_count = 100

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)

        user_name = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        user_name.send_keys(INS_USERNAME)
        password = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
        password.send_keys(INS_PWD, Keys.ENTER)
        time.sleep(4)

    def find_follower(self):
        self.driver.get(f"https://www.instagram.com/{similar_account}/followers")
        time.sleep(10)
             

    def follow(self):
        first_follower = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div/span[1]/span/div/div/div/a/span/div")
        if first_follower.get_attribute("innerText") == INS_USERNAME:
            div_index = "1"
        else:
            div_index = "2"

        for i in range (1, follow_count):
            try:
                follow_button = self.driver.find_element(By.XPATH, f"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[{div_index}]/div/div[{i}]/div/div/div/div[3]/div/button")
            except NoSuchElementException:
                continue
            else:
                try:
                    if follow_button.get_attribute("textContent") == "Follow":
                        follow_button.click()
                except ElementClickInterceptedException:
                    continue

            time.sleep(1)


insfollow = InstaFollower()
insfollow.login()
insfollow.find_follower()
insfollow.follow()