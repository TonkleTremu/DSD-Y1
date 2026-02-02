import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pixelvault game sales.csv")

print(df["game_title"].mode())
print(df.groupby(["category"])["total_sale"].sum().sort_values())
print(df.groupby(["category"])["total_sale"].max().sort_values())
print(df.groupby(["category"])["category"].sum().sort_values())
print(df.groupby(["game_title"])["price"].mean())