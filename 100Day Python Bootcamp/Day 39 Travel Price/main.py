#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirement

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.read_csv()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.read_csv = sheet_data
    data_manager.update_destimation_code()

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_month_from_today = (datetime.now() + timedelta(days=(6 * 30))).strftime("%d/%m/%Y")

for destination in sheet_data:
    flight_info = flight_search.search_flight_price(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        tomorrow,
        six_month_from_today
    )

    print(flight_info)
    if flight_info[1] != None and flight_info[1] < destination['lowestPrice']:
        body = (f"Low price alert! Only £{flight_info[1]} to fly from {ORIGIN_CITY_IATA} to {flight_info[0]}")
        NotificationManager().send_message(body)
