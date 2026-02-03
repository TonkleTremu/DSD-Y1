import pandas as pd
import matplotlib.pyplot as plt

# Best matplotlib style.
plt.style.use("classic")

# Creates 3 dataframes correspondant to the 3 csv files.
countries = pd.read_csv("CountriesSD.csv")
summer = pd.read_csv("SummerSD.csv")
winter = pd.read_csv("WinterSD.csv")

earned_medals = summer.groupby(["Country", "Medal"])["Medal"].value_counts()

plt.bar()
plt.show()

# did you know that you can alt-select a link so you can copy-paste the text without following the link? well, now you do.