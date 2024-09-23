#Alec George Skill Practice: Average Grade

#variables
total_points = 0
grades = 0

#first grade
total_points = int(input("type the grade of a class (number, usually from 1 to 100): "))
grades += 1
#other grades are optional
while True:
    next_grade = input("\nIf you want to add another grade, type the number.\nIf that is all the grades, type finished\ntype your answer here: ")
    if next_grade == "finished":
        break
    else:
        total_points += int(next_grade)
        grades += 1
average_grade = total_points / grades
print("Your average grade is " + str(round(average_grade, 1)))