import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

question_link = "https://docs.google.com/forms/d/e/1FAIpQLSdXxPaiXwCql8_kiR9IR6gv9iQvoJt6-FmklvXNI1PAueFVSA/viewform?usp=sf_link"
zillow_link = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

# 1. Obtain information from Zillow
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
zillow_content = requests.get(zillow_link, headers=header)
souped_zillow = BeautifulSoup(zillow_content.text, 'html.parser')

# 1.a Find all links
property_link_card = souped_zillow.find_all("a", attrs = {"data-test": "property-card-link"})
property_links = [f"https://www.zillow.com/{property_link_card[i].get('href')}" for i in range(0, len(property_link_card), 2)]

# 1.b Find all rents
property_rents_card = souped_zillow.find_all("span", attrs = {"data-test": "property-card-price"})
property_rents = [card.text.split(" ")[0] for card in property_rents_card]

# 1.c Find all addresses
property_address_card = souped_zillow.find_all("address")
property_addresses= [card.text.split("|")[-1] for card in property_address_card]


# 2. Fill in form and submit
driver = webdriver.Chrome()

for i in range(len(property_links)):
    driver.get(question_link)
    time.sleep(3)

    address_box = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_box.send_keys(property_addresses[i])
    rents_box = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rents_box.send_keys(property_rents[i])
    link_box = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_box.send_keys(property_links[i])
    time.sleep(2)

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]//div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    time.sleep(2)
