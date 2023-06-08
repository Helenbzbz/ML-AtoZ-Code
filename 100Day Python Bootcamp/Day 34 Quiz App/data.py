import requests

response = requests.get(url = "https://opentdb.com/api.php?amount=10&type=boolean")
if response.status_code != 200:
    raise Exception("Something is wrong with API!")
question_data = response.json()['results']
