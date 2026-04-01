major_faults = int(input("How many major faults were detected?\n"))
minor_faults = int(input("How many minor faults were detected?\n"))

points = major_faults*5 + minor_faults*2

if(points > 7):
	print("Fail")
else:
	print("Pass")
