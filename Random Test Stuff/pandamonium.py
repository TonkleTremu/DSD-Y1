import pandas as pd

pokemon = pd.read_csv("pokemonheaders.csv")
print(pokemon.loc[(pokemon.Total >= 700) | (pokemon.Speed >= 150)])
print(pokemon["Total"].describe())