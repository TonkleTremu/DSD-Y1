from datetime import datetime

StudentRecords = [{"loan_id": 1, "student_name": "Alex Green", "student_id": "S12345", "device_type": "Laptop", "device_id": "L-001", "date_out": "24/11/2025", "due_back": "1/12/2025", "returned": False}, {"loan_id": 2, "student_name": "Connor East", "student_id": "S54321", "device_type": "Laptop", "device_id": "L-002", "date_out": "24/11/2025", "due_back": "1/12/2025", "returned": False}] # Format: {"loan_id": 1, "student_name": "Alex Green", "student_id": "S12345", "device_type": "Laptop", "device_id": "L-001", "date_out": "2025-11-24", "due_back": "2025-12-01", "returned": False}
DeviceTypes = ["Laptop", "Tablet"]


def ValidateInt(Data, Variable): # Data is like 1, variable is like loan_id. This saves me from making 100 definitions for the same thing.
    if(Variable == "loan_id"): # Validates a loan id - cannot be a duplicate.
        try:
            Data = int(Data)
            if(Data <= 0):
                print("No negative numbers allowed!")
                return(True)
            for x in StudentRecords:
                if(Data in x.values()):
                    print("That ID is already taken!")
                    return(True)
            return(False)
        except:
            print("That is not an integer!")
            return(True)
    elif(Variable == "device_type"): # Validates device names - must be from "DeviceTypes[]"
        if(Data in DeviceTypes):
            return(False)
        else:
            return(True)      
    elif(Variable == "device_id"): # Validates device_id - must not be duplicate.
        for x in StudentRecords:
            if(Data in x.values()):
                print("That ID is already taken!")
                return(True)
        return(False)
    elif(Variable == "date"): # Validates dates. Dates must be valid dates.
        try:
            Date = datetime.strptime(Data, "%d/%m/%Y").date()
            return(False)
        except:
            return(True)
    elif(Variable == "returned"): # Validates "returned" - it must be "y" or "n"
        if(Data == "y" or Data == "n"):
            return(False)
        else:
            return(True)
    else:
        return(True)

def ViewLoan(): # Displays a specific loan and their details.
    student_id = input("What is the student's ID, or the device's ID?\n").capitalize()
    for x in StudentRecords:
        if(student_id in x.values()):
            for y in x:
                print(f"{y}: {x[y]}")
            print("\n-------\n")

def ViewLoans(): # Displays all loans and their details.
    for x in StudentRecords:
        for y in x:
            print(f"{y}: {x[y]}")
        print("\n-------\n")
    
def EditLoan(): # Edit a specific loan, given the student or device ID.
    student_id = input("What is the student's ID, or the device's ID that you would like to change a detail about?\n").capitalize()
    for x in StudentRecords:
        if(student_id in x.values()):
            for y in x:
                print(f"{y}: {x[y]}")
            Change = input("\nWhat needs changing?\n")
            ChangeTo = input("What should it be changed to?\n")
            try:
                if(ChangeTo.lower() == "y"):
                    ChangeTo = True
                elif(ChangeTo.lower() == "n"):
                    ChangeTo = False
            except:
                pass

            StudentRecords[StudentRecords.index(x)].update({Change: ChangeTo})
        
def DeleteLoan(): # Deletes a loan, given the corresponding student or device ID.
    student_id = input("What is the student's ID, or the device's ID that you would like to delete?\n").capitalize()
    for x in StudentRecords:
        if(student_id in x.values()):
            StudentRecords.pop(StudentRecords.index(x))

def NewLoan(): # Creates a new loan. There's probably a more efficient way to write all this code. Actually, there is, but I don't want to.
    loan_id = input("What is the loan's ID?\n")
    while(ValidateInt(loan_id, "loan_id")):
        loan_id = input("What is the loan's ID?\n")
    student_name = input("What is the student's name?\n")
    student_id = input("What is the student's ID?\n")
    device_type = input("What is the device they loaned?\n").capitalize()
    while(ValidateInt(device_type, "device_type")):
        device_type = input("What is the device they loaned?\n").capitalize()
    device_id = input("What is the device's ID?\n")
    while(ValidateInt(device_id, "device_id")):
        device_id = input("What is the device's ID?\n")
    date_out = input("What date was it taken?\n")
    while(ValidateInt(date_out, "date")):
        date_out = input("What date was it taken?\n")
    due_back = input("What date is it due back?\n")
    while(ValidateInt(due_back, "date")):
        due_back = input("What date is it due back?\n")
    returned = input("Has it been returned? (Y/N)").lower()
    while(ValidateInt(returned, "returned")):
        returned = input("Has it been returned? (Y/N)").lower()
    if(returned == "y"):
        returned = True
    else:
        returned = False
    # This line appends the new dictionary to the list.
    StudentRecords.append({"loan_id": loan_id, "student_name": student_name, "student_id": student_id, "device_type": device_type, "device_id": device_id, "date_out": date_out, "due_back": due_back, "returned": returned})

def MainMenu(): # Contains a menu for all functions.
    Choix = input("What do you want to do?\n1. Add new loan.\n2. View all loans.\n3. View specific loans.\n4. Edit loan.\n5. Delete loan.\n")
    if(Choix == "1"):
        NewLoan()
    elif(Choix == "2"):
        ViewLoans()
    elif(Choix == "3"):
        ViewLoan()
    elif(Choix == "4"):
        EditLoan()
    elif(Choix == "5"):
        DeleteLoan()
    else:
        print("Only enter a number from the valid range.")
    MainMenu()
MainMenu()