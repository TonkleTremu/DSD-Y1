def Run():
    '''Decides whether someone is intensive enough to access the "Intensive Zone."'''
    Age = int(input("What is the person's age?\n"))
    Clearance = input("Does the person have medical clearance? (T/F)\n")
    if(Clearance == "T" or Age > 18):
        print('They can access the "Intensive Zone."')
    else:
        print("They are not intense enough.")
