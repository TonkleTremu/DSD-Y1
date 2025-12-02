# It's spelt with no 'e' because that's cool.
import RevLib
import random
def AskQuestion(): # Pulls a random question from the library, and asks the user it.
    question = random.choice(list(RevLib.OpenEnd.items()))
    inputanswer = input(f"{question[0]}\n").lower()
    answers = question[1][1]
    response = False
    for answer in answers:
        distance = Lev(answer, inputanswer)
        if(distance <= question[1][0]):
            response = True
    if(response):
        print("Correct answer!")
    else:
        print(f"Wrong answer. It was {answers[0]}.")
    AskQuestion()

def Lev(str1, str2):
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

AskQuestion()