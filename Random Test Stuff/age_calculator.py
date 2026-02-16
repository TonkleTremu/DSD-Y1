from datetime import datetime

today = datetime.now()
print(today.strftime("%d/%m/%Y"))
birth_year = input("What is your birth year? (DD/MM/YYYY)\n").split("/")
birth_year = datetime(int(birth_year[2]), int(birth_year[1]), int(birth_year[0]))
age = today.year-birth_year.year
if(today.month < birth_year.month):
    age -= 1
print(f"So, you are {age}?")
next_bday = datetime(today.year, birth_year.month, birth_year.day)
if(today > next_bday):
    next_bday = datetime(today.year+1, birth_year.month, birth_year.day)
    next_bday_days = next_bday - today
    print(today, next_bday)
else:
    next_bday_days = next_bday - today
print(f"There are {next_bday_days.days} days until your next birthday!")