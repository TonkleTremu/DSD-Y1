import matplotlib.pyplot as plt
from matplotlib import style 
import math
import random
import csv

x = []
y = []

types = {"Water": 0, "Fire": 0, "Grass": 0, "Electric": 0, "Poison": 0, "Dragon": 0, "Fairy": 0, "Ice": 0, "Steel": 0, "Ground": 0, "Rock": 0, "Ghost": 0, "Dark": 0, "Psychic": 0, "Flying": 0, "Normal": 0, "Fighting": 0, "Bug": 0}

with open("Pokemon.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for line in reader:
        if(int(line[0])%10 == 0):
            print(line)
            x += [line[0]]
            y += [line[4]]
        types.update({line[2]: types.get(line[2])+1})
        try:
            types.update({line[3]: types.get(line[3])+1})
        except:
            print("Null second typing.")

plt.style.use("classic")

print(types)


plt.subplot(1,2,1)
plt.xlabel("Dex No.")
plt.ylabel("BST")
plt.xticks(rotation=90, ha="right")
plt.plot(x,y, label="Power Creep")
plt.legend()



plt.subplot(1,2,2)
plt.xlabel("Types")
plt.ylabel("Pokémon with type")
plt.xticks(rotation=45, ha="right")
plt.bar(types.keys(), types.values(), label="Abundancy of Types")
plt.legend()
plt.show()