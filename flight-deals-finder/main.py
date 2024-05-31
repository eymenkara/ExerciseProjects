from pprint import pprint

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

searcher = FlightSearch()
sheetData = DataManager()

sheetFlights = sheetData.get_saved_flights()
searchFlights = searcher.search_flights()

flightData = FlightData(sheet_json=sheetFlights, search_json=searchFlights)

flight_deal = flightData.find_deal()

if flightData.new_deal != None:
    response = sheetData.update_flight(flight_deal)

#shows the cheapest found deal details
found_deal = flightData.new_deal

pprint(found_deal)

