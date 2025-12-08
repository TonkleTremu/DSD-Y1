import csv

FILENAME = "scores.csv"

def add_score(username, score):
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, score])
    pass

def show_scores():
    print("\n")
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            for line in reader:
                print(f"{line[0]} scored {line[1]}")
    except:
        print("Something went wrong - are we sure that scores exist to read from?")
    pass

def leaderboard():
    print("\n")
    scores = {}
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            for line in reader:
                try:
                    templist = scores[line[0]]
                    templist.append(int(line[1]))
                    scores.update({line[0]: templist})
                except:
                    scores.update({line[0]: [int(line[1])]})
            
        biglist = []
        for x in scores.values():
            for y in x:
                biglist.append(y)
        biglist.sort()
        for x in range(5):
            for i in scores:
                if(x in i[1]):
                    print(f"{x}. {i[0]} at {biglist[x]}")
    except:
        print("Something went wrong - are we sure that scores exist to read from?")
    pass

def main():
    while True:
        print("\n1. Add score")
        print("2. Show all scores")
        print("3. Leaderboard")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            score = int(input("Enter score: "))
            while(score < 0 or score > 100):
                score = int(input("Try again - only from 0 to 100: "))
            add_score(username, score)
        elif choice == "2":
            show_scores()
        elif choice == "3":
            leaderboard()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()