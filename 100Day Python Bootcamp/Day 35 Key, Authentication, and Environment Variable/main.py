import requests
from twilio.rest import Client
import os

latitude = 31.230391
longitude = 121.473701
API_key = "161a1eb87b72bb40456617fb8192d778"

API_address = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&&appid={API_key}"

is_rain = False
response = requests.get(API_address)
weather_code = response.json()['weather'][0]['id']
if weather_code < 700:
    is_rain = True
print(weather_code, is_rain)

if is_rain:
    client = Client("ACb7d25a9cec7cc9c1eace24622eced7f7", os.environ.get('AUTH_TOKEN'))
    message = client.messages \
                .create(
                     body="It's raining outside :)",
                     from_='+18337530797',
                     to='+17813758277'
                 )
try:
    print(message.sid)
except:
    print("not raining")

