class FlightData:

    #This class is responsible for structuring the flight data.

    def __init__(self, sheet_json=dict, search_json=dict):
        self.sheet_data = sheet_json
        self.search_data = search_json

        self.destination = search_json['destination']
        self.saved_prices = {item['iataCode']: item['price'] for item in self.sheet_data['flights']}
        self.cheapest_price = float(self.saved_prices[self.destination])
        self.new_deal = None

    def find_deal(self):
        for deal in self.search_data['data']:
            if float(deal['price']['total']) < self.cheapest_price:
                self.cheapest_price = float(deal['price']['total'])
                self.new_deal = deal
                self.new_deal['destination'] = self.destination
        if self.new_deal == None:
            print('No new deal found')
        return self.new_deal
