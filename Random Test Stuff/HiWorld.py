TheWord = input("Give me a word to reverse:\n")
TempWord = ""
TempList = []
for x in TheWord:
    TempList += x
TempList.reverse()
for x in TempList:
    TempWord += x
print(TempWord)