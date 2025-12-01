import random
import json

def Roshambo():
    try:
        f = open("weaknesses", 'r')
    except:
        with open('weaknesses', 'w') as f:
            f.write('{"Rock": ["Paper", "Spock"], "Paper": ["Scissors", "Lizard"], "Scissors": ["Rock", "Spock"], "Lizard": ["Rock", "Scissors"], "Spock": ["Lizard", "Paper"]}')
        f.close()
        f = open("weaknesses", 'r')
    Weaknesses = dict(json.loads(f.read()))
    TheirChoice = random.choice(list(Weaknesses.keys()))
    YourChoice = input("Rock, Paper, Scissors, Lizard, Spock:\n").capitalize()
    if(YourChoice in Weaknesses[TheirChoice]):
        print(f"You win! They chose {TheirChoice} - {YourChoice} beats {TheirChoice}.")
    elif(YourChoice == TheirChoice):
        print("Draw!")
    elif(YourChoice in Weaknesses.values()):
        print(f"You lost! They chose {TheirChoice} - {TheirChoice} beats {YourChoice}.")
    else:
        if(random.randint(0,1) == 1):
            print(f"You win! {YourChoice} beats {TheirChoice}.")
            Weaknesses
        else:
            print(f"You lose! {TheirChoice} beats {YourChoice}.")
    Roshambo()
Roshambo()