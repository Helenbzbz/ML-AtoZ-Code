##################### Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random

myname = "Helen Zheng"

def check_birthday():
    birthday_data = pd.read_csv("100Day Python Bootcamp/Day 32 Email SMTP/Birthday Letter/birthdays.csv")
    now = dt.datetime.now()
    today_date = now.day
    today_month = now.month
    today_brithday = birthday_data[(birthday_data['month'] == today_month) & (birthday_data['day'] == today_date)]
    return today_brithday

def random_letter():
    template_index = random.randint(1, 3)
    template = open(f"100Day Python Bootcamp/Day 32 Email SMTP/Birthday Letter/letter_templates/letter_{template_index}.txt").read()
    return template

def send_email(destination_email, body):
    myemail = "helenbzbz@outlook.com"
    password = ""
    connection = smtplib.SMTP("smtp.office365.com")
    connection.starttls()
    connection.login(user = myemail, password=password)
    connection.sendmail(from_addr=myemail, to_addrs=destination_email, 
                    msg = f"Subject:Happy Birthday!\n\n{body}")
    connection.close()

today_birthday = check_birthday()
if len(today_birthday) > 0:
    birthday_dict = today_birthday.to_dict(orient="records")
    for record in birthday_dict:
        template = random_letter()
        letter = template.replace("[NAME]", record['name'].upper()).replace("Angela", myname)
        send_email(record['email'], letter)

