def Run():
    '''Decides if an unknown substance is safe to give to somebody.'''
    Age = int(input("What is the patient's age?\n"))
    Weight = float(input("What is the patient's weight? (kg)\n"))
    if(Age > 12 and Weight > 40):
        print("Safe to give.")
    else:
        print("Not safe.")
