#Alec George Proficiency Test: Simple Calculator

#make this a function so it can be repeated
def calculator():
    number_one = float(input("\nwhat is the first number? "))
    number_two = float(input("what is the second number? "))
    output = 0
    operator = input("What would you like to do with these numbers?\ntype 1 to add "+ str(number_one)+" and "+str(number_two)+"\ntype 2 to subtract "+str(number_two)+" from "+ str(number_one) + "\ntype 3 to multiply "+str(number_one)+" by "+ str(number_two) +"\ntype 4 to divide "+str(number_one)+" by "+str(number_two)+"\ntype 5 to raise "+str(number_one)+" to the power of "+str(number_two)+ "\ntype 6 to get the result of "+str(number_one)+" mod "+str(number_two)+"\ntype 7 to get a rounded answer of "+str(number_one)+" divided by "+str(number_two)+"\n")
    if operator == "1":
        output = number_one+number_two
    elif operator == "2":
        output = number_one-number_two
    elif operator == "3":
        output = number_one*number_two
    elif operator == "4":
        output = number_one/number_two
    elif operator == "5":
        output = number_one**number_two
    elif operator == "6":
        output = number_one%number_two
    elif operator == "7":
        output = number_one//number_two
    else:
        output = "no"
    if type(output) == float:
        print("The answer is "+str(output))
    else:
        print("that is not an option.")
    calculator()
calculator()