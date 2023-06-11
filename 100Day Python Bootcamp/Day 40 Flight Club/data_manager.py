from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/0d66d2433f110b62f91adfb3228e9f20/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/0d66d2433f110b62f91adfb3228e9f20/flightDeals/users"
auth = ("flight_deals", "key")

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth = auth)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def get_user_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, auth = auth)
        data = response.json()
        self.user_data = data['users']
        return self.user_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=auth
            )
            print(response.text)