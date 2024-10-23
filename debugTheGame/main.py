#Alec George Raid: Fix the Game

#I know, it was said that there were four, but the program runs fine now.

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: ")) #logic error, guess was a string, but it is supposed to be an integer and is used like one multiple times. The code breaks if you try to use a string in an inequality with an integer. Fixed by casting the user input for guess to a string.

        attempts += 1 #runtime error, the code doesn't count attempts, so user guesses as much as they want. Fixed by adding 1 to the attempts after each guess

        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
            break #runtime error, the while loop keeps running until after it says too high or too low, causes it to still say it after the number. To fix, added break function in the if statement

        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        continue
    print("Game Over. Thanks for playing!")
start_game()