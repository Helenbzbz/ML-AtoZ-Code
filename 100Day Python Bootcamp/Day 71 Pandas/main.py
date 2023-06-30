from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import pandas as pd

# # Open the page
# web_driver = webdriver.Chrome()
# web_endpoint = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
# web_driver.get(web_endpoint)

# # Start CSV and define headers
# file = open('100Day Python Bootcamp/Day 71 Pandas/major.csv', 'w', newline='')
# writer = csv.writer(file)
# writer.writerow(['Rank', 'Major','Degree Type','Early Career Pay','Mid Career Pay', '% High Meaning'])

# # Find major data
# def add_page_value():
#     major_data_rows = web_driver.find_elements(By.CLASS_NAME, "data-table__row")
#     for row in major_data_rows:
#         new_row = [value.get_attribute("innerText") for value in row.find_elements(By.CLASS_NAME, "data-table__value")]
#         writer.writerow(new_row)

# time.sleep(4)
# add_page_value()

# for i in range(2, 35):
#     web_driver.get(web_endpoint+f'/page/{i}')
#     time.sleep(3)
#     add_page_value()
#     time.sleep(3)

# web_driver.close()
# file.close()

major_data = pd.read_csv("100Day Python Bootcamp/Day 71 Pandas/major.csv")
print(major_data.sort_values("Early Career Pay").head())