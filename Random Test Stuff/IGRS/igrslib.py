import csv

FILENAME = "children.csv"

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
                print(line)

CsvToJson()