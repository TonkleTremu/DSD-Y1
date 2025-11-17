print(input("What should be printed?\n"))
Fname = input("First Name:\n")
Sname = input("Second Name:\n")
name = f"{Fname} {Sname}"
print(name)
ShorterThanTwenty = False
while(ShorterThanTwenty == False):
    Sente = input("Gimme a sentence under 20 chars:\n")
    if(len(Sente) <= 20):
        print(f"That's a good sentence. It is {len(Sente)} characters long.")
        ShorterThanTwenty = True
    else:
        print("How dare you give me a sentence over 20 characters long?")

