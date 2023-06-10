import requests
API_key = "mrwLmeX-VZdWwpoB3HZusEAD42PRZQJz"
Affli_endpoint = "https://api.tequila.kiwi.com/"

class FlightSearch:
    def get_destination_code(self, city_name):
        location_endpoint = f"{Affli_endpoint}locations/query"
        headers = {"apikey": API_key}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        return response.json()['locations'][0]['code']

    def search_flight_price(self, depart_code, arrival_code, date_from, date_to):
        location_endpoint = f"{Affli_endpoint}search"
        headers = {"apikey": API_key}
        params = {
            "fly_from": depart_code, 
            "fly_to": arrival_code,
            "date_from": date_from,
            "date_to": date_to
            }
    
        response = requests.get(
            url=location_endpoint, 
            headers=headers, 
            params=params
            ).json()['data'][0]['price']
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {arrival_code}.")
            return None
        
        return [arrival_code, response]

