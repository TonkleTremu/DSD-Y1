Machines = {"Pinball Wizard": {"Category": "Pinball", "Status": "Working"}, "Retro Racer": {"Category": "Racing", "Status": "Needs Service"}} # A nested dictionary in the format MachineName: {Category, Status}

def MainMenu(): # The main menu where you choose what to do.
    Choix = input("1. View all machines.\n2. Add machine.\n3. Update machine status.\n4. Remove a machine.\n5. Display all 'Out of Order' machines.\n") # The user's choice for what the program will do next. 'Choix' is used to prevent conflicts with 'Choice', which is used quite often.
    if(Choix == "1"): # Views all machines.
        print("-----------------\n")
        for x in Machines: # Prints each machine, its category and status in a nice format.
            print(f"{x}\nCategory: {Machines[x]["Category"]}\nStatus: {Machines[x]["Status"]}\n\n-----------------\n")
    elif(Choix == "2"): # Add a machine.
        NewMachine = input("What is the new machine's name?\n")
        NewCategory = input("What is the machine's category?\n")
        NewStatus = input("What is the machine's status?\n")
        Machines[NewMachine] = {"Category": NewCategory, "Status": NewStatus}
    elif(Choix == "3"): # Updates a machine's status.
        Machine = input("What is the machine's name?\n")
        NewStatus = input("What is the machine's new status?\n")
        Machines[Machine]["Status"] = NewStatus
    elif(Choix == "4"): # Remove a machine from the dictionary.
        Machine = input("What is the machine's name?\n")
        Machines.pop(Machine)
    elif(Choix == "5"): # Displays all "out of order" machines.
        OutOfOrder = 0
        for x in Machines:
            if(Machines[x]["Status"] == "Out of Order"):
                OutOfOrder += 1
                print(f"{x} is out of order.")
        print(f"There are {OutOfOrder} machines out of order.")
    MainMenu() # Calls itself - much prettier than a while-true loop.
MainMenu() # Boots the program.