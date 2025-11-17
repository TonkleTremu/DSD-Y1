import requests
import random

while(True):
    Characters = '1 2 3 4 5 6 7 8 9 0 q w e r t y u i o p a s d f g h j k l z x c v b n m'.split(' ')
    TempString = ''
    for x in range(5):
        TempString += random.choice(Characters)
    TempString = "GHQ24"
    response = requests.get('https://app.nearpod.com/presentation?pin=' + TempString)
    print(response.text)
    if(response.text.find('<script src="https://api.nearpod.com/v1/ct/translations?component=100"></script>') > 0):
        print(TempString)
    else:
        print(f"{TempString} found!")
        break