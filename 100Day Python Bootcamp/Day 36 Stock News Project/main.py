import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "TRG6IBRYE7QM9QUY"
NEWS_API_KEY = "31e36e93ead24bf187b9a64aafc6c8c3"
MESSAGE_API_KEY = "161a1eb87b72bb40456617fb8192d778"

THRESHOLD = 0.01

def get_stock_price():
    response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={STOCK_API_KEY}")
    response.raise_for_status()
    stock_data = list(response.json()['Time Series (Daily)'].values())

    price_now = float(stock_data[0]['4. close'])
    price_previous = float(stock_data[1]['4. close'])
    return (price_now - price_previous)/price_previous

def get_news():
    response = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2023-06-01&sortBy=publishedAt&apiKey={NEWS_API_KEY}")
    response.raise_for_status()
    company_news = response.json()['articles']
    
    return [[company_news[i]["title"], company_news[i]["description"]] for i in range(3)]
    
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_message():
    stock_change = get_stock_price()
    if abs(stock_change) >= THRESHOLD:
        company_news = get_news()
        if stock_change > 0: notation = "🔺"
        else: notation = "🔻"

        message = ""
        for news in company_news:
            message += f"TSLA: {notation}{stock_change*100}%\n"
            message += f"Headline: {news[0]}\n"
            message += f"Breif: {news[1]}\n"


        client = Client("ACb7d25a9cec7cc9c1eace24622eced7f7", os.environ.get())
        message = client.messages \
                .create(
                     body="It's raining outside :)",
                     from_='+18337530797',
                     to='+17813758277'
                 )
        try:
            print(message.sid)
        except:
            print("Message Sent Failed")

send_message()

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

