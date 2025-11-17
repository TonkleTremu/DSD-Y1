questions = {"What is Pokémon #58 called?": {"Answers": ["Growlithe"], "AllowedDistance": 3}, "How many patterns does Spinda have?": {"Answers": ["4 billion", "4,294,967,295", "4,000,000,000", "4294967295", "4000000000"], "AllowedDistance": 1}, "How many Pokémon are there?": {"Answers": ["1025"], "AllowedDistance": 0}, "What is the first mythical Pokémon in dex order?": {"Answers": ["Mew"], "AllowedDistance": 1}, "What year was the first Pokémon game released?": {"Answers": ["1996"], "AllowedDistance": 0}, "Name one type that is super-effective against Fairy.": {"Answers": ["Poison","Steel"], "AllowedDistance": 1}, "Which Pokémon has the most evolutions?": {"Answers": ["Eevee"], "AllowedDistance": 2}, "What is the most common type in Pokémon?": {"Answers": ["Water"], "AllowedDistance": 1}, "What is Pokémon 1000?": {"Answers": ["Gholdengo"], "AllowedDistance": 3}, "Which Pokémon evolves after taking at least 49 damage (without fainting) then walking underneath a specific stone arch in the Dusty Bowl in Pokémon Sword/Shield?": {"Answers": ["Yamask", "Galarian Yamask"], "AllowedDistance": 2}, "Which Pokémon has the most regional forms?": {"Answers": ["Meowth"], "AllowedDistance": 1}, "How many generations of Pokémon are there?": {"Answers": ["9"], "AllowedDistance": 0}, "What is the only Pokémon region where Pokémon do NOT naturally appear?": {"Answers": ["Orre"], "AllowedDistance": 1}, "Which celestial body do all Pokémon canonically originate from?": {"Answers": ["The Moon", "Moon", "Luna"], "AllowedDistance": 1}, "Which Pokémon with a striking resemblance to Gallade/Gardevoir was the subject of a paranormal magazine, according to its dex entry?": {"Answers": ["Iron Valiant"], "AllowedDistance": 3}, "Which Pokémon was the first Mythical to be capable of evolution?": {"Answers": ["Meltan", "Melmetal"], "AllowedDistance": 2}, "Which Pokémon had its evolution accidentally revealed by an oversight in coding, where the item 'eviolite' improved its stats, implying it had a further evolution?": {"Answers": ["Applin", "Dipplin", "Hydrapple"], "AllowedDistance": 2}, "Charizard's shiny variant was changed from its gen 2 colour to black. What was it originally?": {"Answers": ["Purple"], "AllowedDistance": 1}, "Togepi and Ho-Oh were revealed in the anime before they were revealed in a game. Which other Pokémon was this the case for?": {"Answers": ["Terapagos"], "AllowedDistance": 2}, "Which Pokémon has a special variant obtainable in Pokémon Ultra Sun/Moon, only obtainable via a QR code event, which has a 1/4096 chance to be shiny, even though it is programmed NOT to have one?": {"Answers": ["Pikachu"], "AllowedDistance": 1}, "At what level does Pikachu learn Volt Tackle?": {"Answers": ["99"], "AllowedDistance": 0}, "What is the base shiny rate for all Pokémon before Gen 6?": {"Answers": ["1/8192", "8192"], "AllowedDistance": 0}}
# "": {"Answers": [""], "AllowedDistance": 0}

def Levenshtein(str1, str2):
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
