# Alec George Raid: Simple histogram

#will ask for a list of numbers and display the list, IT IS NOT ACTUALLY A HISTOGRAM!!!


while True:
    try:
        inputted_numbers = input("\nwhat numbers would you like to display? (minimum of 6, separated by spaces)\n")
        loop_repeats = 0

        #reset variables: list and indexes for numbers to be put into lists
        min_index = 0
        max_index = 0
        list_of_numbers = []

        for i in inputted_numbers: #use spaces to put numbers in list
            if i == " ":
                min_index = max_index
                max_index = loop_repeats
                list_of_numbers.append(int(inputted_numbers[min_index:max_index]))
            loop_repeats += 1

        if inputted_numbers[-1] != " ": #put last number in list
            min_index = max_index
            max_index = len(inputted_numbers)
            list_of_numbers.append(int(inputted_numbers[min_index:max_index]))

        if len(list_of_numbers) >= 6: #check if list is long enough
            break

        else:
            print("\nmust have at least 6 numbers")

    except ValueError:
        print("\ninvalid input")

#will display values as:
#display 1's as *
#for 10's, will use ^
#for 100's will use %
#for 1000's will use $
#for 10000's will use #
#for 100000's will use @
#for 1000000's will use !
#for 10000000's will use ~
#and so on
#print key
print("""
KEY:
y: 1,000,000,000,000,000,000,000,000
t: 100,000,000,000,000,000,000,000
r: 10,000,000,000,000,000,000,000
e: 1,000,000,000,000,000,000,000
w: 100,000,000,000,000,000,000
q: 10,000,000,000,000,000,000
}: 1,000,000,000,000,000,000
W: 100,000,000,000,000,000
Q: 10,000,000,000,000,000
X: 1,000,000,000,000,000
O: 100,000,000,000,000
.: 10,000,000,000,000
?: 1,000,000,000,000
E: 100,000,000,000
>: 10,000,000,000
:: 1,000,000,000
|: 100,000,000
~: 10,000,000
!: 1,000,000
@: 100,000
#: 10,000
$: 1,000
%: 100
^: 10
*: 1
""")

loop_repeats = 0

for i in list_of_numbers:
    next_number = i
    next_number_translated = ""

    while next_number >= 1000000000000000000000000:
        next_number_translated += "y"
        next_number -= 1000000000000000000000000

    while next_number >= 100000000000000000000000:
        next_number_translated += "t"
        next_number -= 100000000000000000000000

    while next_number >= 10000000000000000000000:
        next_number_translated += "r"
        next_number -= 10000000000000000000000

    while next_number >= 1000000000000000000000:
        next_number_translated += "e"
        next_number -= 1000000000000000000000

    while next_number >= 100000000000000000000:
        next_number_translated += "w"
        next_number -= 100000000000000000000

    while next_number >= 10000000000000000000:
        next_number_translated += "q"
        next_number -= 10000000000000000000

    while next_number >= 1000000000000000000:
        next_number_translated += "}"
        next_number -= 1000000000000000000

    while next_number >= 100000000000000000:
        next_number_translated += "W"
        next_number -= 100000000000000000

    while next_number >= 10000000000000000:
        next_number_translated += "Q"
        next_number -= 10000000000000000

    while next_number >= 1000000000000000:
        next_number_translated += "X"
        next_number -= 1000000000000000

    while next_number >= 100000000000000:
        next_number_translated += "O"
        next_number -= 100000000000000

    while next_number >= 10000000000000:
        next_number_translated += "."
        next_number -= 10000000000000

    while next_number >= 1000000000000:
        next_number_translated += "?"
        next_number -= 1000000000000

    while next_number >= 100000000000:
        next_number_translated += "E"
        next_number -= 100000000000

    while next_number >= 10000000000:
        next_number_translated += ">"
        next_number -= 10000000000

    while next_number >= 1000000000:
        next_number_translated += ":"
        next_number -= 1000000000

    while next_number >= 100000000:
        next_number_translated += "|"
        next_number -= 100000000

    while next_number >= 10000000:
        next_number_translated += "~"
        next_number -= 10000000

    while next_number >= 1000000:
        next_number_translated += "!"
        next_number -= 1000000

    while next_number >= 100000:
        next_number_translated += "@"
        next_number -= 100000

    while next_number >= 10000:
        next_number_translated += "#"
        next_number -= 10000

    while next_number >= 1000:
        next_number_translated += "$"
        next_number -= 1000

    while next_number >= 100:
        next_number_translated += "%"
        next_number -= 100

    while next_number >= 10:
        next_number_translated += "^"
        next_number -= 10

    while next_number > 0:
        next_number_translated += "*"
        next_number -= 1
    
    loop_repeats += 1
    print(str(loop_repeats) +": "+ next_number_translated+"\n")