import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style 

plt.style.use("classic")

df = pd.read_csv("students.csv")

print(df.head())

df.info()

print(df["Grade"].value_counts())


AtRisk = df
AtRisk["AtRisk"] = df["Attendance"] < 80

print(AtRisk)
AtRisk.to_clipboard()

df.sort_values("Attendance", ascending=False)

print(df.head(1))

plt.subplot(1, 3, 2)
plt.xlabel("Grade")
plt.ylabel("Number of learners")
plt.bar(df["Grade"], df["Grade"])