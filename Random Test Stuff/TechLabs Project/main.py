import json

def InitialSetup():
    '''Set up how many desks exist in each room, how many are available and what people are working in them.'''
    try:
        f = open("rooms.json", "x") # Creates the file, then immediately closes it.
        f.close()
    except:
        print("Does Python have write permissions in this directory?")
    keepgoing = True
    while(keepgoing):
        choice = input("Would you like to make another room? (Y/N)\n")
        if(choice[0].lower() == "n"):
            keepgoing = False
        else:
            ChangeRoom()

def ChangeRoom():
    '''Allows you to add/delete a room, or change the number of desks.'''
    with open("rooms.json", "r") as rooms:
        rooms_dict = json.loads(rooms.read())
        choice = input("Would you like to add, delete or change a room? (A/D/C)\n")
        # Adding a new one.
        if(choice[0].lower() == "a"):
            # Gets the user inputs. If they are invalid, an error message shows and they gotta re-do it.
            invalid_input = True
            while(invalid_input):
                try:
                    new_room_name = input("What should the new room be called?\n")
                    if(new_room_name in rooms_dict):
                        raise(ValueError)
                    else:
                        invalid_input = False
                except:
                    print("That room already exists. Did you mean to change or delete it instead?")
            invalid_input = True
            while(invalid_input):
                try:
                    new_room_desks = int(input("How many desks does the room have?\n"))
                    if(new_room_desks <= 0):
                        raise(ValueError)
                    else:
                        invalid_input = False
                except:
                    print("That is not a whole, positive number! (Zero is also invalid.)")

            # Sets the new room up to be able to add to the file.
            new_room_inner_dict = {}
            for x in range(new_room_desks):
                new_room_inner_dict.update({x+1: "free"})
            rooms_dict.update({new_room_name: new_room_inner_dict})
            new_rooms = json.dumps(rooms_dict)

        # Delete an existing one.
        elif(choice[0].lower() == "d"):
            print("Existing rooms:")
            for room in rooms_dict:
                print(room)
            invalid_input = True
            while(invalid_input):
                try:
                    doomed_room = input("Which room should be deleted?\n")
                    if(not(doomed_room in rooms_dict)):
                        raise(ValueError)
                    else:
                        invalid_input = False
                except:
                    print("That room doesn't exist yet. Did you mean to add it instead?")
            decision = input(f'To clarify, you would like to delete room "{doomed_room}" Enter "Y" to continue, or any other character to stop.\n')
            if(decision.lower() == "y"):
                del rooms_dict[doomed_room]
            
        # Change the room count for an existing one.
        elif(choice[0].lower() == "c"):
            # Gets the user inputs. If they are invalid, an error message shows and they gotta re-do it.
            invalid_input = True
            while(invalid_input):
                try:
                    old_room_name = input("What room should be changed?\n")
                    new_room_name = input("What should its name be changed to? (Leave blank to keep current name.)\n")
                    if(new_room_name in rooms_dict or old_room_name not in rooms_dict):
                        raise(ValueError)
                    else:
                        invalid_input = False
                except:
                    print("Either the new name was already taken, or the old name didn't exist.")
            invalid_input = True
            while(invalid_input):
                try:
                    new_room_desks = int(input("How many desks does the room have? (Leave 0 to keep current desk count.)\n"))
                    if(new_room_desks < 0):
                        raise(ValueError)
                    else:
                        invalid_input = False
                except:
                    print("That is not a whole, positive number! (Zero is also invalid.)")
            if(new_room_name == "" and new_room_desks == 0):
                print("There is nothing to change!")
            elif(new_room_name == ""): # Only changes desk count.
                new_room_name = old_room_name
            old_room_count = 0
            for x in rooms_dict[old_room_name]:
                old_room_count += 1
            if(new_room_desks == 0):
                new_room_desks = old_room_count
            else:
                distance = new_room_desks-old_room_count
                
                # Sets the new room up to be able to add to the file.
                new_room_inner_dict = rooms_dict[old_room_name]
                if(distance > 0): # If more desks are added.
                    for x in range(distance):
                        new_room_inner_dict.update({x+distance+1: "free"})
                elif(distance < 0): # If desks are removed.
                    print("Desks cannot be removed. To do so, delete the room and make another with the same name.")

            del rooms_dict[old_room_name]
            rooms_dict.update({new_room_name: new_room_inner_dict})
            new_rooms = json.dumps(rooms_dict)
            
    with open("rooms.json", "w") as rooms:
        rooms.write(new_rooms)


def AssignEmployee():
    '''Puts an employee in a free desk.'''
    with open("rooms.json", "r") as rooms:
        rooms_dict = json.loads(rooms.read())
        print("Rooms:")
        for room in rooms_dict:
            print(room)

        add_to_room = input("Which room should the employee be added to?\n")
        employee_name = input("What is the employee's name? (Leave blank to un-assign a desk.)\n")
        if(employee_name == ""):
            employee_name = "free"
        print("Desks:")
        for desks in rooms_dict[add_to_room]:
            print(f"{desks} - {rooms_dict[add_to_room][desks]}")
        invalid_input = True
        while(invalid_input):
            try:
                desk = int(input("Which desk should the employee be added to?\n"))
                if(desk <= 0 or desk > len(rooms_dict[add_to_room])):
                    raise(ValueError)
                else:
                    invalid_input = False
            except:
                print(f"That is not a whole, positive number within the correct range (there are only {len(rooms_dict[add_to_room])} rooms)! (Zero is also invalid.)")

        # Sets the new room up to be able to add to the file.
        new_room_inner_dict = rooms_dict[add_to_room]
        new_room_inner_dict.update({str(desk): employee_name})
        rooms_dict.update({add_to_room: new_room_inner_dict})
        new_rooms = json.dumps(rooms_dict)
    with open("rooms.json", "w") as rooms:
        rooms.write(new_rooms)
        

def CheckFreeRooms():
    '''Checks every room to see if any of them are completely free.'''
    with open("rooms.json", "r") as rooms:
        rooms_dict = json.loads(rooms.read())
        for room in rooms_dict:
            all_free = True
            for desk in rooms_dict[room]:
                if rooms_dict[room][desk] != "free":
                    all_free = False
            if(all_free):
                print(f"Room {room} is free!")

def MainMenu():
    choix = input("What would you like to do?\n1. Change, Delete or Add a Room\n2. Assign an employee to a desk.\n3. Check for free rooms.\n")
    if(choix == "1"):
        ChangeRoom()
    elif(choix == "2"):
        AssignEmployee()
    elif(choix == "3"):
        CheckFreeRooms()
    else:
        print("That choice is invalid.")
    MainMenu()

try:
    with open("rooms.json") as rooms:
        print("File loaded successfully!")
        MainMenu()
except:
    print("File not found. You will be directed to the setup page.")
    InitialSetup()
    MainMenu()