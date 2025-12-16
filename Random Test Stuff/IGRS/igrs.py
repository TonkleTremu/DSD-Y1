import igrslib as lib

toys = {
    ""
}

def getUserInformation():
    name = input("Enter child's name: ")
    while ageValid == False:
        age = input("Enter child's age: ")
        ageValid, age = lib.checkInt(age)
    