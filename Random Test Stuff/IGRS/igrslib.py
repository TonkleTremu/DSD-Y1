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
                ChildrenInterests.update({"ID": line[0], "Interests": [line[6], line[7]], "Toy": line[4]})
            print(ChildrenInterests)

CsvToJson()