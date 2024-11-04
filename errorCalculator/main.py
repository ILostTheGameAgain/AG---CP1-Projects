#Alec George Skill Practice: Error Handling Calculator

#is a calculator that that can do basic operators and can handle errors

#may want more operations, exponents, ...,

def addition(num_1, num_2): #function for adding two number
    return num_1 + num_2

def multiplication(num_1, num_2): #function for multiplying two numbers
    return num_1 * num_2

def division(num_1, num_2): #function for dividing one number by the other
    return num_1 / num_2

def exponent(num_1, num_2): #function for raising one number to the power of another
    return num_1 ** num_2


while True: #make a while loop so user can keep using
    try:
        number_1 = int(input("what is the first number? "))
        number_2 = int(input("what is the second number? "))
    except ValueError:
        print("invalid number")
        continue
    #multiline string for user input
    operator = input("""\nWhat would you like to do with these numbers?
type:
 1 for addition
 2 for subtraction
 3 for multiplication
 4 for division
 5 for exponents
your answere here: """)
    if operator == "1":
        print(addition(number_1, number_2))
    elif operator == "2":
        print(addition(number_1, 0-number_2))
    elif operator == "3":
        print(multiplication(number_1, number_2))
    elif operator == "4":
        if number_2 != 0:
            print(division(number_1, number_2))
        else:
            print("\ncan't divide by 0")
            continue
    elif operator == "5":
        print(exponent(number_1, number_2))
    else:
        print("invalid input")
