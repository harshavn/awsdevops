def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals
    return any(
        all(cell == player for cell in row) for row in board
    ) or any(
        all(row[i] == player for row in board) for i in range(3)
    ) or all(
        board[i][i] == player for i in range(3)
    ) or all(
        board[i][2 - i] == player for i in range(3)
    )

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_move():
    while True:
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter numbers between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row, col = get_move()
        
        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
