#{'John Doe': [27, 2.56]}

Patients = {}

def NewPatient(): # Allows the user to add a new patient to "Patients"
    PatientName = input("What is the patient's name?\n")
    PatientAge = input("What is the patient's age?\n")
    PatientHeight = input("What is the patient's height? (in metres)\n")
    print(f"{PatientName} is {PatientAge} years old, and is {PatientHeight}m tall.")
    Patients[PatientName] = [PatientAge,PatientHeight]
    MainMenu()

def ViewPatient(): # Allows the user to view an existing patient from "Patients"
    Patient = input("Which patient?\n")
    print(f"{Patient} is {Patients[Patient][0]} years old and is {Patients[Patient][1]}m tall.")

def MainMenu(): # The main menu. It allows the user to access all areas of the program.
    Choixs = input("1. Patient Data\n2. BMI Calc\n3. Dosage Calc\n4. Bill Calc\n")
    if(Choixs == "1"):
        Choix = input("Add a new patient, or view existing?\n")
        if(Choix[0].lower() == "a" or Choix[0].lower() == "n"):
            NewPatient()
        elif(Choix[0].lower() == "v" or Choix[0].lower() == "e"):
            ViewPatient()
        else:
            print("Try again.")
            MainMenu()
    elif(Choixs == "2"):
        BMIcalc()
    elif(Choixs == "3"):
        DosageCalc()
    elif(Choixs == "4"):
        Bill()
    else:
        print("Try again.")
        MainMenu()

def BMIcalc(): # Calculates a patient's BMI.
    Height = float(input("What is the patient's height?\n"))
    Weight = float(input("What is the patient's weight?\n"))
    BMI = Weight/(Height*Height)
    if(BMI <= 18.5):
        print(f"At {BMI}, the patient is underweight.")
    elif(BMI <= 25):
        print(f"At {BMI}, the patient is a healthy weight.")
    elif(BMI <= 30):
        print(f"At {BMI}, the patient is overweight.")
    else:
        print(f"At {BMI}, the patient is obese.")
    MainMenu()
    
def DosageCalc(): # Calculates whether a patient is over their maximum dosage.
    MAXDOSAGE = float(input("What is the max limit of the medicine?\n"))
    IsChild = input("Is the person a child (under 18)?\n")
    if(IsChild[0].lower() == "y"): # This is an example number, I don't know how the age-medicine thing works.
        MAXDOSAGE /= 2
    CurrentDosage = float(input("How much medicine have you given them?\n"))
    if(CurrentDosage >= MAXDOSAGE):
        print("They have reached the maximum dosage. Good luck!\n")
    elif(CurrentDosage >= 0.8 * MAXDOSAGE):
        print("The patient is over 80% of the way to the max dosage.")
    else:
        print("The patient is fine.")
    MainMenu()

def Bill(): # This calculates an overcharged bill. American healthcare, essentially. "Service cost" is a made-up parameter created just to charge even more money.
    DaysStayed = int(input("How many days did they stay?\n"))
    ServiceCost = float(input("What is their service cost?\n£"))
    MedCost = float(input("How much did their treatment cost?\n£"))
    RoomQuality = float(input("Ask the patient to rate their room from 1-10, 10 being the best.\n"))
    Doctors = int(input("How many doctors served them?\n"))

    TotalCost = (DaysStayed*20 + ServiceCost + MedCost*1.25 + RoomQuality*20 + Doctors*50) * 1.2 # Amazing formula if you ask me. Source: I made it up.
    print(f"The total cost is £{TotalCost}")
    MainMenu()

# These each call their respective functions. Right-click and select "go to definition" to find the functions easier.
#Bill()
#DosageCalc()
#BMIcalc()
MainMenu()