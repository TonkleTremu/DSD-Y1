import random

rooms = {
    "start": ["living"], 
    "living": ["start", "exit", "drawing"], 
    "drawing": ["treasure", "living"], 
    "treasure": ["monty", "conclusions"], 
    "empty": ["exit"],
    "exit": ["living"],
    "conclusions": ["treasure", "monty"]}

this_room = "start"
key = False
inconclusive = False

def CheckValidInt(num, des_num, banned_room):
    try:
        
        if(num == "1000"):
            return(False)
        num = int(num)
        if(num <= 0 or num > des_num or num == banned_room):
            raise(ValueError)
        else:
            return(False)
    except:
        return(True)

def MoveRoom(this_room, key, inconclusive):
    while(True):
        if(this_room == "monty"):
            safe_room = random.randint(1,3)
            choix1 = 0
            while(CheckValidInt(choix1, 3, 0)):
                choix1 = input("Before you are three doors. Two of which contain immediate death, and the other contains an exit. Will you pick room 1, 2, or 3?\n")
            if(choix1 == "1000"):
                choix1 = 0
                while(CheckValidInt(choix1, 1000, 0)):
                    choix1 = input("Monty knocks you unconcious. You awake in front of a thousand doors. Which number do you pick?\n")
                safe_room = random.randint(1,1000)
                if(choix1 == safe_room):
                    oth_room_valid = False
                    while(oth_room_valid == False):
                        other_room = random.randint(1,1000)
                        if(other_room != int(choix1)):
                            oth_room_valid = True
                else:
                    other_room = safe_room

                choix2 = 0
                while(CheckValidInt(choix2, 1000, 0)):
                    choix2 = input(f"Monty has opened every door except #{other_room}. You can either stick with your current room (#{choix1}), or swap to room #{other_room}. Choose well.\n")

                if(choix2 == str(safe_room)):
                    print("You picked the right room!")
                    this_room = "empty"
                else:
                    print("You failed! Starting over...")
                    this_room = "start"
                    key = False
            else:
                rem_room_valid = False
                while(rem_room_valid == False):
                    removed_room = random.randint(1,3)
                    if(removed_room != safe_room and removed_room != int(choix1)):
                        rem_room_valid = True

                oth_room_valid = False
                while(oth_room_valid == False):
                    other_room = random.randint(1,3)
                    if(other_room != int(choix1) and other_room != removed_room):
                        oth_room_valid = True

                choix2 = 0
                while(CheckValidInt(choix2, 3, removed_room)):
                    choix2 = input(f"Monty has opened door #{removed_room}. You can either stick with your current room (#{choix1}), or swap to room #{other_room}. Choose well.\n")

                if(choix2 == str(safe_room)):
                    print("You picked the right room!")
                    this_room = "empty"
                else:
                    print("You failed! Starting over...")
                    this_room = "start"
                    key = False
        elif(this_room == "exit" and key):
            print("You've won!")
            exit
        elif(this_room == "conclusions"):
            if(inconclusive == False):
                choix = input("There's a chasm between the treasure room and conclusions. Will you leap over it? (Y/N)\n")
                if(choix[0].lower() == "y"):
                    print("You jump to conclusions.")
                    inconclusive = True
                    this_room = "conclusions"
                elif(choix[0].lower() == "n"):
                    print("Yeah, probably best not to jump to conclusions...")
                    this_room = "treasure"
                else:
                    print("That's not a Y or an N.")
            else:
                print(f"You are currently in the concept of conclusions. You can move to these rooms:")
                for x in rooms[this_room]:
                    print(x)
                room_choice = input("Which room would you like to move to?\n")
                if(room_choice in rooms[this_room]):
                    if(room_choice == "treasure" and key == False):
                        print("You got a key!")
                        return(room_choice, True)
                    else:
                        return(room_choice, key)
                else:
                    print("That isn't a valid choice!")
        else:
            print(f"You are currently in the {this_room} room. You can currently move to:")
            for x in rooms[this_room]:
                print(x)
            room_choice = input("Which room would you like to move to?\n")
            if(room_choice in rooms[this_room]):
                if(room_choice == "treasure" and key == False):
                    print("You got a key!  ...but the way back just collapsed.")
                    return(room_choice, True)
                else:
                    return(room_choice, key)
            else:
                print("That isn't a valid choice!")

while(True):
    this_room, key = MoveRoom(this_room, key, inconclusive)