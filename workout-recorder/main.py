import requests
import datetime as dt
import os

today = dt.datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")

# Nutritionix API ~ nx
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

nx_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety API

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TOKEN = os.getenv("TOKEN")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")

projectName = "myWorkoutsForPython"
sheetName = "workouts"

sheetyEndpoint = f"{SHEET_ENDPOINT}/{projectName}/{sheetName}"

nx_params = {
    "query": input("What workout did you do? Please include duration: ")
}

nx_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

sheetyHeaders = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

response = requests.post(url=nx_endpoint, json=nx_params, headers=nx_headers)
nx_data = response.json()["exercises"][0]

exercise = nx_data["name"].title()
duration = nx_data["duration_min"]
calories = nx_data["nf_calories"]

workout_row = {
    "workout": {
        "date": today_date,
        "time": today_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

sheety_post = requests.post(sheetyEndpoint, auth=(USERNAME, PASSWORD), headers=sheetyHeaders, json=workout_row)
print(workout_row)
print(sheety_post.status_code, sheety_post.text)
