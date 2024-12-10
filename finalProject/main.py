#Alec George Final Project

#first variables
map = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
player_position = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," ","X"," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
player_x = 2
player_y = 2
#function for movement
def movement(max_moves):
    global player_position
    global player_x
    global player_y
    #list for the change of player position, [n, e, s, w]
    position_change = [0, 0, 0, 0]
    for y in range(7):
        for x in range(7):
            if player_position[y][x] == "X":
                player_x = x
                player_y = y
    while True:
        #user types letters, and moves depending on what they put
        player_moves = input(f"where would you like to move? type up to {max_moves} letters,\nn for north\ne for east\ns for south\nw for west\nyour answer here\n").strip().lower()
        if len(player_moves) <= max_moves: #user can't move more than an amount
            for i in player_moves:
                if i == "n":
                    position_change[0] += 1
                elif i == "e":
                    position_change[1] += 1
                elif i == "s":
                    position_change[2] += 1
                elif i == "w":
                    position_change[3] += 1
                else:
                    print("invalid input")
                    break
            
            player_position[player_y][player_x] = " " #remove the previous x
            #adjust position
            player_x += position_change[1]
            if player_x > 6:
                player_x = 6
            player_x -= position_change[3]
            if player_x < 9:
                player_x = 0
            player_y += position_change[2]
            if player_y > 6:
                player_y = 6
            player_y -= position_change[0]
            if player_x < 0:
                player_x = 0
            player_position[player_y][player_x]= "X"
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
            print(f"{map[y][x]} ", end="")
            print(f" {player_position[y][x]}|", end="")

        if y == 0:
            print("   W + E",end="")
            print("\n+----+----+----+----+----+----+----+     S")

        else:
            print("\n+----+----+----+----+----+----+----+")


display_map()
movement(3)
display_map()