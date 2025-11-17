String = "String"
Int = 1
Float = 1.3
Boolean = True

print(f"{String} is an example of a string. {Int} is an integer. {Float} is a float, and {Boolean} is a boolean.")

Name = input("What is your name?\n")
FavNumOneTen = int(input("What is your favourite whole number from 1-10?\n"))
if(FavNumOneTen > 10 or FavNumOneTen < 1):
    print("I ask of you one thing. And you answer incorrectly.")
    exit()
FavNum = float(input("What is your favourite number out of anything?\n"))
HonestyAsk = input("Did you answer honestly?\n")
if(HonestyAsk[0].lower() == "y"):
    print(f"So, your name is {Name}, your favourite number from 1-10 is {FavNumOneTen} and your favourite number in general is {FavNum}")
elif(HonestyAsk[0].lower() == "n"):
    print(f"Why not, {Name}? If that even is your real name...")
else:
    print("Wrong answer.")