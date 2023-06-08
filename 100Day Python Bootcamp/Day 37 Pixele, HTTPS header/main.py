# Request an account
import requests
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "/",
    "username":"helenbzbz1",
    "agreeTermsOfService" : "yes",
    "notMinor":"yes"
}

# reponse = requests.post(url = pixela_endpoint, json = user_params)
# print(reponse.text)

# Create a graph
USER_NAME = "helenbzbz1"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
headers = {
    "X-USER-TOKEN": "/"
}

graph_params = {
    "id": "graph1",
    "name": "coding habbit",
    "unit": "days",
    "type" : "int",
    "color": "sora"
}
# response = requests.post(url = graph_endpoint, json = graph_params, headers=headers)
# print(response.text)

# Add Pixel
from datetime import datetime
GRAPH_ID = "graph1"
pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today_date = datetime.now().strftime("%Y%m%d")

pixel_params = {
    "date": today_date,
    "quantity": "8",
}

response = requests.post(url = pixel_endpoint, json = pixel_params, headers=headers)
print(response.text)