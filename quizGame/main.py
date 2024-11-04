#Alec George Proficiency Test: Simple Quiz Game


#will ask math questions, if correct give point and give harder question, if incorrect, don't give point and give easier question

#add randomness to answers, import random
import random

#variable for difficulty, gives harder questions as it moves up
difficulty = 10

for x in range(0, 5): #makes the user answer five questions
    #each question gets two values and multiplies them, bigger range and higher numbers as difficulty goes up
    value_1 = random.randint(int(difficulty/2), difficulty)
    value_2 = random.randint(int(difficulty/2), difficulty)
    correct_answer = value_1 * value_2

    answers = []
    #provides four random answers
    for x in range(0, 4):
        answers.append(random.randint(correct_answer - random.randint(int(difficulty/2), difficulty), correct_answer + random.randint(int(difficulty/2), difficulty)))

    print(f"what is {value_1} times {value_2}?\nA. {answer_1}\nB. {answer_2}\nC. {answer_3}\nD. {answer_4}")
    #if one isn't already correct, make one correct