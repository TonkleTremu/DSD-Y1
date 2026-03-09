import pandas as pd, matplotlib.pyplot as plt, matplotlib.style as style

FILENAME = "Game_Shop_Sales_300_Rows.csv"

plt.style.use("classic")

df = pd.read_csv(FILENAME)

def GamesSales():
    total_revenues = df.groupby(["Game Title"])["Total Revenue (£)"].sum().to_dict()
    plt.xlabel("Game")
    plt.ylabel("Total Revenue")
    plt.grid()
    plt.bar(total_revenues.keys(), total_revenues.values())
    plt.show()

def GenreSales():
    total_revenues = df.groupby(["Category"])["Total Revenue (£)"].sum().to_dict()
    plt.xlabel("Game")
    plt.ylabel("Total Revenue")
    plt.grid()
    plt.bar(total_revenues.keys(), total_revenues.values())
    plt.show()


def GameSalesTime():
    games = df["Game Title"].unique()
    game_chosen = False
    while(game_chosen == False):
        for x in games:
            print(x)
        game = input("Which game would you like to check?\n")
        if(game in games):
            game_chosen = True
    dates_and_such = df.loc[df["Game Title"] == game].groupby("Date")
    total_revenues = dates_and_such["Total Revenue (£)"].sum()

    plt.xlabel("Date")
    plt.ylabel("Daily Revenue")
    plt.xticks(rotation=45, ha="right")
    plt.plot(total_revenues)
    plt.show()

def GenreSalesTime():
    genres = df["Category"].unique()
    genre_chosen = False
    while(genre_chosen == False):
        for x in genres:
            print(x)
        genre = input("Which genre would you like to check?\n")
        if(genre in genres):
            genre_chosen = True
    dates_and_such = df.loc[df["Category"] == genre].groupby("Date")
    total_revenues = dates_and_such["Total Revenue (£)"].sum()

    plt.xlabel("Date")
    plt.ylabel("Daily Revenue")
    plt.xticks(rotation=45, ha="right")
    plt.plot(total_revenues)
    plt.show()

def MainMenu():
    choix = input("What would you like to do?\n1. Analyse best-selling games.\n2. Check best-selling genres.\n3. View sales of a game over time.\n4. View sales of a genre over time.\n")
    if(choix == "1"):
        GamesSales()
    elif(choix == "2"):
        GenreSales()
    elif(choix == "3"):
        GameSalesTime()
    elif(choix == "4"):
        GenreSalesTime()
    elif(choix.lower() == "quit"):
        exit()
    MainMenu()
MainMenu()