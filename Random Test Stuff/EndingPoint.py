def PercentGoal(steps, goal=10000):
    '''Calculates how close someone is to their step goal. Rounds the percentage to 2 d.p.'''
    percent_of_goal = (steps/goal)*100
    remaining_steps = goal-steps
    if(percent_of_goal > 100):
        percent_of_goal = 100
    if(remaining_steps > goal):
        remaining_steps = goal
    print(f"You are {percent_of_goal:.2f}% of the way to your goal, and have {remaining_steps} steps left.")
    return(f"{percent_of_goal:.2f}")

def WeightCheck():
    '''Calculates the user's BMI, then tells them if they are obese, healthy, etc.'''
    weight_kg = float(input("What is your weight (kg)?\n"))
    height_m = float(input("What is your height (m)?\n"))
    bmi = weight_kg/(height_m**2)
    if(bmi <= 18.5):
        print("Underweight.")
    elif(bmi <= 25):
        print("Healthy.")
    elif(bmi <= 30):
        print("Overweight.")
    else:
        print("Obese.")

def FlagUser(daily_screen_minutes, night_screen_minutes, steps): # This was flag_user since that is what they asked, but FlagUser fits the naming conventions.
    '''Determines whether a user is being unhealthy or not.'''
    if((daily_screen_minutes > 240 and steps < 5000) or night_screen_minutes > 60):
        return(True)
    else:
        return(False)

def HydrationStreak(water_ml):
    '''Gives points to a hydration meter, to 'gamify' it.'''
    points = 5*(water_ml // 2000) + (water_ml // 250)
    return(points)

def EligibleForClass():
    '''Checks if someone is eligible for a free class, using certain factors.'''
    age = int(input("What is your age?\n"))
    LowIncome = input("Are you a registered low-income particpant? (Y/N)")
    FreeClass = input("Have you received a free class in the last 30 days? (Y/N)")
    if(CheckEligibility(age, LowIncome, FreeClass)):
        print("You are eligible!")
    else:
        print("Unfortunately, you are not eligible...")
    return(CheckEligibility(age, LowIncome, FreeClass))

def CheckEligibility(age, low_income, days_since_last_free):
    '''Checks if someone is eligible for a free class.'''
    if((16 <= age <= 25 or low_income.lower() == "y") and days_since_last_free.lower() == "n"):
        return(True)
    else:
        return(False)
    
def WeeklyTier(steps, water_ml):
    '''Gives a tier to someone's habits, to 'gamify' it.'''
    points = (steps // 1000) * 2 + (water_ml // 500)
    if(points <= 19):
        return("Bronze")
    elif(points <= 39):
        return("Silver")
    else:
        return("Gold")
    
def SafeAverageMinutes(total_minutes, sessions):
    '''Calculates someone's average minutes per session.'''
    if(sessions == 0):
        return(0)
    else:
        average = round(total_minutes / sessions, 1)
        return(average)

def SummaryLine(steps, water_ml, screen_mins):
    '''Gives a summary of several of the other functions.'''
    percent = PercentGoal(steps)
    points = HydrationStreak(water_ml)
    if(screen_mins <= 240):
        screen_label = "OK"
    else:
        screen_label = "High"
    print(f"Steps: {steps} ({percent}%), Water: {water_ml}ml (+{points}pts), Screen: {screen_mins} mins - {screen_label}")

def MainMenu():
    '''Allows you to actually, y'know, use the other functions.'''
    choix = int(input("1. Percentage to step goal\n2. Check BMI\n3. Flag user\n4. Hydration Streak\n5. Check free class eligibility\n6. Check tier\n7. Check average minutes\n8. Summary\n"))
    if(choix == 1):
        PercentGoal(int(input("How many steps?\n")))
    elif(choix == 2):
        WeightCheck()
    elif(choix == 3):
        print(FlagUser(float(input("What are your daily screen minutes?\n")), float(input("What are your night screen minutes?\n")), int(input("How many steps?\n"))))
    elif(choix == 4):
        print(HydrationStreak(float(input("How many ml of water?\n"))), "points.")
    elif(choix == 5):
        EligibleForClass()
    elif(choix == 6):
        print("Your tier is", WeeklyTier(int(input("What are your steps?\n")), int(input("What is your water intake?\n"))))
    elif(choix == 7):
        print("Your average is", SafeAverageMinutes(int(input("What are your total minutes?\n")), int(input("How many sessions have you taken?\n"))))
    elif(choix == 8):
        SummaryLine(int(input("What are your steps?\n")), int(input("What is your water intake?\n")), float(input("What are your daily screen minutes?\n")))
    else:
        print("ONE TO EIGHT!")
    MainMenu()

MainMenu()