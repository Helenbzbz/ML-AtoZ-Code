import requests
from flight_search import FlightSearch

class DataManager():

    def __init__(self) :
        #This class is responsible for talking to the Google Sheet.
        self.auth = ("flight_deals", "oinacouqd012")
        self.url = "https://api.sheety.co/0d66d2433f110b62f91adfb3228e9f20/flightDeals/prices"

    def read_csv(self):
        response = requests.get(url = self.url, auth = self.auth)
        data = response.json()['prices']
        return data

    def update_destimation_code(self):
        for city in self.read_csv():
            city_name = city['city']
            city_code = FlightSearch().get_destination_code(city_name)
            city_id = city['id']
            new_data = {"price": {"iataCode": city_code}}
            response = requests.put(f"{self.url}/{city_id}", json = new_data, auth=self.auth)
            print(response.text)

DataManager().update_destimation_code()


