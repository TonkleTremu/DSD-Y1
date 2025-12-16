import csv

def checkInt(num):
    try:
        num = int(num)
        return True, num
    except:
        return False, 0