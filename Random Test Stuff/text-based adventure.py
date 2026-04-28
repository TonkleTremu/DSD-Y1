import random

rooms = {
    "start": ["living"], 
    "living": ["start", "exit", "drawing"], 
    "drawing": ["treasure", "living"], 
    "treasure": ["monty", "drawing"], 
    "empty": ["exit"],
    "exit": ["living"]}

this_room = "start"
key = False

def MoveRoom(this_room, key):
    while(True):
        if(this_room == "monty"):
            safe_room = random.randint(1,3)
            choix1 = input("Before you are three doors. Two of which contain immediate death, and the other contains an exit. Will you pick room 1, 2, or 3?\n")
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
        else:
            print(f"You are currently in the {this_room} room. You can currently move to:")
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

while(True):
    this_room, key = MoveRoom(this_room, key)