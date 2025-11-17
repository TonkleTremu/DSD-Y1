LOGINS = {"Miguel":["MyPassword123", 573489.24],"Miguel2":["MySecurePassword!", 820.23],"Alex":["&8dKK3@'", 10.42]}

def Login():
    '''Attempts to login the user with a provided name and password.'''
    Username = input("What is your username?\n")
    try:
        LOGINS[Username]
    except:
        print("Username not found.")
        Login()
    Password = input("What is your password?\n")
    if(LOGINS[Username][0] == Password):
        print("Login successful!")
        MainMenu(Username)
    else:
        print("Incorrect password! Have you checked you've used the correct capitalisation?")
        Login()
    
def MainMenu(Username):
    '''The main menu, where you can do all acccount-related stuff.'''
    Choix = input("What would you like to do?\n1. View bank details.\n2. Add/Withdraw money from account.\n3. Sign out.")
    if(Choix == "1"):
        print(f"You have £{LOGINS[Username][1]:.2f} in your account.")
        MainMenu(Username)
    elif(Choix == "2"):
        AddBal = float(input("How much do you want to deposit/withdraw to your account? (use negative numbers to withdraw)\n£"))
        LOGINS[Username][1] += AddBal
        print(f"You now have £{LOGINS[Username][1]:.2f} in your account.")
        MainMenu(Username)
    elif(Choix == "3"):
        Login()
    else:
        print("Please enter a number from 1-3.")
        MainMenu(Username)

    
Login()