# It's spelt with no 'e' because that's cool.
import RevLib
import random
import time
import webbrowser

def AskQuestion(askedquestions): # Pulls a random question from the library, and asks the user it. "askedquestions" counts up until it gets to 5, then an intermission starts.
    question = random.choice(list(RevLib.OpenEnd.items())) # A random question is pulled from the "RevLib" library.
    inputanswer = input(f"{question[0]}\n").lower() # A response to the question is taken from the user.
    answers = question[1][1]
    response = False
    for answer in answers: # Checks if the user's answer is close enough to any of the acceptable answers, using Lev().
        distance = Lev(answer, inputanswer)
        if(distance <= question[1][0]):
            response = True
    if(response):
        print("Correct answer!")
    else:
        print(f"Wrong answer. It was {answers[0]}.") # Tells the user the answer was the first acceptable answer in the list - for example, if RFID, NFC and Bluetooth are answers, it will say that RFID was the correct answer, though the other two would still be accepted.
    if(askedquestions >= 5):
        askedquestions = 0
        Intermissioning()
    else:
        askedquestions += 1
    AskQuestion(askedquestions)

def Intermissioning(): # Creates an "intermission". Some random silly stuff to make revision more fun.
    Choix = random.randint(0,6)
    if(Choix == 0):
        print("We're intermissioning, Pomni!")
        time.sleep(5)
    elif(Choix == 1):
        print("Did you know that fish in Indonesian is 'ikan' - this WILL be on the end-of-year test.")
        time.sleep(7)
    elif(Choix == 2):
        print("You should take a 5-minute break. No, I'm serious. This will not run again until 5 minutes have passed. I mean, you could turn it on and off... but why?")
        time.sleep(300)
    elif(Choix == 3):
        print("Pop-quiz princess: what happens when you bring an element of harmony into another world?")
        time.sleep(9)
    elif(Choix == 4):
        print("This program uses something called Levenshtein distance. It's really cool! Here, I'll open it for you:")
        time.sleep(4)
        webbrowser.open("https://www.google.com/search?q=levenshtein+distance/") # This should open in your native browser, such as Chrome or Opera.
        time.sleep(7)
    elif(Choix == 5):
        print("Hey, wanna see me waste your time?") # I've never actually had the patience to test if this one works or not.
        thecount = random.randint(60,6000)
        for x in range(thecount):
            if(x == thecount // 4):
                print("See, it's funny because you have no clue how long this goes on for.")
            if(x == 2*(thecount // 3)):
                print("Like, this could be 30% of the way, or 75%. By the way, this could actually go on for like an hour and a half.")
            if(x == 8*(thecount // 10)):
                print("In fact, this could only be 20% right now.")
            if(x == thecount):
                print("Well... that was fun.")
            time.sleep(1)
    elif(Choix == 6):
        print("Random websites go:")
        time.sleep(2)
        webbrowser.open("idk.lol")
        webbrowser.open("http.cat")
        webbrowser.open("https://mrdoob.com/projects/chromeexperiments/google-space/")
        webbrowser.open("neocities.org")
        webbrowser.open("wikipedia.com")
    else:
        print("See, I made this one as an else statement. That means this shouldn't run...")
        time.sleep(3)


def Lev(str1, str2): # Levenshtein distance implementation. Copied from Geeks For Geeks.
    m = len(str1)
    n = len(str2)

    # Initialize a matrix to store the edit distances
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize the first row and column with values from 0 to m and 0 to n respectively
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the matrix using dynamic programming to compute edit distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # Characters match, no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Characters don't match, choose minimum cost among insertion, deletion, or substitution
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    # Return the edit distance between the strings
    return dp[m][n]

AskQuestion(0)