import LeisureQuizLib as LQL
import random

correctanswers = 0
askedquestions = []
for x in range(1,11):
    question = random.choice(list(LQL.questions.items()))
    while(question[0] in askedquestions):
        question = random.choice(list(LQL.questions.items()))
    askedquestions.append(question[0])
    inputanswer = input(f"Question {x}. {question[0]}\n").capitalize()
    answers = question[1]["Answers"]
    response = False
    for answer in answers:
        distance = LQL.Levenshtein(answer, inputanswer)
        if(distance <= question[1]["AllowedDistance"]):
            response = True
    if(response):
        print("Correct answer!")
        correctanswers += 1
    else:
        print(f"Wrong answer. It was {answers[0]}")
print(f"You got {correctanswers} correct out of 10")