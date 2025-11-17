CF = input("Converting from Celcius or Farenheit?\n")
Val = float(input("What is the value?\n"))
if(CF[0].upper()=="C"):
    print(f"{(Val*1.8)+32}F")
elif(CF[0].upper()=="F"):
    print(f"{(Val-32) * (5/9)}")