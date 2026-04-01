keylist = {"a": "s", "b": "n", "c": "v", "d": "f", "e": "r", "f": "g", "g": "h", "h": "j", "i": "o", "j": "k", "k": "l", "l": ";", "m": ",", "n": "m", "o": "p", "p": "[", "q": "w", "r": "t", "s": "d", "t": "y", "u": "i", "v": "b", "w": "e", "x": "c", "y": "u", "z": "x"}
encode = input("What should be encoded?\n").lower()
encoded = ""
for cha in encode:
    try:
        encoded += keylist[cha]
    except:
        encoded += cha
print(encoded)


encode = input("What should be decoded?\n").lower()
encoded = ""
for cha in encode:
    try:
        keys = [key for key, val in keylist.items() if val == cha]
        encoded += keys[0]
    except:
        encoded += cha
print(encoded)