#Alec George Proficiency Test: rock, paper, scissors

#will keep playing rock paper scissors with user until they choose to stop

import random #needs random for computer to decide input

#variables for computer wins, player wins, ties, and number of plays
computer_score = 0
player_score = 0
ties = 0
rounds = 0

while True: #will use break statement to end game

    computer_input = random.randint(0,2) #whether something is rock, paper, or scissors doesn't matter other than printing it

    try:
        user_input = int(input("\ntype\n1 for rock\n2 for paper\n3 for scissors\n4 to show score\n5 to quit\nyour input here: "))
    except ValueError: 
        print("\ninvalid input")
        continue

    #if statements to show what user played
    if user_input == 5: #quit while loop if input is 5
        break
    elif user_input == 1: #play rock if input is 1
        print("\nyou played rock")
    elif user_input == 2: #play paper if input is 2
        print("\nyou played paper")
    elif user_input == 3: #play scissors if input is 3
        print("\nyou played scissors")
    elif user_input == 4: #show score if input is 4
        print(f"\nscore:\n player: {player_score}\n computer: {computer_score}\n ties: {ties}\nwin rate: {round((player_score/rounds)*100, 2)}%")
        continue
    else:
        print("\ninvalid input")
        continue
    
    user_input -= 1

    #if statements to show what computer played
    if computer_input == 0: #play rock if input is 0
        print("\ncomputer played rock")
    elif computer_input == 1: #play paper if input is 1
        print("\ncomputer played paper")
    else: #play scissors if input is anything else, which can only be 2
        print("\ncomputer played scissors")

    #if statements to decide who wins, tie if numbers are equal
    if computer_input == user_input:
        print("\nit's a tie")
        ties += 1
    elif (computer_input-1)%3 == user_input:
        print("\ncomputer wins")
        computer_score += 1
    elif (computer_input+1)%3 == user_input:
        print("\nplayer wins")
        player_score += 1
    
    rounds += 1

print("\nThanks for playing!")