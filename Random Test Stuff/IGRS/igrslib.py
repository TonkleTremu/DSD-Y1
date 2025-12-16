import csv

FILENAME = "IGRS/children.csv"

ChildrenInterests = {}

def checkInt(num):
    try:
        num = int(num)
        return True, num
    except:
        return False, 0
    
def CsvToJson():
    with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            for line in reader:
                ChildrenInterests.update({line[0]: {"Name": line[1], "Interests": [line[6], line[7]], "Toy": line[4]}})
            ChildrenInterests.pop("child_id")
            print(ChildrenInterests)

def SearchCsv(name): # Returns a list of lists [{ID: {Name, Interests, Toy}}, {ID: {Name, Interests, Toy}}]
    try:
        ChosenChildren = []
        for x in ChildrenInterests:
             if(ChildrenInterests[x]["Name"] == name.capitalize()):
                  ChosenChildren.append({x: ChildrenInterests[x]})
        return(ChosenChildren)
    except:
         return("No children found! Santa can't see them while they're sleeping, so he knows they're awake...")

CsvToJson()
print(SearchCsv(input()))