import igrslib as lib

toys = {
    "Plush toy": 0,
    "Football": 6,
    "Lego": 4,
    "Magic set": 5,
    "Basketball": 6,
    "Robot toy": 4,
    "Doll": 0,
    "Story book": 0,
    "Race car": 4,
    "Art set": 5,
    "Science kit": 5,
    "Drawing kit": 4,
    "Puzzle": 6,
    "Keyboard": 6,
    "Building blocks": 0
}

def getUserInformation():
    name = input("Enter child's name: ")

    returnedNames = lib.SearchCsv(name)
    for child in returnedNames:
        print(f"\n Child ID: {child[0]} \n Child Name: {child[1]} \n Child's Interests: {child[2]} \n Suggested Toy: {child[3]}")