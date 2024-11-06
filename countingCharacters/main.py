#Alec George Skill Practice: Counting Characters

#will generate a random grid of letters, display it, and show how many of each letter there is
#needs random for random letters
import random

#user input for grid size
while True:
    try:
        width = int(input("\nhow wide is the grid? "))
        break
    except ValueError:
        print("invalid input")
while True:
    try:
        height = int(input("\nhow tall is the grid? "))
        break
    except ValueError:
        print("invalid input")

#variable for grid, starts blank
grid = []

#fill the grid with letters
for x in range(height):
    grid.append([])
    for y in range(width):
        grid[x].append(chr(random.randint(65,90)))

print("\n")
#print the grid
for x in range(height):
    for y in range(width):
        print(grid[x][y], end = "   ")
    print("\n")

#list amount of each letter
letters = []
for x in range(height): #first put all letters into a sorted list
    for y in range(width):
        letters.append(grid[x][y])
letters.sort()

for y in range(65, 91): #count amount of letters
    if letters.count(chr(y)) > 0:
        print(f"{chr(y)}: {letters.count(chr(y))}", end= " ")