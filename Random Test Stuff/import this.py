import requests

thing = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
print(thing.text)