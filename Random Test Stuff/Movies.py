Movies = ["Last Christmas", "I gave you my heart", "But the very next day...", "You Gave It Away", "This Year"]

def MainMenu(): # Where all the business goes down.
    Choix = input("1. Display list.\n2. Add new movie.\n3. Remove a movie.\n4. Find a movie.\n5. Exit.\n") # Asks user for their choice.
    if(Choix == "1"): # Displays the list in order of oldest input to newest input.
        DisplayedList = ""
        for x in Movies:
            DisplayedList += f"#{Movies.index(x)+1}: {x}\n"
        print(DisplayedList)
        print(f"There are {len(Movies)} movies in the list.\n")
    elif(Choix == "2"): # Adds a new movie to the last place in the list.
        Movies.append(input("What is the new movie?\n"))
    elif(Choix == "3"): # Removes a movie from the list.
        Movies.remove(input("What movie should be exalted?\n"))
    elif(Choix == "4"): # Finds a movie in the list.
        FindMovie = input("What movie should be found?\n")
        try:
            FoundMovie = Movies.index(FindMovie)
            print(f"{FindMovie} is at location {FoundMovie+1} in the list.")
        except:
            print(f"{FindMovie} couldn't be found.")
    elif(Choix == "5"):
        print("BYEEEEEEEEEEE!")
        exit()
    else: # Seriously, typing a number from 1-5, how difficult is that?
        print("1-5, not that difficult.")
    MainMenu()
MainMenu()