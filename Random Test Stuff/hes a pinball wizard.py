machines = ["Pinball Wizard", "Dance Floor X", "Retro Racer", "Alien Blaster"] 
categories = ["Pinball", "Rhythm", "Racing", "Shooter"] 
status = ["Working", "Working", "Needs Service", "Working"] 

def MainMenu(machines, categories, status): # The main menu where you choose what to do.
    Choix = input("1. View all machines.\n2. Add machine.\n3. Update machine status.\n4. Filter by category.\n")
    if(Choix == "1"): # Views all machines.
        for x in machines:
            print(f"{machines.index(x)+1}. {x}")
    elif(Choix == "2"): # Adds a new machine, category and status to the relevant lists.
        NewMach = input("What is the machine's name?\n")
        Category = input("What is the machine's category?\n")
        Status = input("What is the machine's status?\n")
        if(NewMach != "" and Category != "" and Status != ""):
            machines.append(NewMach)
            categories.append(Category)
            status.append(Status)
        else:
            print("All fields need to contain data.")
    elif(Choix == "3"): # Updates a machine's status.
        print("Which machine's status should be updated?\n")
        for x in machines:
            print(f"{machines.index(x)+1}. {x}")
        OrdChoix = int(input())-1
        NewStatus = input("What should the new status be?\n")
        status[OrdChoix] = NewStatus
        print(f"Status updated to {NewStatus}.")
    elif(Choix == "4"):
        ChosenCategory = input("What should the category be?\n")
        FilteredList = []
        for x in machines:
            if(categories[x] == ChosenCategory):
                FilteredList += x
        for x in FilteredList:
            print(f"{FilteredList.index(x)+1}. {x}")

    else:
        print("Try again.")
    MainMenu(machines, categories, status)
        
        
MainMenu(machines, categories, status)