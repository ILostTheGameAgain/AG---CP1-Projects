#Alec George Tic Tac Toe

# play tic tac toe on adjustable board

#adjustable board
while True:
    try:
        board_size = int(input("\nhow large is the board? (squares): "))
        break
    except ValueError:
        print("invalid input")

#setup board
board = []
for x in range(board_size):
    board.append([])
    for y in range(board_size):
        board[x].append("  ")

