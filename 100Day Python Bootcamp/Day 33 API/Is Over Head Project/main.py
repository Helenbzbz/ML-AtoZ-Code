import requests
from datetime import datetime
import pytz
import smtplib
import time

MY_LAT = 41.3083 # Your latitude
MY_LONG = -72.9279 # Your longitude
destination_email = "helenbzbz@gmail.com"
myemail = "helenbzbz@outlook.com"
password = "Zheng200139!"


def if_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    latitude_close = (iss_latitude > MY_LAT-5 and iss_latitude < MY_LAT + 5)
    longitude_close = (iss_longitude > MY_LAT-5 and iss_latitude < MY_LAT + 5)

    return (latitude_close and longitude_close)


def is_black():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = (data["results"]["sunrise"].split("T")[1].split(":"))
    sunrise_hour = int(sunrise[1])
    sunrise_min = int(sunrise[0])
    sunset = (data["results"]["sunset"].split("T")[1].split(":"))
    sunset_hour = int(sunset[1])
    sunset_min = int(sunset[0])
    
    UTC = pytz.utc
    time_now = datetime.now(UTC)
    now_hour = time_now.hour
    now_minute = time_now.minute

    havent_sunrise = (now_hour < sunrise_hour or (now_hour == sunrise_hour and now_minute < sunrise_min))
    already_sunset = (now_hour > sunset_hour or (now_hour == sunset_hour and now_minute > sunset_min))

    return (havent_sunrise or already_sunset)


def send_email():
    if if_iss_close() and is_black():
        connection = smtplib.SMTP("smtp.office365.com")
        connection.starttls()
        connection.login(user = myemail, password=password)
        connection.sendmail(from_addr=myemail, to_addrs=destination_email, 
                    msg = f"Subject:It's time!\n\nLook Up")
        connection.close()


while True:
    time.sleep(60)
    send_email()