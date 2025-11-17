import matplotlib as plt

def UnitConv(): 
    '''Simple converter for blood glucose.'''
    CONSTANTINOPLE = 18 # This is devised from the formula, moles=mass/mr. Substituting in the values, we get moles = x/180. Then, accounting for the dL, we times by 10, so moles = x/18. Mass, therefore, is x*18.
    ConvFrom = input("What unit are you converting from? (mmol/L or mg/dL)\n")
    Measurement = float(input("What is the value?\n"))
    if(ConvFrom.lower() == "mmol/l"):
        print(f"In mg/dL, {Measurement} mmol/L is {Measurement*CONSTANTINOPLE}")
    elif(ConvFrom.lower() == "mg/dl"):
        print(f"In mmol/L, {Measurement} mg/dL is {Measurement/CONSTANTINOPLE}")
    else:
        print("Come again?")
    MainMenu()

def TempTrack(): 
    '''Calculates an average from 3 user entered values, and confirms whether or not they have a fever.'''
    Temps = [float(input("What is the first temperature reading? (these are all in Celcius)\n")),float(input("What is the second temperature reading?\n")),float(input("What is the third temperature reading?\n"))]
    Avreg = round(sum(Temps)/3,2)
    FEVER = 38
    if(Avreg >= FEVER):
        print(f"The average temperature is {Avreg}. This is too high! You have a fever.")
    else:
        print(f"Average is {Avreg}. You're fine.")
    MainMenu()

def HeartRateMon(): 
    '''Checks if a patient's resting heart rate is too high.'''
    Age = int(input("What is your age?\n"))
    RestRate = float(input("What is your resting heart rate?\n"))
    MaxRate = round(220-Age,2)
    if(RestRate >= MaxRate):
        print(f"How are you alive? You've exceeded the max rate of {MaxRate}!")
    elif(RestRate >= MaxRate * 0.75):
        print(f"Your resting heart rate is {RestRate}. This is way too close to your max of {MaxRate}")
    elif(RestRate >= MaxRate * 0.25):
        print(f"Your resting heart rate is {RestRate}. You are well below your max. ({MaxRate}) Good job!")
    else:
        print(f"Your resting heart rate is {RestRate}. This is way too low, compared to ({MaxRate}).")
    MainMenu()
        
def Hydration(): 
    '''Calculates if a person has drank enough water today.'''
    DAILY_GOAL = 2.25
    TodayIntake = float(input("How much water have you drank today, in litres?\n"))
    if(TodayIntake >= DAILY_GOAL):
        print(f"Congrats! You've drank over {DAILY_GOAL} litres of water!")
    elif(TodayIntake >= DAILY_GOAL * 0.5):
        print(f"Congrats! You're over halfway to your goal of {DAILY_GOAL}")
    else:
        print(f"You need to drink much more water to reach your goal of {DAILY_GOAL} litres.")
    MainMenu()
    
def MainMenu():
    '''The main menu. Not much else to say.'''
    Choix = int(input("What would you like to do?\n1. Convert glucose measurements.\n2. Calculate an average temperature.\n3. Check if someone's resting heart rate is normal.\n4. Track someone's hydration.\n"))
    if(Choix == 1):
        UnitConv()
    elif(Choix == 2):
        TempTrack()
    elif(Choix == 3):
        HeartRateMon()
    elif(Choix == 4):
        Hydration()
    else:
        print("No.")
    MainMenu()

# Most important line of code. Without it, the Democratic Republic of Congo's government collapses.
MainMenu()

# These are here so you can Right Click -> Go To Definition. Just much easier than searching through stuff. Since they are after MainMenu(), they should never be called.
UnitConv()
TempTrack()
HeartRateMon()
Hydration()

