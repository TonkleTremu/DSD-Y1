Movies = {"Wonka": {"Time": "17:35", "Seats": 45}, "Dune 2": {"Time": "19:00", "Seats": 30}}

def MainMenu(): # The main menu where you choose what to do.
    Choix = input("1. View all movies.\n2. Add movie.\n3. Book tickets.\n4. Remove a movie.\n5. Display all sold out movies and average remaining seats.\n") # The user's choice for what the program will do next. 'Choix' is used to prevent conflicts with 'Choice', which is used quite often.
    if(Choix == "1"): # Views all movies.
        print("-----------------\n")
        for x in Movies: # Prints each movie, its time and available seats in a nice format.
            print(f"{x}\nTime: {Movies[x]["Time"]}\nSeats: {Movies[x]["Seats"]}\n\n-----------------\n")
    elif(Choix == "2"): # Add a movie.
        NewMovie = input("What is the new movie's name?\n")
        NewTime = input("What is the movie's timeslot?\n")
        NewSeats = input("What is the movie's seat count?\n")
        Movies[NewMovie] = {"Time": NewTime, "Seats": NewSeats}
    elif(Choix == "3"): # Books some tickets.
        Movie = input("What is the movie's name?\n")
        Tickets = int(input("How many tickets?\n"))
        if((Movies[Movie]["Seats"] - Tickets) >= 0):
            Movies[Movie]["Seats"] -= Tickets
            print("Tickets booked successfully.")
        else:
            print("Too many tickets would be booked, resulting in an over-booking.")
    elif(Choix == "4"): # Remove a movie from the dictionary.
        Movie = input("What is the movie's name?\n")
        Movies.pop(Movie)
    elif(Choix == "5"): # Displays all sold out movies.
        MovieCount = 0
        TotalSeats = 0
        for x in Movies:
            if(Movies[x]["Seats"] == 0):
                print(f"{x} is sold out.")
            MovieCount += 1
            TotalSeats += Movies[x]["Seats"]
        print(f"Average available seats is {TotalSeats/MovieCount:.0f}.")
    else:
        print("Try again.")
            
    MainMenu() # Calls itself - much prettier than a while-true loop.
MainMenu() # Boots the program.