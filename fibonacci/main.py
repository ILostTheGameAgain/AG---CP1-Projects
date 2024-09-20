#Alec George Raid: Fibonacci Sequence Generator

#variables
digits = 0
list_of_numbers = [0]
current_number = 0
sequence = ""

#variable for number of numbers, is user input
number_of_numbers = input("\nhow many numbers would you like? (enter a whole number): ")
#repeat the amount of digits times
while digits <= int(number_of_numbers)-1:

    #if current number is 0, add 1
    if current_number == 0:
        current_number += 1

    #if current number is greater than 0, add the previous numbers together
    else:
        current_number = list_of_numbers[digits]+list_of_numbers[digits-1]

    #add current number to the list of numbers
    list_of_numbers.append(current_number)

    #add the last digit to the string
    sequence = sequence + str(list_of_numbers[digits]) +", "
    digits += 1

print("\nthe first"+number_of_numbers+ "digits of the fibonacci sequence are:")
print(sequence)