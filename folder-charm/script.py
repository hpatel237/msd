def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def f(board):
    return all(column != " " for row in board for column in row)


def turn():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_board(board)
    for turn in range(9):
        current_player = player[turn % 2]
        while 1:
            try:
                row, column = map(int, input(f"P {current_player}, row col (0-2): ").split())
                if board[row][column] == " ":
                    board[row][column] = current_player
                    break
                else:
                    print("Nope. Again.")
            except:
                print("Wrong. 0-2 pls.")
        print_board(board)
        if check_winner(board, player):
            print(f"P {current_player} wins!")
            return
        if f(board):
            print("Draw!")
            return
    print("Draw!")


t()

