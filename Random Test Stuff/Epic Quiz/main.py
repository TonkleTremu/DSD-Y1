import random, math, json

regions = {"kanto": 1, "johto": 2, "hoenn": 3, "sinnoh": 4, "unova": 5, "kalos": 6, "alola": 7, "galar": 8, "hisui": 9, "paldea": 10}
region_counts = [151,100,135,107,156,72,88,89,7,120]
FINAL_DEX_NO = 1024

correct = 0
asked = 0

with open("Random Test Stuff/Epic Quiz/pokedata.json") as f:
    pokelist = json.loads(f.read())

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

def RandomQuestion():
    dex_no = random.randint(0,FINAL_DEX_NO)
    this_poke = pokelist.get("results")[dex_no]
    return(dex_no)

def AskQuestion(dex_no):
    global asked, correct
    name = pokelist.get("results")[dex_no].get("name")
    response = input(f"What is Pokémon #{dex_no+1}?\n")
    asked += 1
    if(Lev(response.lower(), name) <= len(name)*0.2):
        correct += 1
        print(f"Correct! Out of {asked} questions, you got {correct} right so far. ({round(correct/asked, 2)*100}%)")
    else:
        print(f"Incorrect. Pokémon #{dex_no+1} is {name.capitalize()}. Out of {asked} questions, you got {correct} right so far. ({round(correct/asked, 2)}%)")
    
def AskRegion():
    for reg in regions.keys():
        print(reg.capitalize())
    region = input("Which region would you like to do?\n")
    this_region = regions.get(region.lower())
    total_before = 0
    for x in range(0, this_region-1):
        total_before += region_counts[x]
    parameters = [total_before, total_before+region_counts[this_region-1]]
    print(parameters)
    return(parameters)

    
choix = input("What would you like to do?\n1. Random Dex Numbers\n2. Full Dex\n3. Random by Region\n4. Full Region\n")
if(choix == "1"):
    while(True):
        AskQuestion(RandomQuestion())
elif(choix == "2"):
    for x in range(0,FINAL_DEX_NO):
        AskQuestion(x)
elif(choix == "3"):
    parameters = AskRegion()
    while(True):
        x = random.randint(parameters[0], parameters[1]-1)
        AskQuestion(x)
elif(choix == "4"):
    parameters = AskRegion()
    for x in range(parameters[0], parameters[1]):
        AskQuestion(x)