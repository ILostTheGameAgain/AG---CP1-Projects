#Alec George Final Project

import random
import time

#---------------------------------
#first variables
#---------------------------------
map = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
player_position = [["  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","⬜","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  "]]
player_x = 3
player_y = 3
inventory = []
speed = 1
player_health = 50
player_attack = 2
level = 1
starting_actions = 3
actions = 3
time_of_day = "day"
max_health = 50
days_passed = 0
win = ""

#---------------------------------
#set board function
#---------------------------------
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


#---------------------------------
#function to show inventory
#---------------------------------
def display_inventory():
    inventory_display = []
    for i in inventory:
        if i not in inventory_display:
            inventory_display.append(i)
    print(f"\nINVENTORY:")
    for i in inventory_display:
        print(f"{i} x {inventory.count(i)}")


#---------------------------------
#function for combat
#---------------------------------
def combat():
    global player_health
    global player_attack
    global map
    global player_y
    global player_x
    #decide what attacks you, there aren't really any differences except for the name
    enemies = ["a bear", "100 squirrels", "a racoon", "a snake", "a deer"]
    short_name = ["bear", "squirrels", "racoon", "snake", "deer"]
    enemy = random.randint(0, len(enemies)-1)
    print(f"\nYou encounter {enemies[enemy]}")
    #end combat immediately if there's a trap
    if map[player_y][player_x] == "v ":
        map[player_y][player_x] = "  "
        print("\nhowever, there was a trap, ending combat")
        return True
    enemy_health = 10 + round(1.5 ** days_passed)
    enemy_attack = 2 + round(0.2 ** days_passed)
    attack_multiplier = 1
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
                enemy_health -= round(player_attack*attack_multiplier)
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
                print(f"""\nwhat would you like to use? type
1 to use a health potion ({inventory.count("health potion")})
2 to use a strength potion ({inventory.count("health potion")})""")
                user_input = input()
                if user_input == "1" and inventory.count("health potion") > 0: #use health potion
                    inventory.remove("health potion")
                    health_gain = random.randint(1, max_health//10)
                    while health_gain + player_health > max_health:
                        health_gain -= 1
                    player_health += health_gain
                    print(f"\ngained {health_gain} health\nyou now have {player_health} health")
                elif user_input == "2" and inventory.count("strenght potion") > 0: #use strength potion
                    inventory.remove("strength potion")
                    attack_multiplier = 2
                    print("\nnext attack will do double damage")
                
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


#---------------------------------
#function to buy things
#---------------------------------
def shop(gold):
    global inventory
    global speed
    global starting_actions
    global player_attack
    global max_health
    global player_health
    speed_price = 7
    efficiency_price = 10
    strength_price = 5
    health_price = 6
    random_upgrade_price = 6
    strength_potion_price = 4
    health_potion_price = 3
    trap_price = 4
    while True:
        #display the possible inputs
        print("\033c")
        print(f"""\nwhat would you like to buy? type:
   UPGRADES
1 to buy speed upgrade: can move faster .................. ({speed_price} gold)
2 to buy efficiency upgrade: can do more things in a day . ({efficiency_price} gold)
3 to buy strength upgrade: do more damage ................ ({strength_price} gold)
4 to buy health upgrade: take more hits .................. ({health_price} gold)
5 to buy random upgrade .................................. ({random_upgrade_price} gold)
   ITEMS
6 to buy strength potion: deal more damage once .......... ({strength_potion_price} gold)
7 to buy health potion: heal some health ................. ({health_potion_price} gold)
8 to buy a trap: use  on an empty space to skip a fight .. ({trap_price} gold)
   SELL
9 to sell wood, 2 gold per wood ......................... (you have {inventory.count("wood")} wood)
10 to sell rocks, 3 gold per rock......................... (you have {inventory.count("rock")} rocks)
11 to leave shop
(you have {gold} gold)
""")
        #get user input
        user_input = input()
        if user_input == "1": #buy movement upgrades
            if gold >= speed_price:
                gold -= speed_price
                speed_price += 3
                speed += 1
                print("\nupgraded speed")
            else:
                print("\nnot enough gold")

        elif user_input == "2": #buy efficiency upgrade
            if gold >= efficiency_price:
                gold -= efficiency_price
                efficiency_price += 2
                starting_actions += 1
                print("upgraded efficiency")
            else:
                print("\nnot enough gold")

        elif user_input == "3": #buy strength upgrade
            if gold >= strength_price:
                gold -= strength_price
                strength_price += 2
                player_attack += 1
                print("\nupgraded strength")
            else:
                print("\nnot enough gold")

        elif user_input == "4": #buy health upgrade
            if gold >= health_price:
                gold -= health_price
                health_price += 2
                max_health += 10
                player_health += 10
                print("\nupgraded health")
            else:
                print("\nnot enough gold")

        elif user_input == "5": #buy random upgrade
            if gold >= random_upgrade_price:
                gold -= random_upgrade_price
                random_upgrade_price += 2
                random_upgrade = random.randint(1,4)
                if random_upgrade == 1:
                    speed += 1
                    print("\nupgraded speed")
                elif random_upgrade == 2:
                    starting_actions += 1
                    print("upgraded efficiency")
                elif random_upgrade == 3:
                    player_attack += 1
                    print("\nupgraded strength")
                elif random_upgrade == 4:
                    max_health += 10
                    player_health += 10
                    print("\nupgraded health")

        elif user_input == "6": #buy strength potion 
            if gold >= strength_potion_price:
                gold -= strength_potion_price
                strength_potion_price += 1
                inventory.append("strength potion")
                print("\ngained strength potion")
            else:
                print("\nnot enough gold")
                
        elif user_input == "7": #buy health potion
            if gold >= health_potion_price:
                gold -= health_potion_price
                health_potion_price += 1
                inventory.append("health potion")
                print("\ngained health potion")
            else:
                print("\nnot enough gold")
                
        elif user_input == "8": #buy trap
            if gold >= trap_price:
                gold -= trap_price
                trap_price += 2
                inventory.append("trap")
                print("\ngained trap")
        
        elif user_input == "9": #sell wood
            if inventory.count("wood") > 0:
                inventory.remove("wood")
                gold += 2
                print("\ngained 2 gold")
            else:
                print("\nyou have no wood")
                
        elif user_input == "10": #sell rocks
            if inventory.count("rock") > 0:
                inventory.remove("rock")
                gold += 3
                print("\ngained 3 gold")
            else:
                print("\nyou have no rocks")
                
        elif user_input == "11":
            break
        time.sleep(1)


#---------------------------------
#function to interact with environment
#---------------------------------
def interact(place):
    global inventory
    global time_of_day
    global actions
    global player_x
    global player_y
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
        if time_of_day == "day":
            shop(inventory.count("gold"))
        else:
            print("\nthe shop is closed for the night")
            actions +=1
    else:
        actions += 1
        print("\nthere's nothing here")
        if place != "vv" and inventory.count("trap") > 0: #can place a trap on an empty square
            print("place trap? (y/n)")
            user_input = input()
            if user_input == "y":
                inventory.remove("trap")
                map[player_y][player_x] = "v "
                actions -= 1
                print("placed trap")
            
    return False


#---------------------------------
#function for movement
#---------------------------------
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
                player_moves = input(f"\nwhere would you like to move? type 1 letter (you have {max_moves-i} moves left)\nn for north\ne for east\ns for south\nw for west\nto not move, type -\nNOTE THE COMPASS\nyour answer here\n").strip().lower()
                if len(player_moves) == 1: #user moves 1 place at a time_of_day
                    if player_moves == "n":
                        position_change[0] -= 1
                    elif player_moves == "e":
                        position_change[1] += 1
                    elif player_moves == "s":
                        position_change[0] += 1
                    elif player_moves == "w":
                        position_change[1] -= 1
                    elif player_moves == "-":
                        continue_moving = False
                    else:
                        print("invalid input")
                        break
                else:
                    print("invalid input")
                    continue
            player_position[player_y][player_x] = "  " #remove the previous x
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
            player_position[player_y][player_x]= "⬜"
            position_change = [0, 0]
            break


#---------------------------------
#function to make the map
#---------------------------------
def display_map():
    global player_health
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
            print(f"{player_position[y][x]}|", end="")

        if y == 0:
            print("   W + E",end="")
            print("\n+----+----+----+----+----+----+----+     S")

        elif y == 1:
            print(f"\n+----+----+----+----+----+----+----+ TIME: {time_of_day}")
        elif y == 2:
            print(f"\n+----+----+----+----+----+----+----+ DAY {days_passed} {win}")
        else:
            print("\n+----+----+----+----+----+----+----+")
    print(f"""KEY:
$ - Shop       Oo - rocks
? - treasure   /\\ - tree
v - trap      ⬜ - you
you have {actions} actions left
""")
    print(f"\nHEALTH: {player_health}")
    display_inventory()


#---------------------------------
#introduction
#---------------------------------
print("This game doesn't really have a goal, other than surviving as long as possible. You technically win if you survive for more than five days, but it continues. This game is infinite, so long as you keep surviving.")
user_input = ""
while user_input == "":
    user_input = input("type anything to start: ")
#---------------------------------
#run everythng
#---------------------------------
setup()
while True:
    print("\033c")
    if days_passed % 3 == 0 and actions == 0 and time == "day": #reset board every 3 days
        setup()
    
    display_map()
    print("""\nwhat do you do? type:
1 to move - move somewhere else on the map
2 to shop/gather resources - get stuff depending on where you are, and have the option to buy and sell stuff at the shop
3 to rest - do nothing, but heal some health
4 for additional knowlege (doesn't count as an action)""")
    user_input = input()
    if user_input == "1": #if user input is 1, player moves
        movement(speed)
        actions -= 1
        #at night, there is a chance to be attacked while doing things
        if time_of_day == "night" and random.randint(1, 3) == 3:
            if not combat():
                break
            else:
                for i in range(random.randint(1,5)):
                    inventory.append("gold")

    elif user_input == "2": #if user input is 2, player can gather things
        if interact(map[player_y][player_x]):
            map[player_y][player_x] = "  "
        actions -= 1
        #at night, there is a chance to be attacked while doing things
        if time_of_day == "night" and random.randint(1, 3) == 3:
            if not combat():
                break
            else:
                for i in range(random.randint(1,5)):
                    inventory.append("gold")

    elif user_input == "3": #if user input is 4, gain health, can't go over max health
        health_gain = random.randint(0, max_health//10)
        if player_health + health_gain > max_health:
            while player_health + health_gain > max_health:
                health_gain -= 1
        player_health += health_gain
        print(f"\ngained {health_gain} health\nyou now have {player_health} health")
        actions -= 1
    
    elif user_input == "4": #explain anything confusing
        print("""EXTRA INFO:
There isn't really a goal: the game continues infinitely
You technically win if you survive for 6 days

I'm not sure what else to say

I lost the game""")
        
    else:
        print("\ninvalid input")
    if actions == 0: #change time if user has no more actions
        print("\033c")
        display_map()
        actions = starting_actions
        print("\nyou have no more actions")
        if time_of_day == "day":
            time_of_day = "night"
        else:
            time_of_day = "day"
            days_passed += 1
        time.sleep(2)
        print(f"\nit is now {time_of_day}")
        time.sleep(2)

    if days_passed > 5: #to add a win condition, you technically win if you survive for 5 days
        win = "(you technically won)"

print(f"\n\n\n\n\n\nthanks for playing!\nyou survived {days_passed} days")