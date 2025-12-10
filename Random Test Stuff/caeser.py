inp = input("What should be ciphered?\n").lower() # The .lower() function was added later, so that I didn't need to deal with capital letters.
ciph = int(input("How far should it be ciphered?\n"))
out = ""

for x in inp: # Goes through each letter in a string and shifts it along the cipher.
    if(x.isalpha()):
        x = ord(x) + ciph
        while(x > 122): # Values exceeding z overflew into non-alpha characters, such as {.
            x -= 26
        while(x < 97): # Values preceeding a went into non-alpha characters.
            x += 26
        out += chr(x)
    else:
        out += x

print(out)