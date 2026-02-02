import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("lego_sets.csv")

plt.xlabel("Theme")
plt.ylabel("Average Rating")
df["theme_name"] = df["theme_name"].fillna(0)
difficulties = df["theme_name"].unique()
prices = []
df["star_rating"] = df["star_rating"].fillna(0)
for difficulty in difficulties:
    prices.append(float(df.loc[df["theme_name"] == difficulty, "star_rating"].mean()))
top10 = []
top10themes = []
top10threshold = prices.sort()[9]
for x in len(prices):
    if(x >= top10threshold):
        top10.append(prices[x])
        top10themes.append(difficulties[x])
plt.bar(difficulties, prices)
plt.show()