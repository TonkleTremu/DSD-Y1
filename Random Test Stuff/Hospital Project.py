YOUTHDISCOUNT = 0.9 # A constant multiplier for the discount for under 18s.

def Bill():
    '''Calculates a patient's bill, using factors such as age, and identifies whether they can use a payment plan or need to pay upfront.'''
    Name = input("What is the patient's name?\n")
    Age = int(input("What is the patient's age?\n"))
    BillAmount = float(input("What is the bill's cost? (before VAT)\n"))
    BillAmount *= 1.2
    if(Age < 18): # Identifies if a patient gets a youth discount.
        print(f"The patient is under 18, so a discount of {(1-YOUTHDISCOUNT)*100:.2f}% off is applied.")
        BillAmount *= YOUTHDISCOUNT
    if(BillAmount > 1000): # Identifies if a patient can use a payment plan or not.
        print(f"The patient {Name} is to pay a total of £{BillAmount:.2f} for their treatment. Since it is over £1,000, they may choose to pay for it over the course of a year.")
    else:
        print(f"The patient {Name} is to pay a total of £{BillAmount:.2f} for their treatment.")

Bill()