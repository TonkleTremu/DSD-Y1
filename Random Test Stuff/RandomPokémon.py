import requests

dex = int(input("Pick a number from 1-1025:\n"))

url = f"http://pokeapi.co/api/v2/pokemon/{dex}/"
response = requests.get(url)
print(response.text)