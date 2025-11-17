def Bill():
    DaysStayed = int(input("How many days did they stay?\n"))
    ServiceCost = float(input("What is their service cost?\n"))
    MedCost = float(input("How much did their treatment cost?\n"))

    TotalCost = (DaysStayed*20 + ServiceCost + MedCost*1.25) * 1.2
    print(f"The total cost is {TotalCost}")