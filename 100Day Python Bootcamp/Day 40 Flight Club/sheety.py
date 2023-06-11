import requests

auth = ("flight_deals", "key")
url = "https://api.sheety.co/0d66d2433f110b62f91adfb3228e9f20/flightDeals/users"

def add_customer(f_name, l_name, email):
    new_data = {"user": 
                {"firstName": f_name, 
                 "lastName":l_name, 
                 "email":email
                 }
                }
    response = requests.post(url = url, json = new_data, auth = auth)
    response.raise_for_status()
    return response.text
