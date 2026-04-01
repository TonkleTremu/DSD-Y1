is_valid_code = True

parcel_code = input("What is the parcel code?\n")

if(len(parcel_code) == 7 and parcel_code.isnumeric()):
    first_part = parcel_code[0:6]
    last_part = parcel_code[6:7]
    listed_nums = []

    for x in range(1,len(first_part)+1):
        listed_nums.append(x * int(first_part[x-1]))
        
    checksum = sum(listed_nums) % 10
    if(checksum == int(last_part)):
        print("Checks out!")
