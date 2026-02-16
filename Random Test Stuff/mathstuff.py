import math

num = input("Pick a number.\n")
if("i" in num):
    usesimaginary = True
    if(num != "inf"):
        num = num.replace("i", "")
    else:
        usesimaginary = False
    if(num == ""):
        num = "i"
    else:
        num = float(num)
else:
    usesimaginary = False
    num = float(num)
try:
    print(f"Square Root: {round(math.sqrt(num), 2)}")
except:
    print("Square Root not calculable - likely caused by a negative, complex or imaginary input.")
if(usesimaginary):
    if(num == "i"):
        print("Square: -1")
    else:
        print(f"Square: {round(num*num*-1, 2)}")
else:
    print(f"Square: {round(num*num, 2)}")
try:
    print(f"Rounding:\nUp: {round(num)}\nDown: {math.floor(num)}")
except:
    print("Cannot be rounded - did you input a complex or imaginary number?")
if(usesimaginary):
    if(num == "i"):
        print(f"If it were a circle with radius {num}, its area would be {round(math.pi * -1, 2)}")
    else:
        print(f"If it were a circle with radius {num}, its area would be {round(math.pi * num*num*-1, 2)}")
else:
    print(f"If it were a circle with radius {num}, its area would be {round(math.pi * num*num, 2)}")