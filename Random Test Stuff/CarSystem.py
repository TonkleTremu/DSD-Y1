HiredDays = int(input("How many days was the car hired for?\n"))
while(HiredDays <= 0):
    HiredDays = int(input("How many days was the car hired for? (cannot be zero)\n"))
MileageStart = float(input("What was the car's initial mileage?\n"))
MileageEnd = float(input("What was the car's end mileage?\n"))
MilesDriven = MileageEnd - MileageStart
Charge = (20 * HiredDays) + (0.05*MilesDriven)
print(f"The total charge is {Charge}")