from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Challenge 1. Python.org
driver.get("https://www.python.org/")
titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

python_org_dict = {
    i:{'time':dates[i].get_attribute("innerText"), 
       'name':titles[i].get_attribute("innerText")}
    for i in range(5)
}
print(python_org_dict)

# Challeneg 2. Wiki Interaction
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount [title=\"Special:Statistics\"]")
article_count.click()
driver.close()

# Challeneg 3. Search website
driver.get("https://en.wikipedia.org/wiki/Main_Page")
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Python", Keys.ENTER)
driver.close()
