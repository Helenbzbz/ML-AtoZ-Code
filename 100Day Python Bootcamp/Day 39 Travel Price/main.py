#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirement

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.read_csv()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

# if sheet_data[0]["iataCode"] == "":
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     data_manager.read_csv = sheet_data
#     data_manager.update_destimation_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight_info = flight_search.search_flight_price(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        tomorrow,
        six_month_from_today
    )
