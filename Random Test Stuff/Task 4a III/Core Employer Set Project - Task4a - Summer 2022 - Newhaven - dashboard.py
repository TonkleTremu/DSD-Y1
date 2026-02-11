import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Rather than needing to change the filename in several places later, a constant has been set up.
FILENAME = "Core Employer Set Project - Task4A - Data - Summer 2022.csv"
# The dataframe is established, which is used for reading and analysing data from the csv.
df = pd.read_csv(FILENAME)
# Sets the theme. To customise, reference a list of matplotlib styles using plt.style.available()
plt.style.use("classic")


def mainmenu():
    '''This function returns the user's choice of what they'd like to do.'''
    print("\t\t****Welcome to the Dashboard****")
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print('3) Return sizes for a specific property type in a region')
    return input("")


def region_check(region, startdate, enddate):
    '''This function takes the parameters from regional_data() and displays a graph showing the change over time.'''

    # This line creates a new dataframe, df1, which contains only the numerical data.
    df1 = df.loc[:, startdate:enddate]
    # This lines creates a dataframe, df2, which contains only the categorical data, such as region.
    df2 = df.loc[:, 'Region Code':'Rooms']
    
    # This makes a new dataframe, result, which only contains data that matches the specified region.
    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    result = pd.DataFrame(result)
    # Error handling - any missing values are simply removed.
    result.dropna(inplace=True)

    # Basic setup for the graph. ave is the average for each month.
    ave = result.loc[:, startdate:enddate].mean()
    plt.xlabel("Month")
    plt.ylabel("Value")
    ave.plot()
    plt.show()
    return result
    
def regional_data():
    while True:
            # Gives the user a list of regions. They then select from them.
            print("\t\t****Regions:****")
            for unique_region in df["Region"].unique():
                print(unique_region)
            region = input("\nPlease enter the name of the region you would like to check:\n")
            region = region.capitalize()
            if region in df.Region.values:
                while True:
                    # Gives the user a list of start dates. They then select from them.
                    print("\t\t****Dates:****")
                    for unique_date in df.columns[4:]:
                        print(unique_date)
                    startdate = input("Please select one of start dates as month-year.\n")
                    startdate = startdate.capitalize()
                    if startdate not in df.columns:
                        print("Error - start date not found")
                    else:
                        while True:
                            # Gives the user a list of end dates. They then select from them.
                            print("\t\t****Dates:****")
                            for unique_date in df.columns[df.columns.get_loc(startdate)+1:]:
                                print(unique_date)
                            enddate = input("Please select one of end dates as month-year.\n")
                            enddate = enddate.capitalize()
                            if enddate not in df.columns[df.columns.get_loc(startdate)+1:]:
                                print("Error - end date not found")
                            else:
                                # If everything is valid, this function is called.
                                region_check(region, startdate, enddate)
                                break
                        break
                break
            else:
                print("Region not found")


x = mainmenu()
while True:
    # Error handling if x is not an integer.
    try:
        x = int(x)
    except:
        pass
    if type(x) == str:
        print("That is not a valid integer.")
    else:
        # If x is an integer, we check if it corresponds to a function. If not, we give an error message.
        if x == 1:
            print(df)
        elif x == 2:
            regional_data()
        elif x == 3:
            pass
        else:
            print("That is not within the allowed range.")

    x = mainmenu()
