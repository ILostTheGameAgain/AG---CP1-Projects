#Alec George Skill Practice: What is my grade

#asks number grade and gives letter
while True: #while loop to do this repeatedly
    try:
        grade = int(input("\nWhat is your grade? (number from 1 to 100) "))
    except ValueError:
        print("invalid number.")
        continue
    if grade >= 93:
        letter_grade = "A"
    elif grade >= 90:
        letter_grade = "A-"
    elif grade >= 87:
        letter_grade = "B+"
    elif grade >= 83:
        letter_grade = "B"
    elif grade >= 80:
        letter_grade = "B-"
    elif grade >= 77:
        letter_grade = "C+"
    elif grade >= 73:
        letter_grade = "C"
    elif grade >= 70:
        letter_grade = "C-"
    elif grade >= 67:
        letter_grade = "D+"
    elif grade >= 63:
        letter_grade = "D"
    elif grade >= 60:
        letter_grade = "D-"
    else:
        letter_grade = "F"
    print(f"\nyou have a {letter_grade}")