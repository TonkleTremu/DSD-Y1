Games = ["Bastille Jour", "Bastille Jour II: Les Jeux Des Les Dieux", "Bastille Jour III: Le Guerre De Le Soleil", "9801"] # A list of company games. English translations: Bastille Day, Bastille Day 2: The Games of the Gods, Bastille Day 3: The War of the Sun, 9801.
Favourite = "None"
Played = []

def MainMenu(Games, Favourite, Played): # The main menu where you choose what to do.
    Choix = input("1. Favourite a game.\n2. Mark a game as played.\n3. Remove a game as played.\n")
    if(Choix == "1"): # Marks a game as a favourite
        print(f"Mark which game as favourite? (your current favourite is {Favourite})\n")
        for x in Games:
            print(f"{Games.index(x)+1}. {x}")
        Favourite = Games[int(input())-1]
        print(f"Your favourite game has been set to: {Favourite}")
    elif(Choix == "2"): # Marks a game as played
        print(f"Mark which game as played?\n")
        for x in Games:
            print(f"{Games.index(x)+1}. {x}")
        JeuChoix = int(input())
        if(JeuChoix in Played):
            print("That game has already been marked as played.\n")
        else:
            Played.append(JeuChoix)
    elif(Choix == "3"): # Unmarks a game as played.
        print(f"Mark which game as played?\n")
        for x in Games:
            print(f"{Games.index(x)+1}. {x}")
        JeuChoix = int(input())
        if(JeuChoix in Played):
            Played.pop(Played.index(JeuChoix))
        else:
            print("That game has not been marked as played.\n")
    else:
        print("Try again.")
    MainMenu(Games, Favourite, Played)
        
        
MainMenu(Games, Favourite, Played)