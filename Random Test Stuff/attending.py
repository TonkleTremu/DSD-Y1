ExpAtt = float(input("How many students should you have?\n"))
ReAtt = float(input("How many students do you have?\n"))
PercAtt = int(round(ReAtt/ExpAtt, 2) * 100)
if(PercAtt > 100):
    print(f"Outstanding! More students showed up than were expected! ({PercAtt}%)")
elif(PercAtt == 100):
    print("Congrats! You have a full house! (100%)")
elif(PercAtt >= 90):
    print(f"You have some high-scoring attendance! ({PercAtt}%)")
elif(PercAtt >= 75):
    print(f"You should *lightly* encourage those missing students to attend school... ({PercAtt}%)")
elif(PercAtt >= 50):
    print(f"At least the majority of students are attending... ({PercAtt}%)")
elif(PercAtt > 0):
    print(f"You are definitely doing something wrong. ({PercAtt}%)")
else:
    print(f"Hey, you get the lesson off! You have literally nobody to teach! At all! (0%)")