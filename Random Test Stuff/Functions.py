def MyFunction(n1,n2):
    print(f"The result is {n1*n2}")

def Stats(n1,n2,n3):
    print(f"Hello {n1}! You currently have £{n2} in your account, with £{n3} pending, making for a total of £{n2+n3}")

def Maths(N1=0,N2=0):
    print(N1-N2)

def Boot():
    Num1 = float(input("Enter a number:\n"))
    Num2 = float(input("Enter another number:\n"))
    Maths(N2=Num2,N1=Num1)

    Num1 = int(input("Enter a number:\n"))
    Num2 = int(input("Enter another number:\n"))
    MyFunction(Num1,Num2)

    Name = input("What is your name?\n")
    Bal = float(input("How much money is in your account?\n"))
    Pen = float(input("How much money is pending to your account?\n"))
    Stats(Name,Bal,Pen)

Boot()