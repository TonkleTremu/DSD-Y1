for x in range(5):
    print(x)
colours = ["red", "green", "blue", "maroon"]
for colour in colours:
    print(colour)
points = [(0,0), (0,1), (1,0), (1,1)]
for x,y in points:
    print(f"{x = } and {y = }")
for c in "Hello World!":
    print(c)

stuff = {
    1: "Apple",
    2: "Pear",
    3: "Omelette",
    4: "Four"
}

for thing in stuff:
    print(str(thing) + ") " + stuff[thing])

for num,thing in stuff.items():
    print(str(num) + ") " + thing)

for x in range(3000):
    print(x)
    if(x==2763):
        print(f"{x} found!")
        break