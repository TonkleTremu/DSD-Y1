def typations():
    x = 25
    y = 3.14
    print(type(x), type(y))

def ThisThingy():
    a = 10
    b = 3
    print(a/b)
    print(type(a/b))
    print(a//b)
    print(type(a//b))
    print(a*2.5)
    print(type(a*2.5))

def Average(x,y,z):
    print((x+y+z)/3)
#Average(float(input("What is the first number?\n")),float(input("What is the second number?\n")),float(input("What is the third number?\n")))

#ThisThingy()

def OrderMenu():
    TypeFood = input("Would you like breakfast, lunch or a dessert?\n")
    if(TypeFood[0].lower() == "b"):
        ChosenFood = input("We serve:\n1) All-Day Breakfast\n2) Croissant\n3) Rice Krispies\n")
        if(ChosenFood == "1"):
            print("So you have chosen an All-Day Breakfast.")
            aChosenFood="All-Day Breakfast"
        elif(ChosenFood == "2"):
            print("So you have chosen a Crossaint.")
            aChosenFood="Croissant"
        elif(ChosenFood == "3"):
            print("So you have chosen Rice Krispies.")
            aChosenFood="Rice Krispies"
        else:
            print("Please choose the number correspondant to the desired food.")
    elif(TypeFood[0].lower() == "l"):
        ChosenFood = input("We serve:\n1) All-Day Breakfast\n2) Chicken Sandwich\n3) Hamburger\n")
        if(ChosenFood == "1"):
            print("So you have chosen an All-Day Breakfast.")
            aChosenFood="All-Day Breakfast"
        elif(ChosenFood == "2"):
            print("So you have chosen a Chicken Sandwich.")
            aChosenFood="Chicken Sandwich"
        elif(ChosenFood == "3"):
            print("So you have chosen a Hamburger.")
            aChosenFood="Hamburger"
        else:
            print("Please choose the number correspondant to the desired food.")
    elif(TypeFood[0].lower() == "d"):
        ChosenFood = input("We serve:\n1) Death (our specialty ice cream, with 10x your daily calorie intake. You get it free if you manage to finish the whole thing.d)\n2) Rocky Road Sundae\n3) Donut\n")
        if(ChosenFood == "1"):
            print("So you have chosen Death.")
            aChosenFood="Death"
        elif(ChosenFood == "2"):
            print("So you have chosen a Rocky Road Sundae.")
            aChosenFood="Rocky Road Sundae"
        elif(ChosenFood == "3"):
            print("So you have chosen a Donut.")
            aChosenFood="Donut"
        else:
            print("Please choose the number correspondant to the desired food.")
    return(aChosenFood)

RollingOrder = ""
FoodFlag = True
while(FoodFlag):
    RollingOrder += OrderMenu() + ", "
    print("Your order is " + RollingOrder)