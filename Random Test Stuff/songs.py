Songs = []

for x in range(1,6): # Creates a list of five, user-inputted songs.
    Songs.append(input(f"What is your #{x} song?\n"))
print(Songs)

def MainMenu(): # Where all the business goes down.
    Choix = input("1. Display list.\n2. Add new song.\n3. Remove a song.\n4. Display list alphabetically.\n") # Asks user for their choice.
    if(Choix == "1"): # Displays the list in order of oldest input to newest input.
        DisplayedList = ""
        for x in Songs:
            DisplayedList += f"#{Songs.index(x)+1}: {x}\n"
        print(DisplayedList)
        print(f"There are {len(Songs)} songs in the list.\n")
    if(Choix == "2"): # Adds a new song to the last place in the list.
        Songs.append(input("What is the new song?\n"))
    if(Choix == "3"): # Removes a song from the list.
        Songs.remove(input("What song should be exalted?\n"))
    if(Choix == "4"): # Displays the list, sorted alphabetically.
        Temp = []
        Temp += Songs
        Temp.sort()
        print(Temp)
        DisplayedList = ""
        for x in Temp:
            DisplayedList += f"{x}\n"
        print(DisplayedList)
    else: # Seriously, typing a number from 1-4, how difficult is that?
        print("1-4, not that difficult.")
    MainMenu()
MainMenu()