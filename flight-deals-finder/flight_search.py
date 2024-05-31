import requests
import os

API_KEY = os.environ.get('API_KEY')
API_SECRET = os.environ.get('API_SECRET')

FLIGHTS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
# API documentation: https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api
# -reference

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.api_key = API_KEY
        self.api_secret = API_SECRET
        self.endpoint = FLIGHTS_ENDPOINT
        self.destination = input("Enter Destination (IATA Code): ")
        self.departure_date = input("Enter Flight Date (YYYY-MM-DD): ")

    def get_access_token(self, api_key, api_secret):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": api_key,
            "client_secret": api_secret
        }
        response = requests.post(url, headers=headers, data=data)
        response_data = response.json()

        if response.status_code == 200:
            access_token = response_data["access_token"]
            return access_token
        else:
            raise Exception(response.status_code)

    def search_flights(self):
        search_params = {
            "originLocationCode": "IST",
            "destinationLocationCode": self.destination,
            "departureDate": self.departure_date,
            # "returnDate": "optional",
            # "nonStop": False
            "adults": 1
        }

        token = self.get_access_token(api_key=self.api_key, api_secret=self.api_secret)
        headers = {
            "Authorization": "Bearer " + token
        }
        response = requests.get(self.endpoint, params=search_params, headers=headers)
        response_data = response.json()

        if response.status_code == 200:
            response_data['destination'] = self.destination
            return response_data
        else:
            raise Exception(response.status_code, response.text)

# fs = FlightSearch()
# token = fs.get_access_token(api_key=API_KEY, api_secret=API_SECRET)
# print(token)
# data = fs.search_flights()
# print(data)
