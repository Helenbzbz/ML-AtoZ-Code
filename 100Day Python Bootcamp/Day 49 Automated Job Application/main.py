from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

LinkedIn_Link = "https://www.linkedin.com/jobs/search/?currentJobId=3625371467&f_AL=true&f_E=1&geoId=103644278&keywords=data%20intern&location=United%20States&refresh=true"
LinkedIn_email = "jzheng3@babson.edu"
LinkedIn_password = "ENTER KEY HERE"


driver = webdriver.Chrome()
driver.get(LinkedIn_Link)

# Login to the linkedin Account
sign_in_button = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in_button.click()
time.sleep(5)

user_name_box = driver.find_element(By.ID, "username")
password_box = driver.find_element(By.ID, "password")
user_name_box.send_keys(LinkedIn_email)
password_box.send_keys(LinkedIn_password)
time.sleep(2)

signin_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
signin_button.click()
time.sleep(5)

def click_easy_application():
    try: 
        easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        easy_apply.click()
        time.sleep(4)
        return True
    except NoSuchElementException:
        return False

def submit_application():
    submit_application = driver.find_element(By.CSS_SELECTOR, "footer button")
    if submit_application.get_attribute("innerText") == "Next":
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
        time.sleep(2)
        discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
        discard_button.click()
        time.sleep(2)
    else:
        submit_application.click()
        time.sleep(3)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
        time.sleep(3)

# Apply for jobs
job_lists = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for job in job_lists:
    job.click()
    time.sleep(3)
    if click_easy_application():
        submit_application()




