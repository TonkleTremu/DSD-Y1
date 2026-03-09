import requests
import json

def FindPlace():
    place_name = input("Enter a place name (or 'quit'):\n").capitalize()
    
    if(place_name != "" and place_name != "Quit"):
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={place_name}"
        try:
            # Takes the raw data from the website.
            raw_data = requests.get(url=url)

            # Converts the hideous raw data into a useful dictionary. [0] exists, because for some reason they store it as a list with one element.
            data = json.loads(raw_data.text).get("results")[0]

            # Displays information including the place name, country, latitude and longitude.
            print(f"Place: {data.get("name")}, {data.get("country")}")
            latitude = data.get("latitude")
            print(f"Latitude: {latitude}")
            longitude = data.get("longitude")
            print(f"Longitude: {longitude}")
            
            # Calls a separate API to get forecast data.
            forecast_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m,precipitation,wind_direction_10m"
            raw_forecast = requests.get(forecast_url)

            # Tells the user the current temperature in the place. (In degrees celcius.)
            forecast = json.loads(raw_forecast.text)
            print(f"It is {forecast.get("current").get("temperature_2m")}°C in {data.get("name")}. The wind is blowing at {forecast.get("current").get("wind_speed_10m")}km/h on a bearing of {forecast.get("current").get("wind_direction_10m")}°. There is a precipitation of {forecast.get("current").get("precipitation")}mm")
        except:
            # If anything goes wrong, an error will be displayed. Everything before the error will still work as expected.
            print("Something went wrong during runtime. Some stats may not have loaded correctly.")
    if(place_name == "Quit"):
        exit()
    FindPlace()

# a horse walks into a bar. the bar says "ow". then, a gnome, elf and dwarf in a trenchcoat approach the horse and ask him if he works there. the horse replies, "no, I just got here". the bar goes up in flames.
FindPlace()