def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_draw(board):
    return all(cell != " " for row in board for cell in row)


def get_move(player, board):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0-2): ").split())
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    return row, col
                else:
                    print("Cell already taken. Try again.")
            else:
                print("Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter two numbers between 0 and 2.")


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Welcome to Tic-Tac-Toe!")

    for turn in range(9):
        print_board(board)
        current_player = players[turn % 2]
        row, col = get_move(current_player, board)
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

    print_board(board)
    print("It's a draw!")


if __name__ == "__main__":
    play_game()
