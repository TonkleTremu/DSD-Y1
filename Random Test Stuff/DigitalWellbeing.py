notifications = [34, 28, 55, 40, 60, 22, 18]
for x in range(0, len(notifications)): # Displays the values for each day.
    print(f"Day {x+1}: {notifications[x]}")
print(f"The highest day was day {notifications.index(max(notifications))}. The lowest was day {notifications.index(min(notifications))}, and the total was {sum(notifications)}.") # Displays highest, lowest and total notifications.
print(f"The average was {sum(notifications)/len(notifications):.2f}") # Average.
notifications.append(int(input("What is today's notification count?\n")))
for x in range(0, len(notifications)): # Displays the values for each day.
    print(f"Day {x+1}: {notifications[x]}")

notifications2 = [5, 188, 38, 10, 20, 39, 45, 46] # A whole bunch of stuff to compare the two lists. "Maxer", "Miner" and "Averager" decide which word should be used.
maxer = "first"
miner = "1"
averager = "first"

if(max(notifications) < max(notifications2)):
    maxer = "second"
if(min(notifications) > min(notifications2)):
    miner = "2"
if(sum(notifications)/len(notifications) < sum(notifications2)/len(notifications2)):
    averager = "second"
print(f"The user with the max notifications in a day was the {maxer} user. The one with the least in a single day was user {miner}, and the one with the most on average was the {averager} user.")