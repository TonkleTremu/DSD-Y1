import pandas as pd
import csv
import matplotlib.pyplot as plt

plt.style.use("classic")
csvfile = "Task4a_data.csv"

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. Time taken to resolve types of issues")
        print("### 3. Issues and resolutions based on region")

        choice = input('Enter your number selection here: ')

        flag = CheckIntValidation(choice, 3)

    return choice

# Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        flag = CheckIntValidation(choice, 4)

    choice = int(choice)
    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice-1]
  
    return issueType     

# Checks if the user's choice is both a valid integer and within the alloted range.
def CheckIntValidation(choice, maxValues):
    try:
        int(choice)
    except:
        print("Sorry, you did not enter a valid option")
        return(True)
    else:    
        choice = int(choice)
        if(choice <= 0 or choice > maxValues):
            print("Sorry, you did not enter a valid option")
            return("True")
        else:
            print('Choice accepted!')
            return(False)


# Creates a new dataframe then counts the number of occurences of the requested issue type
def get_total_data(total_menu_choice):
    
    issues = pd.read_csv(csvfile)
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg

# Finds the average time taken for each type of issue to be resolved, and produces a bar chart.
def find_time_taken():
    try: 
        issues = pd.read_csv(csvfile)
        issue_types = []
        averages = []
        for issue_type in issues["Issue Type"].unique():
            issue_types.append(issue_type)
            averages.append(issues.loc[issues["Issue Type"] == issue_type, "Days To Resolve"].mean())
        plt.xlabel("Issue Type")
        plt.ylabel("Average Response Time")
        plt.bar(issue_types, averages)
        plt.show()
    except:
        print(f"An issue was encountered when reading CSV data - have you checked that the file is named {csvfile} and that the format has not changed?")

# Creates a bar chart, which shows issue types and how they were resolved.
def regional_issues():
    flag = True
    while(flag):
        issues = pd.read_csv(csvfile)
        Regions = []
        # Iterates through every unique region in the CSV file. If more are added, this updates dynamically.
        print("########## Please select an issue type ##########")
        for temp_region in issues["Region"].unique():
            Regions.append(temp_region)
            print(f"### {len(Regions)}. {temp_region}")
        choice = input()
        flag = CheckIntValidation(choice, len(Regions))
    region = Regions[int(choice)-1]
    issue_types = []
    averages = []
    issues_of_region = issues.loc[issues["Region"] == region, ["Issue Type", "Days To Resolve"]]
    # Finds the averages and issues to be displayed.
    for issue_type in issues_of_region["Issue Type"].unique():
            issue_types.append(issue_type)
            averages.append(issues_of_region.loc[issues_of_region["Issue Type"] == issue_type, "Days To Resolve"].mean())
    plt.xlabel("Issue Type")
    plt.ylabel("Average Response Time")
    plt.bar(issue_types, averages)
    plt.show()


main_menu_choice = main_menu()
if(main_menu_choice ==  "1"):
    total_menu_choice = total_menu()
    print(get_total_data(total_menu_choice))
elif(main_menu_choice == "2"):
    find_time_taken()
elif(main_menu_choice == "3"):
    regional_issues()
