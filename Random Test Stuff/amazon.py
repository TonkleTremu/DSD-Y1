import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("classic")

df = pd.read_csv("amazon_sales_dataset.csv")

sales = df.groupby(["customer_region"])["total_revenue"].sum()

plt.bar(df["customer_region"].unique(), sales.values-7500000, bottom=7500000)
plt.show()