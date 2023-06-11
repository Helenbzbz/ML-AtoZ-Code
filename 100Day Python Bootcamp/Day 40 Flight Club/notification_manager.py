from twilio.rest import Client
import smtplib

TWILIO_SID = "ACb7d25a9cec7cc9c1eace24622eced7f7"
TWILIO_AUTH_TOKEN = ""
TWILIO_VIRTUAL_NUMBER = "+18337530797"
TWILIO_VERIFIED_NUMBER = "+17813758277"
SENDER = "helenbzbz@outlook.com"
PWD = ""


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
    
    def send_email(self, email, message):
        connection = smtplib.SMTP("smtp.office365.com")
        connection.starttls()
        connection.login(user = SENDER, password=PWD)
        connection.sendmail(
            from_addr=SENDER, 
            to_addrs=email, 
            msg = message)
        connection.close()