#Alec George Final Project

import random

#first variables
map = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
player_position = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," ","E"," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
player_x = 3
player_y = 3

#setup board
for y in range(7):
    for x in range(7):
        resource = random.randint(1,5)
        if x == 3:
            if y == 2:
                resource = 6
        if resource == 4:
            map[y][x] = "oO"
        elif resource == 5:
            map[y][x] = "/\\"
        elif resource == 6:
            map[y][x] = "$ "
        else:
            map[y][x] = "  "
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
            player_moves = input(f"where would you like to move? type up to {max_moves} letters,\nn for north\ne for east\ns for south\nw for west\nyour answer here\n").strip().lower()
            if len(player_moves) == 1: #user moves 1 place at a time
                for i in player_moves:
                    if i == "n":
                        position_change[0] -= 1
                    elif i == "e":
                        position_change[1] += 1
                    elif i == "s":
                        position_change[0] += 1
                    elif i == "w":
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
    # ----+----+----+----+----+----+----  W + E
    #     |    |    |    |    |    |        S
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
            print("   W + E",end="")
            print("\n+----+----+----+----+----+----+----+     S")

        else:
            print("\n+----+----+----+----+----+----+----+")
    print("""KEY:
$ - Shop       Oo - rocks
# - treasure   /\\ - tree
E - you
""")




#run everythng
while True:
    display_map()
    movement(3)
