#Alec George Proficiency Test: I Can't Read This!

#Comments also added by Alec George

import random

#function to display an introduction, explain what is happening
def display_intro():
    print("Welcome to the Mystic Forest Adventure!")
    print("You find yourself at the edge of a dark, mysterious forest.")
    print("Your goal is to find the hidden treasure and escape safely.")

#function to make a choice from one of the options available
def make_choice(options):

    #display options
    for i,option in enumerate(options,1):
        print(f"{i}. {option}")

    #user input to choose an option, they type a number
    while True:

        try:
            choice=int(input("Enter your choice: "))

            if 1<=choice<=len(options):
                return choice
            else:
                
                print("Invalid choice. Try again.")
        except ValueError:print("Please enter a number.")

#function to explore forest, chance of a random event happening
def explore_forest():
    print("You venture deeper into the forest...")
    events=["You encounter a friendly woodland creature.","You find a shimmering portal.","You discover an ancient ruins.","You come across a bubbling stream."]
    print(random.choice(events))

#function that displays that you found treasure
def find_treasure():
    print("Congratulations! You've found the hidden treasure!")
    print("It's a chest filled with gold coins and magical artifacts.")

#function to face a challenge, have a chance to succeed and a chance to fail
def face_challenge():
    print("Oh no! You've encountered a challenge!")
    challenges=["A giant spider blocks your path.","A riddle-speaking owl demands an answer.","A magical barrier requires a spell to pass."]
    print(random.choice(challenges))

    #decide if user succeeds or fails
    if random.random()<0.5:
        print("You successfully overcome the challenge!")
        return True
    else:
        print("You fail to overcome the challenge.")
        return False

#function that puts everything together and runs it
def play_game():
    display_intro()
    treasure_found=False

    #keep doing things until user finds treasure
    while not treasure_found:
        print("\nWhat would you like to do?")
        choice=make_choice(["Explore the forest","Search for treasure","Face a challenge","Exit the forest"])

        #if choice is 1, explore the forest
        if choice==1:
            explore_forest()
        
        #if choice is 2, look for treasure
        elif choice==2:

            #have a chance to find treasure if looking
            if random.random()<0.3:
                find_treasure()
                treasure_found=True
            else:
                print("No treasure here. Keep searching!")

        #if choice is 3, face a challenge
        elif choice==3:
            
            #if challenge was a success, chance to find treasure
            if face_challenge():

                if random.random()<0.4:
                    find_treasure()
                    treasure_found=True
        
        #if choice is 4, end the game
        elif choice==4:
            print("You decide to leave the forest. Game over!")
            return
        
        #win if treasure is found
        if treasure_found:
            print("Congratulations! You've won the game!")

if __name__=="__main__":play_game()