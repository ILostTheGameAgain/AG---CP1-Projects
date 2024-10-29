#Alec George Proficiency Test: rock, paper, scissors

#will keep playing rock paper scissors with user until they choose to stop

import random #needs random for computer to decide input

while True: #will use break statement to end game

    computer_input = random.randint(1,3) #whether something is rock, paper, or scissors doesn't matter other than printing it

    try:
        user_input = int(input("\ntype\n1 for rock\n2 for paper\n3 for scissors\n4 to quit\nyour input here: "))
    except ValueError: 
        print("\ninvalid input")
        continue

    #if statements to show what user played
    if user_input == 4: #quit while loop if input is 4
        break
    elif user_input == 1: #play rock if input is 1
        print("\nyou played rock")
    elif user_input == 2: #play paper if input is 2
        print("\nyou played paper")
    elif user_input == 3: #play scissors if input is 3
        print("\nyou played scissors")
    else:
        print("\ninvalid input")
        continue

    #if statements to show what computer played
    if computer_input == 1: #play rock if input is 1
        print("\ncomputer played rock")
    elif computer_input == 2: #play paper if input is 2
        print("\ncomputer played paper")
    else: #play scissors if input is anything else, which can only be 3
        print("\ncomputer played scissors")

    #if statements to decide who wins, 1 beats 2, 2
print("this is a print statement")
print("\nThanks for playing!")