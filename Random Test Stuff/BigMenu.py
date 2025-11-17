Patients = {"Kyle": ["15", "1.7", "70"]}

def BmiCalc(): # Calculates a patient's BMI.
    Patient = input("Who is the patient?\n")
    Height = float(Patients[Patient][1])
    Weight = float(Patients[Patient][2])
    BMI = round(Weight/(Height*Height),2)
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

def ViewTotal(): # Tells the user many patients they have.
    print(f"You have {len(Patients)} patients.")
    MainMenu()

def MainMenu():
    Choix = input("What would you like to do?\n1. Add patient data.\n2. Remove patient data.\n3. Edit patient data.\n4. Calculate a patient's BMI.\n5. Calculate recommended dosage.\n6. View how many patients you have.\n7. Close the system.\n")
    if(Choix == "1"):
        Patient = input("Which patient's data should be added?\n")
        Age = input("What is the patient's age?\n")
        Height = input("What is the patient's height?\n")
        Weight = input("What is the patient's weight?\n")
        Patients.update({Patient:[Age, Height, Weight]})
        MainMenu()
    if(Choix == "2"):
        Patient = input("Which patient's data should be removed?\n")
        if(Patient.lower() == "all"):
            Patients.clear()
            print("Poof!")
        else:
            Patients.pop(Patient)
            print("Gone!")
        MainMenu()
    elif(Choix == "3"):
        Patient = input("Which patient's data do you want to change?\n")
        ThingToChange = input("Do you want to change their age, height or weight?\n").lower()
        if(ThingToChange == "age"):
            Patients[Patient][0] = input("What do you want to change their age to?\n")
        elif(ThingToChange == "height"):
            Patients[Patient][1] = input("What do you want to change their height to?\n")
        elif(ThingToChange == "weight"):
            Patients[Patient][2] = input("What do you want to change their weight to?\n")
        else:
            print("Please only type age, height or weight.")
        MainMenu()
    elif(Choix == "4"):
        BmiCalc()
    elif(Choix == "5"):
        DosageCalc()
    elif(Choix == "6"):
        ViewTotal()
    elif(Choix == "7"):
        print("Closing down.")
    else:
        print("Please only enter a number from 1-7.")
        MainMenu()

MainMenu()