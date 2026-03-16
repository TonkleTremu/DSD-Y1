from inputimeout import inputimeout, TimeoutOccurred

while(True):
    try:
        x = inputimeout(prompt='>>', timeout=5)
    except:
        print("time")
