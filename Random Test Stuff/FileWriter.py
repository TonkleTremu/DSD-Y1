def WriteNewScore(): # Allows the user to add a new name and score to the system.
    name = input("What is your name?\n")
    score = input("What is your score?\n")
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
        for x in scores:
            try:
                if(int(x) > runninghighest):
                    runninghighest = int(x)
            except:
                print("There is an invalid score in the list.")
        print(f"The highest score is {runninghighest}, which belongs to {names[scores.index(str(runninghighest))]}.")

def MainMenu(): # The main menu.
    choix = input("1. Write a new score.\n2. Read all scores.\n")
    if(choix == "1"):
        WriteNewScore()
    elif(choix == "2"):
        ReadScores()
    else:
        print("WRONG.")
    MainMenu()

MainMenu()