Ϟ = 0
þ = 1
ƒ = {}

def á(Æ, æ):
    ƒ[Æ] = float(input("What is your glucose reading?\n"))
    average = sum(ƒ.values()) / len(ƒ)
    if(ƒ[Æ] < ƒ[Æ-1]):
        æ += 1
        print(f"Great! Your reading improved! Your score is now {æ}, and your average is {average}")
    else:
        print(f"Sacre bleu! No improvement. Your score is still {æ}, and your average is {average}")
    Æ += 1
    print(ƒ)
    á(Æ, æ)

def ú(þ, Ϟ):
    ƒ[0] = float(input("What is your glucose reading?\n"))
    á(þ, Ϟ)