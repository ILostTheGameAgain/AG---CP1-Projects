#Alec George Raid: Character Creator


#user will select class, race, and name, and computer will tell health, strength, dexterity, and intelligence

#list of races, along with list with stats
races = ["human", "elf", "dwarf", "troll", "goat...?"]
race_health = [20, 15, 30, 80, 10000]
race_strength = [5, 7, 10, 20, 10000]
race_dexterity = [10, 30, 7, 1, 10000]
race_intelligence = [30, 50, 40, 0, 10000]

#list of classes, multiplies the stats of race
classes = ["warrior", "chef", "preist", "smith", "ranger"]
class_health = [1.1, 2, 1, 1.3, 0.9]
class_strength = [2, 0.9, 1, 1.2, 1.5]
class_dexterity = [1, 1.2, 1, 0.9, 2]
class__intelligence = [0.9, 1.1, 2, 1.1, 1]

#ask for character race
print("what is the race of this character?")
for x in races:
    print(x)
race = input("your answer here: ")
while True:
    if race in races:
        break

#ask for character class


#ask for character name
name = input("what is the name of this character? ")