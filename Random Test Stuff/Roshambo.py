import random
def Roshambo():
    Choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    Weaknesses = {"Rock": ["Paper", "Spock"], "Paper": ["Scissors", "Lizard"], "Scissors": ["Rock", "Spock"], "Lizard": ["Rock", "Scissors"], "Spock": ["Lizard", "Paper"]}
    TheirChoice = random.choice(Choices)
    YourChoice = input("Rock, Paper, Scissors, Lizard, Spock:\n").capitalize()
    if(YourChoice in Weaknesses[TheirChoice]):
        print(f"You win! They chose {TheirChoice} - {YourChoice} beats {TheirChoice}.")
    elif(YourChoice == TheirChoice):
        print("Draw!")
    elif(YourChoice in Choices):
        print(f"You lost! They chose {TheirChoice} - {TheirChoice} beats {YourChoice}.")
    else:
        if(random.randint(0,1) == 1):
            print(f"You win! {YourChoice} beats {TheirChoice}.")
        else:
            print(f"You lose! {TheirChoice} beats {YourChoice}.")
    Roshambo()
Roshambo()