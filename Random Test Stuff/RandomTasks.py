def AreaCalc(): 
    '''Calculates the area of an irregular, 4-sided shape wherein the sides meet at perpendicular joints.'''
    Height = float(input("What is the rectangle's height?\n"))
    Width = float(input("What is the rectangle's width?\n"))
    Area = Height * Width
    print(f"The area of the rectangle is {Area:.2f} (to 2 d.p.)")

def MinutesToHours(): 
    '''Converts plain minutes into hours and minutes.'''
    Minutes = int(input("How many minutes do you have?\n"))
    Hours = Minutes // 60
    Minutes %= 60
    if(Hours == 1):
        print(f"In hours and minutes, that is {Hours} hour and {Minutes}mins")
    else:
        print(f"In hours and minutes, that is {Hours}hrs and {Minutes}mins")

def VatCalc(): 
    '''Multiplies a number by 1.2. Also known as calculating VAT.'''
    StartBillCost = float(input("How much does the bill cost before VAT?\n£"))
    print(f"After VAT, the bill costs £{StartBillCost*1.2:.2f}")

#AreaCalc()
#MinutesToHours()
#VatCalc()