#Alec George Proficiency Test: Graded Quiz

score = 0

if input("Question 1:\nyes or no: you lost the game\n").strip().lower() == "yes":
    score += 1
    print("\ncorrect\n")
else:
    print("\nincorrect\n")

question2 = input("Question 2:\non a scale of square to circle, what letter best describes the color of the number 4?\n").strip().lower()

if  question2 == "rectangle":
    score += 1
    print("\ncorrect\n")
elif question2 == "trapezoid":
    score += 1
    print("\ncorrect\n")
else:
    print("\nincorrect\n")

if input("Question 3:\nyes or no: could I think of a better question 3 than this one?\n").strip().lower() == "no":
    score += 1
    print("\ncorrect\n")
else:
    print("\nincorrect\n")

if input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nQuestion 4:\nhow many questions have you answered before this one?\n") == "3":
    score += 1
    print("\ncorrect\n")
else:
    print("\nincorrect\n")

if input("Question 5:\nyes or no: you lost the game again\n").strip().lower() == "yes":
    score += 1
    print("\ncorrect\n")
else:
    print("\nincorrect\n")

print("final score: "+str(score)+" points")