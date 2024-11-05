#Alec George Proficiency Test: Simple Quiz Game


#will ask math questions, if correct give point and give harder question, if incorrect, don't give point and give easier question

#add randomness to answers, import random
import random

#variable for difficulty, gives harder questions as it moves up
difficulty = 10
score = 0
used_answers = []
#give user option for amount of questions
while True:
    try:
        question_number = int(input("\nhow many questions would you like to answer? "))
        if question_number > 0:
            break
        else:
            print("\ninvalid input")
    except ValueError:
        print("\ninvalid input")
for x in range(0, question_number): #makes the user answer five questions
    #each question gets two values and multiplies them, bigger range and higher numbers as difficulty goes up, don't repeat numbers
    value_1 = random.randint(int(difficulty/2), difficulty)
    value_2 = random.randint(int(difficulty/2), difficulty)
    correct_answer = value_1 * value_2
    while correct_answer in used_answers:
        value_1 = random.randint(int(difficulty/2), difficulty)
        value_2 = random.randint(int(difficulty/2), difficulty)
        used_answers.append(correct_answer)
    answers = []

    #provides four random answers
    for y in range(0, 4):
        answers.append(random.randint(correct_answer - random.randint(int(difficulty/2), difficulty), correct_answer + random.randint(int(difficulty/2), difficulty)))
    
    #if one isn't already correct, make one correct
    if correct_answer not in answers:
        answers.pop(random.randint(0, 3))
        answers.insert(random.randint(0, 3), correct_answer)
    print(f"\nwhat is {value_1} times {value_2}?\nA. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}")
    
    #keeps taking user input until valid value, set user input to the corresponding answer
    while True:
        possible_answers = "abcd"
        user_answer = input("\nWhat is your answer? ").strip().lower()
        if user_answer in possible_answers and len(user_answer) == 1:
            if user_answer == "a":
                user_answer = answers[0]
            elif user_answer == "b":
                user_answer = answers[1]
            elif user_answer == "c":
                user_answer = answers[2]
            else:
                user_answer = answers[3]
            break
        else:
            print("invalid input")

    #tell user if they are correct, get more difficult if they are and less difficult if they aren't
    if user_answer == correct_answer:
        score += 1
        print(f"\ncorrect\nscore: {score} / {x+1}")
        difficulty *= 4
    else:
        print(f"\nincorrect\ncorrect answer: {correct_answer}\n score: {score} / {x+1}")
        difficulty /= 4
        #don't go below a certain difficulty
        if difficulty < 4:
            difficulty = 4
            used_answers.clear()
print("thanks for playing!")