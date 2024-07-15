def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_move(player):
    while True:
        move = input(f"Player {player}, enter your move (row and column: 1 1, 2 2, etc.): ").split()
        if len(move) == 2 and all(m.isdigit() for m in move):
            row, col = int(move[0]) - 1, int(move[1]) - 1
            if row in range(3) and col in range(3):
                return row, col
        print("Invalid move. Please try again.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row, col = get_move(current_player)
        
        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("The game is a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("This spot is already taken. Try a different spot.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()

if __name__ == "__main__":
    play_game()
