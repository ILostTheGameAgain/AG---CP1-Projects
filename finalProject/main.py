#Alec George Final Project

import random

#first variables
map = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
player_position = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," ","E"," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
player_x = 3
player_y = 3
inventory = []
speed = 1
player_health = 100
player_attack = 2
level = 1
actions = 3
time = "day"

#set board function
def setup():
    for y in range(7):
        for x in range(7):
            resource = random.randint(1,20)
            if x == 3:
                if y == 2:
                    resource = 21
            if resource >= 11 and resource <= 13:
                map[y][x] = "oO"
            elif resource >= 14 and resource <= 18:
                map[y][x] = "/\\"
            elif resource >= 19 and resource <= 20:
                map[y][x] = "? "
            elif resource == 21:
                map[y][x] = "$ "
            else:
                map[y][x] = "  "


#function for combat
def combat():
    global player_health
    global player_attack
    #decide what attacks you, there aren't really any differences except for the name
    enemies = ["a bear", "100 squirrels", "a racoon", "a snake", "a deer"]
    short_name = ["bear", "squirrels", "racoon", "snake", "deer"]
    enemy = random.randint(0, len(enemies)-1)
    print(f"You encounter {enemies[enemy]}")

    enemy_health = 10
    enemy_attack = 2
    #loop for main combat
    while True:
        #user does something
        while True:
            counter = 0
            print(f"""
What do you do? type:
1 to attack the {short_name[enemy]}
2 to try to counter the next attack
3 to use an item
your answer here:""")
            
            user_input = input()
            if user_input == "1":
                enemy_health -= player_attack
                print(f"\nattacked the {short_name[enemy]}\nit now has {enemy_health} health left")
                break
            elif user_input == "2":
                counter = random.randint(0,1)
                if counter == 1:
                    print("\ncounter was successful")
                    break
                else:
                    print("\ncounter was successful")
                break
            elif user_input == "3":
                break
            else:
                print("\ninvalid input")
        
        #check if enemy is defeated
        if enemy_health <= 0:
            return True
        
        #enemy attacks
        if counter == 0:
            player_health -= random.randint(1, enemy_attack)
            print(f"\nthe {short_name[enemy]} attacked you\nyou now have {player_health} health left")
        else:
            enemy_health -= random.randint(1, enemy_attack)
            print(f"\nthe {short_name[enemy]} attacked you\nhowever, you countered the attack\nit now has {enemy_health} health left")
        
        #check if player is defeated
        if player_health <= 0:
            return False
    


#function to buy things
def shop(gold):
    global inventory
    global speed
    while True:
        #display the possible inputs
        print(f"""what would you like to buy? type:
1 to buy speed upgrade: can move faster .................. (7 gold)
2 to buy efficiency upgrade: can do more things in a day . (7 gold)
3 to buy strength upgrade: do more damage ................ (5 gold)
4 to buy health upgrade: take more hits .................. (3 gold)
5 to buy random upgrade .................................. (5 gold)
6 to buy strength potion: deal more damage once .......... (4 gold)
7 to buy health potion: heal some health ................. (2 gold)
8 to buy random potion ................................... (3 gold)
9 to sell wood, 2 gold per wood .......................... (you have {inventory.count("wood")} wood)
10 to sell rocks, 3 gold per rock......................... (you have {inventory.count("rock")} rocks)
11 to leave shop
(you have {gold} gold)
""")
        #get user input
        user_input = input()
        if user_input == "1": #buy movement upgrades
            if gold >= 7:
                gold -= 7
                speed += 1
                print("\nupgraded speed\n")
            else:
                print("\nnot enough gold\n")
        elif user_input == "9": #sell wood
            if inventory.count("wood") > 0:
                inventory.remove("wood")
                print("\n gained 2 gold")
            else:
                print("\nyou have no wood")
        elif user_input == "10": #sell rocks
            if inventory.count("rock") > 0:
                inventory.remove("rock")
                print("\n gained 3 gold")
            else:
                print("you have no money")
        elif user_input == "11":
            break


#function to interact with environment
def interact(place):
    global inventory
    #if there's a thing on the space the payer is on, remove it and add it to their inventory
    if place == "oO":
        amount_of_resource = random.randint(1, 3)
        for i in range(amount_of_resource):
            inventory.append("rock")
        print(f"\ngot rocks x {amount_of_resource}")
        inventory.sort()
        return True
    
    elif place == "/\\":
        amount_of_resource = random.randint(1, 3)
        for i in range(amount_of_resource):
            inventory.append("wood")
        print(f"\ngot wood x {amount_of_resource}")
        inventory.sort()
        return True
    
    elif place == "? ":
        amount_of_resource = random.randint(0, 10)
        for i in range(amount_of_resource):
            inventory.append("gold")
        print(f"\ngot gold x {amount_of_resource}")

        amount_of_resource = random.randint(0, 2)
        for i in range(amount_of_resource):
            inventory.append("rock")
        print(f"got rocks x {amount_of_resource}")

        amount_of_resource = random.randint(0, 2)
        for i in range(amount_of_resource):
            inventory.append("wood")
        print(f"got wood x {amount_of_resource}")

        inventory.sort()
        return True
    
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
                player_moves = input(f"where would you like to move? type 1 letter (you have {max_moves-i} moves left)\nn for north\ne for east\ns for south\nw for west\nto not move, type -\nNOTE THE COMPASS\nyour answer here\n").strip().lower()
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
    print("\n----------------------------------------------------------------\n")
    display_map()
    print("""what do you do? type:
1 to move
2 to shop/gather resources
3 to view inventory, does not count as an action
4 to rest""")
    user_input = input()
    if user_input == "1": #if user input is 1, player moves
        movement(speed)
        actions -= 1
    elif user_input == "2": #if user input is 2, player can gather things
        if interact(map[player_y][player_x]):
            map[player_y][player_x] = "  "
        actions -= 1
    elif user_input == "3": #if user input is 3, shows inventory
        display_inventory()
    elif user_input == "4": #if user input is 4, gain health
        health_gain = random.randint(0, 5)
        player_health += health_gain
        actions -= 1
    else:
        print("\ninvalid input")

    if actions > 0:
        print(f"\nyou have {actions} actions left")
    else:
        