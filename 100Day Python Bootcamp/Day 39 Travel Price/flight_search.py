import requests
API_key = "API_KEY_KIWI"
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
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
            }
    
        response = requests.get(
            url=location_endpoint, 
            headers=headers, 
            params=params)
        
        try:
            price = response.json()['data'][0]['price']
        except:
            return [arrival_code, None]
        
        return [arrival_code, price]
    