import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style

df = pd.read_csv("retail_sales_1M_dataset.csv")

plt.style.use("classic")

df["total_sale"] = df["quantity"] * df["price"]

print(f"Total: £{sum(df["total_sale"])}")

products = {}
for x in df["product"].unique():
    print(f"{x}: £{round(sum(df.loc[df["product"] == x, "total_sale"]),2)}")
    products[x] = round(sum(df.loc[df["product"] == x, "total_sale"]),2)

categories = {}
for x in df["category"].unique():
    print(f"{x}: £{round(sum(df.loc[df["category"] == x, "total_sale"]),2)}")
    categories[x] = round(sum(df.loc[df["category"] == x, "total_sale"]),2)

plt.subplot(1,2,1)
plt.xlabel("Product")
plt.ylabel("Profit (in 10 millions)")
plt.xticks(rotation=60, ha="right")
plt.bar(products.keys(), products.values())

plt.subplot(1,2,2)
plt.pie(categories.values(), labels = categories.keys())

plt.show()

