import requests
from datetime import datetime


USERNAME = "eymenkara"
TOKEN = "js-akd83er*92djwek-sad9.33d"

GRAPH_ID = "graph2"

today = datetime.now()
pixel_date = today.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Daily Mindfulness",
    "unit": "minutes",
    "type": "float",
    "color": "sora",
    "timezone": "Turkey"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_config = {
    "date": pixel_date,
    "quantity": input("How many minutes did you spend for mindfulness today?: "),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)


