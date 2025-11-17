def Run():
    '''Sends an alert if you tell the program that you are awake and your heart rate is over 100. Why? 'Tis a mystery.'''
    Asleep = input("Are you asleep? (T/F)\n")
    HeartRate = float(input("What is your heart rate?\n"))
    if(HeartRate > 100 and Asleep == "F"):
        print("Alert!")