from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

BUMBLE_EMAIL = 'jz107@wellesley.edu'
BUMBLE_PWD = 'PWD'
BUMBLE_PAGE = 'https://bumble.com/get-started'
CLICKS = 10

driver = webdriver.Chrome()
driver.get(BUMBLE_PAGE)
time.sleep(4)

# Switch to consent iframe
driver.switch_to.frame("sp_message_iframe_810475")
continue_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/button")
continue_button.click()
time.sleep(3)

# Continue with Facebook
facebook_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div")
facebook_button.click()
time.sleep(3)

# Facebook Login
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_entry = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
email_entry.send_keys(BUMBLE_EMAIL)
password_entry = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
password_entry.send_keys(BUMBLE_PWD)
time.sleep(5)

submit_buttom = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]')
submit_buttom.click()
time.sleep(10)
driver.switch_to.window(base_window)

count = 0
while count < CLICKS:
    try:
        like = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div')
        like.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/main/div[2]/article/div/footer/div[2]/div[2]/div/span/span/span/span')
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)
    time.sleep(1)