import requests
from bs4 import BeautifulSoup
import smtplib

URL_to_track = "https://www.amazon.com/Dyson-Cyclone-Animal-Cordless-Cleaner/dp/B0BTDXZBFL/ref=sr_1_1?keywords=dyson+vacuum+cleaners&qid=1686691737&s=home-garden&sprefix=vacuum+cleaners+dyson%2Cgarden%2C71&sr=1-1"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
MY_EMAIL = "helenbzbz@outlook.com"
EMAIL_PASSWORD = ""
TARGET_PRICE = 500
destination_email = "helenbzbz@gmail.com"

# Get price from Amazon
headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

response = requests.get(URL_to_track, headers=headers)
amazon_content = BeautifulSoup(response.text, "lxml")
product_name = amazon_content.find(name="span", id = "productTitle").text
price_whole = amazon_content.find(name="span", class_ = "a-offscreen").text
price_without_curr = float(price_whole.split("$")[1])

# Send Email alert
if price_without_curr < TARGET_PRICE:
    body = f"{product_name.strip()} is now {price_whole}\n{URL_to_track}"

    with smtplib.SMTP("outlook.office365.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=destination_email,
            msg=f"Subject:Amazon Price Alert!\n\n{body}".encode("utf-8")
        )
