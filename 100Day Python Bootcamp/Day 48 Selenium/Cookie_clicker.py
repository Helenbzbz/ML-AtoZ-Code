from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_element = driver.find_element(By.ID, "cookie")
loop_time = 2

def click():
    start_time = time.time()
    while time.time()-start_time < loop_time:
        cookie_element.click()

def purchase_equipments():
    purchse_items = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.grayed)")
    purchse_items[-1].click()
    
game_on = True

while game_on:
    click()
    purchase_equipments()
