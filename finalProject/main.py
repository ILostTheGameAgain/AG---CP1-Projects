#Alec George Final Project

import random

#first variables
map = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
player_position = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," ","E"," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
player_x = 3
player_y = 3
inventory = []
#setup board function
def setup():
    for y in range(7):
        for x in range(7):
            resource = random.randint(1,12)
            if x == 3:
                if y == 2:
                    resource = 13
            if resource == 5 or resource == 6:
                map[y][x] = "oO"
            elif resource == 7 or resource == 8:
                map[y][x] = "/\\"
            elif resource == 9:
                map[y][x] = "? "
            elif resource == 13:
                map[y][x] = "$ "
            else:
                map[y][x] = "  "

#function to interact with environment
def interact(place):
    if place == "oO":
        inventory.append("rock")
        print("got rocks")
    elif place == "/\\":
        inventory.append("wood")
        print("got wood")
    elif place == "? ":
        inventory.append("gold")
        print("got gold")
    
    inventory.sort()


#function for movement
def movement(max_moves):
    global player_position
    global player_x
    global player_y
    #list for the change of player position, [n/s, e/w]
    position_change = [0, 0, 0, 0]
    for i in range(max_moves):
        while True:
            #user types letters, and moves depending on what they put
            player_moves = input(f"where would you like to move? type 1 letter,\nn for north\ne for east\ns for south\nw for west\nyour answer here\n").strip().lower()
            if len(player_moves) == 1: #user moves 1 place at a time
                for i in player_moves:
                    if i == "n":
                        position_change[0] -= 1
                    elif i == "w":
                        position_change[1] += 1
                    elif i == "e":
                        position_change[0] += 1
                    elif i == "s":
                        position_change[1] -= 1
                    else:
                        print("invalid input")
                        break
            
                player_position[player_y][player_x] = " " #remove the previous x
                #adjust position
                player_y += position_change[0]
                player_x += position_change[1]
                if player_x > 6:
                    player_x = 6
                if player_x < 0:
                    player_x = 0
                if player_y > 6:
                    player_y = 6
                if player_y < 0:
                    player_y = 0
                player_position[player_y][player_x]= "E"
                return True
            else:
                print("invalid input")



#function to make the map
def display_map():
    #Make 7x7 grid of squares
    #will print as
    #     |    |    |    |    |    |        N
    # ----+----+----+----+----+----+----  S + W
    #     |    |    |    |    |    |        E
    # ----+----+----+----+----+----+----
    #     |    |    |    |    |    |    
    # ----+----+----+----+----+----+----
    #     |    |    |    |    |    |    
    # ----+----+----+----+----+----+----
    #     |    |    |    |    |    |    
    # ----+----+----+----+----+----+----
    #     |    |    |    |    |    |    
    # ----+----+----+----+----+----+----
    #     |    |    |    |    |    |    
    print("+----+----+----+----+----+----+----+     N")
    for y in range(7):
        print(f"|",end="")
        for x in range(7):
            print(f"{map[y][x]}", end="")
            print(f" {player_position[y][x]}|", end="")

        if y == 0:
            print("   S + W",end="")
            print("\n+----+----+----+----+----+----+----+     E")

        else:
            print("\n+----+----+----+----+----+----+----+")
    print("""KEY:
$ - Shop       Oo - rocks
? - treasure   /\\ - tree
E - you
""")




#run everythng
setup()
while True:
    display_map()
    print("""what do you do? type:
1 to move
2 to shop/gather resources
3 to view inventory""")
    user_input = input()
    if user_input == "1":
        movement(3)
    elif user_input == "2":
        interact(map[player_y][player_x])
    elif user_input == "3":
        print(inventory)