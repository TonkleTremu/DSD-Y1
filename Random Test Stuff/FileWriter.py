def WriteNewScore(): # Allows the user to add a new name and score to the system.
    name = input("What is your name?\n")
    score = input("What is your score?\n")
    try:
        score = int(score)
    except:
        WriteNewScore()
    with open("scores.txt", "a") as f:
        f.write(f"{name}: {score}\n")

def ReadScores(): # Allows the user to read all prior names and scores.
    with open("scores.txt", "r") as f:
        names = []
        scores = []
        for x in f:
            if(x == "\n"):
                pass
            else:
                print(x)
                x = x.split(": ")
                names.append(x[0])
                scores.append(x[1].replace("\n", ""))
        runninghighest = 0
        runningtotal = 0
        runningamount = 0
        for x in scores:
            try:
                if(int(x) > runninghighest):
                    runninghighest = int(x)
                runningtotal += x
                runningamount += 1
            except:
                print("There is an invalid score in the list.")
        print(f"The highest score is {runninghighest}, which belongs to {names[scores.index(str(runninghighest))]}. The average score is {(runningtotal/runningamount):.2f}")

def SearchName(): # Finds a specific player's scores.
    Name = input("Who should be searched for?\n")
    with open("scores.txt", "r") as f:
        for x in f:
            if(x == "\n"):
                pass
            else:
                if(x[0:len(Name)] == Name):
                    print(x)
                    x = x.split(": ")
                    print(f"{x[0]}: {x[1]}")
                
def ExportSummary(): # Exports a copy of the data file.
    with open("scores.txt", "r") as f:
        with open("exportdata.txt", "w") as g:
            g.write(f.read())

def MainMenu(): # The main menu.
    choix = input("1. Write a new score.\n2. Read all scores.\n3. Search for player.\n4. Export data.\n")
    if(choix == "1"):
        WriteNewScore()
    elif(choix == "2"):
        ReadScores()
    elif(choix == "3"):
        SearchName()
    elif(choix == "4"):
        ExportSummary()
    else:
        print("WRONG.")
    MainMenu()

MainMenu()