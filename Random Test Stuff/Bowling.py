Bookings = {} # Uses a dictionary. ID number, Name, Day, Time, People
ValidDays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
MenuItems = ["coffee", "tea", "the ultimate cruncher supreme deluxe (for two)", "burger", "chicken burger", "boiled egg", "cheesy chips", "omelette", "the bowler's delight"] # I love ordering the ultimate cruncher supreme deluxe (for two)

def CheckValidTime(Time): # Checks whether a time falls under the 00:00 format. True is returned if it does NOT follow the format.
    try:
        TimeParts = Time.split(":")
        if(int(TimeParts[0]) > 23):
            return(True)
        elif(int(TimeParts[0]) < 0):
            return(True)
        elif(int(TimeParts[1]) > 59):
            return(True)
        elif(int(TimeParts[1]) < 0):
            return(True)
        else:
            return(False)
    except:
        return(True)

def CheckValidPeople(People): # Checks if a booking amount is an integer.
    try:
        H = int(People)
        return(False)
    except:
        return(True)

def NewBooking(): # Adds a new booking to "Bookings"
    Name = input("What is the name of the booking?\n")
    ChosenDay = ""
    while(not(ChosenDay in ValidDays)):
        ChosenDay = input("What day is the booking for? (please only enter a day of the week)\n").lower()
    Time = ""
    while(CheckValidTime(Time)):
        Time = input("What is the time for the booking? (please use the 23:59 format)\n")
    People = "Four"
    while(CheckValidPeople(People)):
        People = input("How many people is the booking for?\n")
    try:
        Bookings.update({max(Bookings.keys())+1: [Name, ChosenDay, Time, People]})
    except:
        Bookings.update({0: [Name, ChosenDay, Time, People]})
    Discount = 1
    if(int(People) > 4):
        Discount = 0.85
    Price = int(People) * Discount * 5
    print(f"Summary\n------------\nName: {Name}\nDay: {ChosenDay}\nTime: {Time}\nPeople: {People}\nPrice: £{Price:.2f}")

def CaféOrder(): # Allows people to place a café order.
    Order = []
    print("Menu:\n")
    for x in MenuItems:
        print(x.capitalize())
    print("------")
    Adding = ""
    while(not(Adding in MenuItems)):
        Adding = input("What would you like to order?\n").lower()
    while(Adding != "stop"):
        Order.append(Adding)
        Adding = ""
        print("Menu:")
        for x in MenuItems:
            print(x.capitalize())
        print("------")
        while(not(Adding in MenuItems or Adding == "stop")):
            Adding = input("To order another item, enter its name. Otherwise, type 'stop'.\n").lower()
    print(f"So, you have ordered: {str(Order).replace("[","").replace("]","").replace("'", "")}.")

def MainMenu():
    Choix = input("Would you like to book (1) or buy from the café (2)?")
    if(Choix == "1"):
        NewBooking()
    elif(Choix == "2"):
        CaféOrder()
    else:
        print("ONE OR TWO.")
    MainMenu()

MainMenu()