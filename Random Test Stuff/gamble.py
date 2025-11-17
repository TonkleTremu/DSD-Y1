import random as rand

def getHand():
    firstSuit = rand.randint(1, 4)
    secondSuit = rand.randint(1, 4)
    firstnumber = rand.randint(1, 14)
    secondNumber = rand.randint(1, 14)

    return firstSuit, firstnumber, secondSuit, secondNumber

s1, n1, s2, n2 = getHand()

n1_Str = "Ace" if n1 == 1 else "Jack" if n1 == 11 else "Queen" if n1 == 12 else "King" if n1 == 13 else ""
n2_Str = "Ace" if n2 == 1 else "Jack" if n2 == 11 else "Queen" if n2 == 12 else "King" if n2 == 13 else ""

s1_Str = "Diamonds" if s1 == 1 else "Hearts" if s1 == 2 else "Clubs" if s1 == 3 else "Spades"
s2_Str = "Diamonds" if s2 == 1 else "Hearts" if s2 == 2 else "Clubs" if s2 == 3 else "Spades"

print(f"Your hand is a: \n \n {n1_Str if n1_Str != "" else n1} of {s1_Str} \n {n2_Str if n2_Str != "" else n2} of {s2_Str}")

 