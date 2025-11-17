def EnergyTracker(): # Tracks an individual's 'level of energy' throughout a day. No clue what the measurement is here.
    EnergyLevels = []
    while(len(EnergyLevels) < 5):
        EnergyLevels.append(int(input("What is your energy level right now? (from 1-10, where 10 is most energy)\n")))
    print(f"Your energy levels today were: {str(EnergyLevels).replace("[", "").replace("]", "")}. In the morning, you were at {EnergyLevels[0]} iotas of energy, at midday you had {EnergyLevels[int(len(EnergyLevels)/2)]} motes of energy, and at the end of the day you had {EnergyLevels[-1]} magicules of energy.") # Alex keeps berating me for having long lines of code, so I'm adding this comment to make line 5 even longer.

def UsernameTracker(): # Tracks a list of usernames. Literally just reused code from EnergyTracker() but I renamed the symbols.
    Usernames = []
    while(True):
        Usernames.append(input("Add another username (type 'stop' to stop):\n"))
        if(Usernames[-1].lower() == "stop"):
            Usernames.pop(-1)
            break
    print(f"The usernames are: {str(Usernames).replace("[", "").replace("]", "").replace("'", "")}. The first in the list is {Usernames[0]}, the middle is {Usernames[int(len(Usernames)/2)]} and the last username is {Usernames[-1]}.")

def StepCount(): # Same as UsernameTracker() but with steps instead of names.
    StepCounts = []
    while(len(StepCounts) < 7):
        StepCounts.append(int(input("What is your step count for today?\n")))
    print(f"Your step counts for this week were: {str(StepCounts).replace("[", "").replace("]", "")}. On the first day you had {StepCounts[0]} steps, on the middle day you had {StepCounts[int(len(StepCounts)/2)]} steps, and at the end of the week you had {StepCounts[-1]} steps.")

# He didn't say we needed to make a menu, so...
EnergyTracker()
UsernameTracker()
StepCount()