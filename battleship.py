from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Battleship v0.1")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    print ("Turn", turn + 1)

if guess_row == ship_row and guess_col == ship_col:
    print ("Grats, you sunk the battleship!")
    break

else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print ("Way off the mark.")
    elif(board[guess_row][guess_col] == "X"):
        print ("You already tried this location.")
    else:
        print ("You missed the ship!")
        board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
    if turn == 3:
        print ("Game Over")
    print_board(board)