import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

plt.style.use("classic")

FILEPATH = "Task4a_data.csv"

#Displays the main menu and collects choice of menu item
def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. ")

        main_menu_choice = input("Please enter the number of your choice (1-2): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 2:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

#Menu item selection form user and validates it
def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos", "Soup", "Burger", "Brisket", "Ribs", "Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name

#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY): ')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return pd.to_datetime(start_date, format="%d/%m/%Y").date().strftime("%d/%m/%Y") # This line is really convoluted to allow 3/3/2023 to be inputted without extra zeroes.

#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY): ')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return pd.to_datetime(end_date, format="%d/%m/%Y").date().strftime("%d/%m/%Y") # This line is really convoluted to allow 3/3/2023 to be inputted without extra zeroes.


#imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv(FILEPATH) 
    df2 = df1.loc[df1['Menu Item'] == item]
    df3 = df2.loc[:,startdate:enddate]

    return df3

     
main_menu = menu()
if main_menu == 1: # Gives data about a specific item.

    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
 
    extracted_data = get_selected_item(item, start_date, end_date)
    
    print(f"Here is the sales data for {item} between dates {start_date} and {end_date}:")
    extract_no_index = extracted_data.to_string(index=False)
    print(extract_no_index)

    print(f"Overall, {sum(extracted_data.sum())} servings of {item} were sold.")

    # Makes a graph showing sales at dinner/lunch over time.
    plt.title(f"Generated table showing sales of {item} over time.")
    plt.xlabel("Date")
    plt.ylabel(f"{item} Sold")
    plt.plot(extracted_data.columns, extracted_data.values[0], label="Lunch")
    plt.plot(extracted_data.columns, extracted_data.values[1], label="Dinner")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.show()

elif main_menu == 2: # Finds the highest total and average product. Due to basic common sense, it will always be the same product.
    totals = []
    averages = []
    menu_list = ["Nachos", "Soup", "Burger", "Brisket", "Ribs", "Corn", "Fries", "Salad"]
    start_date = get_start_date()
    end_date = get_end_date()

    for item in menu_list:
        extracted_data = get_selected_item(item, start_date, end_date)
        
        totals.append(sum(extracted_data.sum()))
        averages.append(extracted_data.mean().mean())
    
    highest_val = max(totals)
    highest_average = max(averages)

    print(f"{menu_list[totals.index(highest_val)]} was the highest total, at {highest_val}.")
    print(f"{menu_list[averages.index(highest_average)]} was the highest average, at around {round(highest_average)}.")

else:
    print('This part of the program is still under development, or an invalid option was entered.')
