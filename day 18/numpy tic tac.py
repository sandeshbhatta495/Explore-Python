import numpy as np
board = np.full((3, 3), " ")

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
def player_move(board, symbol):
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    if board[row][col] == " ":
        board[row][col] = symbol
    else:
        print("Cell already occupied, try again!")
        player_move(board, symbol)

def check_winner(board, symbol):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2-i] == symbol for i in range(3)):
        return True
    return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    for turn in range(9):
        symbol = "X" if turn % 2 == 0 else "O"
        print(f"Player {symbol}'s turn")
        player_move(board, symbol)
        print_board(board)
        if check_winner(board, symbol):
            print(f"Player {symbol} wins!")
            return
    print("It's a draw!")

