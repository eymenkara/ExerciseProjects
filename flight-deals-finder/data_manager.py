import requests
import os

SHEETY_ENDPOINT = "https://api.sheety.co/81e2bcce9a9319a663517fd2beb98bca/flightFinder/flights"
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = SHEETY_ENDPOINT
        self.token = SHEETY_TOKEN
        self.headers = {"Authorization": self.token}

    def get_saved_flights(self) -> dict:
        response = requests.get(self.endpoint, headers=self.headers)
        return response.json()

    def update_flight(self, flight_deal: dict):
        sheet_data = requests.get(self.endpoint, headers=self.headers).json()
        row_id = int
        updated_row = {}

        for row in sheet_data['flights']:
            if row['iataCode'] == flight_deal['destination']:
                updated_row['flight'] = row
                updated_row['flight']['price'] = flight_deal['price']['total']
                row_id = updated_row['flight']['id']

        row_endpoint = f"{self.endpoint}/{row_id}"
        response = requests.put(row_endpoint, json=updated_row, headers=self.headers)
        return response.json()

# dm = DataManager()
# flights = dm.get_saved_flights()
# print(flights)
