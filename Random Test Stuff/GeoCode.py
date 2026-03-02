import requests
import json

def FindPlace():
    place_name = input("Enter a place name (or 'quit'):\n").capitalize()

    url = f"https://geocoding-api.open-meteo.com/v1/search?name={place_name}"

    try:
        # Takes the raw data from the website.
        raw_data = requests.get(url=url)

        # Converts the hideous raw data into a useful dictionary. [0] exists, because for some reason they store it as a list with one element.
        data = json.loads(raw_data.text).get("results")[0]

        print(f"Place: {data.get("name")}, {data.get("country")}")
        latitude = data.get("latitude")
        print(f"Latitude: {latitude}")
        longitude = data.get("longitude")
        print(f"Longitude: {longitude}")
        
        forecast_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&am…"
        print(forecast_url)
        raw_forecast = requests.get(forecast_url)

        forecast = json.loads(raw_forecast.text).get("results")[0]
        print(forecast)
    except:
        print("Something went wrong. Did you enter a real place name?")
    FindPlace()

FindPlace()