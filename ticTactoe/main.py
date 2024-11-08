#Alec George Tic Tac Toe

# play tic tac toe

#random computer input
import random

#title
print("""
+-----------+   +-----------+     ------          +-----------+        /\\           ------
|           |   |           |    / /  \\ \\         |           |       /  \\         / /  \\ \\
+---+   +---+   +---+   +---+   / /    +-+        +---+   +---+      / /\\ \\       / /    +-+
    |   |           |   |       | |                   |   |         / /__\\ \\      | | 
    |   |       +---+   +---+   \\ \\    +-+            |   |        / ______ \\     \\ \\    +-+
    |   |       |           |    \\ \\  / /             |   |       / /      \\ \\     \\ \\  / /
    +---+       +-----------+     ------              +---+      +-+        +-+     ------

+-----------+      ------      +-----------+     
|           |     / /  \ \\     |   ._______|
+---+   +---+    / /    \ \\    |   |____.
    |   |        | |    | |    |        |
    |   |        \ \\    / /    |   +----+
    |   |         \ \\  / /     |   +-------+
    +---+          ------      |___________|\n\n""")
#set up board
board_squares = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#function to check if someone wins
def win():
    for x in range(3): #check rows
        if board_squares[x][0] == board_squares[x][1] == board_squares[x][2]:
            return True
    for x in range(3): #check columns
        if board_squares[0][x] == board_squares[1][x] == board_squares[2][x]:
            return True
    #check diagonals
    if board_squares[0][0] == board_squares[1][1] == board_squares[2][2]:
        return True
    if board_squares[0][2] == board_squares[1][1] == board_squares[2][0]:
        return True
    return False


#function to do an action
def action(number, figure):
    global board_squares
    if number in board_squares[0]:
        board_squares[0][number-1] = figure
        return True
    elif number in board_squares[1]:
        board_squares[1][number-4] = figure
        return True
    elif number in board_squares[2]:
        board_squares[2][number-7] = figure
        return True
    else:
        if figure == "X":
            print("that square is taken")
        return False


#function to print board
def board():
    global board_squares
    print(f""" {board_squares[0][0]} | {board_squares[0][1]} | {board_squares[0][2]}
---+---+---
 {board_squares[1][0]} | {board_squares[1][1]} | {board_squares[1][2]}
---+---+---
 {board_squares[2][0]} | {board_squares[2][1]} | {board_squares[2][2]}""")


while True: #keep playing until win
    #print board
    board()
    while True:
        try:
            if action(int(input("\n what square? (type the number): ")), "X"):
                break
        except ValueError:
            print("invalid input")

    #check if user wins
    if win():
        board()
        print("X wins")
        break

    #computer chooses random square
    while True:
        if action(random.randint(1,9), "O"):
            break
    
    #check if computer wins
    if win():
        board()
        print("O wins")
        break

print("thanks for playing!")