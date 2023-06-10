import requests
from twilio.rest import Client
import os

class NotificationManager:

    def send_message(self, body):
        client = Client("ACb7d25a9cec7cc9c1eace24622eced7f7", "TOKEN")
        message = client.messages \
                .create(
                     body=body,
                     from_='+18337530797',
                     to='+17813758277'
                 )
        try:
            print(message.sid)
        except:
            print("Message Sent Failed")

