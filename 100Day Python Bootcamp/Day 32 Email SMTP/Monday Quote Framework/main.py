import smtplib
import datetime as dt
import random

destination_email = "helenbzbz@gmail.com"
myemail = "helenbzbz@outlook.com"
password = ""

def check_date():
    now = dt.datetime.now()
    day_of_week = now.weekday()
    return day_of_week == 1

def random_quotes():
    f = open("100Day Python Bootcamp/Day 32 Email SMTP/quotes.txt", "r")
    file_data = f.readlines()
    return random.choice(file_data)

if check_date():  
    connection = smtplib.SMTP("smtp.office365.com")
    connection.starttls()
    connection.login(user = myemail, password=password)
    connection.sendmail(from_addr=myemail, to_addrs=destination_email, 
                    msg = f"Subject:Quote\n\n{random_quotes()}")
    connection.close()

