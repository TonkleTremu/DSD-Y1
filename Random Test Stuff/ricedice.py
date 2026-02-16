import random

Lives = 3
while(Lives > 0):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f"Total: {dice1} + {dice2} = {dice1+dice2}")
    if(dice1+dice2 == 7 or dice1+dice2 == 11):
        print("You Win!")
    else:
        print("Try Again!")
        Lives -= 1
    input()