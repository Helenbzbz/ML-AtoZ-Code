import requests
from datetime import datetime
import os

basic = (os.environ.get('BASIC_USER'),os.environ.get('BASIC_KEY'))

NU_KEY = "8d9e94c6400e506fa90f40f2cc29b46b"
NU_ID = "e20b48ef"
NU_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "female"
WEIGHT_KG = 78
HEIGHT_CM = 170
AGE = 21

# Get Exercise Calories Calculated
header = {
    "x-app-id": NU_ID,
    "x-app-key": NU_KEY
    }

query = input("Tell me which exercies you did: ")
exercise_params = {
 "query":  query,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}

response = requests.post(NU_ENDPOINT, exercise_params, headers = header).json()
exercise_data = response['exercises']
print(exercise_data)

# Add a record to the sheet
g_sheet_url = "https://api.sheety.co/0d66d2433f110b62f91adfb3228e9f20/myWorkouts/workout"

today = datetime.now()

DATE = str(today.date())
TIME = str(today.time())

for exercise in exercise_data:
    body = {
    "workout": {
	    "date": DATE,
	    "time": TIME,
        "exercise": exercise["user_input"],
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
    }
    } 
    response = requests.post(g_sheet_url, json = body, auth = basic)
    print(response.json())