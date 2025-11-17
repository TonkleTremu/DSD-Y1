import FitnessCentreAccess
import MedSafetyRule
import SleepTrack
    
def MainMenu():
    '''The main menu that is loaded when the program starts, allowing you to access all parts of the program.'''
    Choix = int(input("1. Medication Safety Rule\n2. Fitness Centre Access\n3. Sleep Tracker Alert\n"))
    if(Choix == 1):
        MedSafetyRule.Run()
    elif(Choix == 2):
        FitnessCentreAccess.Run()
    elif(Choix == 3):
        SleepTrack.Run()
    else:
        print("NUMBERS FROM 1-3!!!")
    MainMenu()

MainMenu()