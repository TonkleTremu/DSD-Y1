import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("classic")

def main_menu():
    flag = True

    while flag:

        print("#################################################")
        print("############## Snowy Animal Rescue ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average Social Media Interaction Data")
        print("### 2. Explore The Data")
        print("### 3. Interactions by Time of Day")

        choice = input('Enter your number selction here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice


def average_menu ():
    flag = True

    while flag:

        print("#################################################")
        print("############## Average Interaction ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average number of Likes")   
        print("### 2. Average number of Shares") 
        print("### 3. Average number of Comments")  
        print("### 4. Total Interactions by Post Type")

        choice = input('Enter your number selction here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice      

def convert_avg_men_coice(avg_men_choice):
    
    if avg_men_choice == "1":
        avg_choice = "Likes"
    elif avg_men_choice == "2":
        avg_choice = "Shares"
    elif avg_men_choice == "3":
        avg_choice = "Comments"  
    elif avg_men_choice == "4":
        avg_choice = "Total"

    return avg_choice


def get_avg_data(avg_choice):
    
    if avg_choice == "Total":
        df = pd.read_csv("Task4a_data.csv")
        extract = df.groupby(['Post Type'], as_index=False)[["Likes", "Shares", "Comments"]].sum()
        
        for x in range(1,5):
            plt.subplot(1,4,x)
            plt.title(df["Post Type"].unique()[x-1])
            plt.xlabel("Interaction Type")
            plt.ylabel("Interactions")
            values = list([list(extract["Likes"])[x-1], list(extract["Shares"])[x-1], list(extract["Comments"])[x-1]])
            values.append(sum(values))
            plt.bar(["Likes", "Shares", "Comments", "Total"], values)
        plt.show()
        return("")

    else:
        df = pd.read_csv("Task4a_data.csv")
        extract = df.groupby(['Date'], as_index=False)[avg_choice].mean()
        extract_no_index = extract.to_string(index=False)
        
        plt.plot(extract["Date"], extract[avg_choice])
        plt.show()

        print("Here is the average number of {} each day during the campaign:".format(avg_choice))
        return extract_no_index

def interactions_by_day(avg_choice):
    if avg_choice == "Total":
        avg_choice = "Likes"
        print("'Total' is not currently supported. 'Likes' are being used as default.")
    df = pd.read_csv("Task4a_data.csv")
    extract = df.groupby(['Time'], as_index=False)[avg_choice].mean()
    extract_no_index = extract.to_string(index=False)
    
    plt.xlabel("Time")
    plt.ylabel(avg_choice)
    plt.bar(extract["Time"], extract[avg_choice])
    plt.show()

def explore_data():
    df = pd.read_csv("Task4a_data.csv")
    print(df.head())
    print(df.columns)
    print(df.info())

main_menu_choice = main_menu()
if main_menu_choice == "1":
    avg_men_choice = average_menu()
    avg_choice = convert_avg_men_coice(avg_men_choice)
    print(get_avg_data(avg_choice))
elif main_menu_choice == "2":
    explore_data()
elif main_menu_choice == "3":
    avg_men_choice = average_menu()
    avg_choice = convert_avg_men_coice(avg_men_choice)
    interactions_by_day(avg_choice)

# Overall, images appear to have the most interactions, and the majority are shares - which may introduce new people to the organisation.
# The trends appear to fluctuate a lot, where sometimes there are many shares, sometimes comments are highest, and other times it's likes.
# Posts typically get the most interactions at midday.