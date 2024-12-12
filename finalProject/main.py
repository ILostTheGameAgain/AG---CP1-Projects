#Alec George Final Project

import random

#first variables
map = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
player_position = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," ","E"," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
player_x = 3
player_y = 3
inventory = []
speed = 1


#set board function
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


#function to buy things
def shop(gold):
    global inventory
    global speed
    
    while True:
        print(f"""what would you like to buy? type:
1 to buy speed upgrade: can move faster .................. (7 gold)
2 to buy efficiency upgrade: can do more things in a day . (7 gold)
3 to buy strength upgrade: do more damage ................ (5 gold)
4 to buy health upgrade: take more hits .................. (3 gold)
5 to buy random upgrade .................................. (5 gold)
6 to buy strength potion: deal more damage once .......... (4 gold)
7 to buy health potion: heal some health ................. (2 gold)
8 to buy random potion ................................... (3 gold)
9 to sell wood, 2 gold per wood .......................... (+{inventory.count("wood")*2} gold)
10 to sell stone .........................................
10 to leave shop
(you have {gold} gold)
""")
        user_input = input()
        if user_input == "1":
            if gold >= 7:
                gold -= 7
                speed += 1
                print("\nupgraded speed\n")
            else:
                print("\nnot enough gold\n")
        elif user_input == "9":
            break


#function to interact with environment
def interact(place):
    global inventory
    if place == "oO":
        inventory.append("rock")
        print("got rocks")
        inventory.sort()
        return True
    elif place == "/\\":
        inventory.append("wood")
        print("got wood")
        inventory.sort()
        return True
    elif place == "? ":
        inventory.append("gold")
        print("got gold")
        inventory.sort()
        return true
    elif place == "$ ":
        shop(inventory.count("gold"))

    return False


#function for movement
def movement(max_moves):
    global player_position
    global player_x
    global player_y
    continue_moving = True
    #list for the change of player position, [n/s, e/w]
    position_change = [0, 0]
    for i in range(max_moves):
    
        while True:
            if continue_moving:
                #user types letters, and moves depending on what they put
                player_moves = input(f"where would you like to move? type 1 letter (you have {max_moves-i} moves left)\nn for north\ne for east\ns for south\nw for west\nto not move, type -\nyour answer here\n").strip().lower()
                if len(player_moves) == 1: #user moves 1 place at a time
                    if player_moves == "n":
                        position_change[0] -= 1
                    elif player_moves == "w":
                        position_change[1] += 1
                    elif player_moves == "e":
                        position_change[0] += 1
                    elif player_moves == "s":
                        position_change[1] -= 1
                    elif player_moves == "-":
                        continue_moving = False
                    else:
                        print("invalid input")
                        break
                else:
                    print("invalid input")
                    continue
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
            position_change = [0, 0]
            break
            



#function to show inventory
def display_inventory():
    inventory_display = []
    for i in inventory:
        if i not in inventory_display:
            inventory_display.append(i)
    print(f"\ninventory:")
    for i in inventory_display:
        print(f"{i} x {inventory.count(i)}")

    
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
        movement(speed)
    elif user_input == "2":
        if interact(map[player_y][player_x]):
            map[player_y][player_x] = "  "
    elif user_input == "3":
        display_inventory()
    