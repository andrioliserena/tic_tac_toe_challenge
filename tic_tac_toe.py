# The 8 ways to get three in a row: 3 rows, 3 columns, 2 diagonals
WINNING_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6],
]

def create_board():
    """Creates an empty Tic Tac Toe board: a list of 9 empty squares."""
    board = []
    for square in range(9):
        board.append(" ")
    return board

def print_board(board):
    """Prints the current state of the Tic Tac Toe board."""
    for start in [0, 3, 6]:
        print(f" {board[start]} | {board[start + 1]} | {board[start + 2]} ")
        if start < 6:
            print("---+---+---")
    print()

def choose_player():
    """Prompts the user to choose their player symbol (X or O)."""
    while True:
        choice = input("Player 1, choose X or O: ").strip().upper()
        if choice == "X" or choice == "O":
            print(f"Player 1 is {choice}, Player 2 is {switch_player(choice)}.")
            print()
            return choice
        print("Invalid input, please type X or O.")

def ask_move(board, player):
    """Asks the current player for their move and updates the board."""
    while True:
        answer = input(f"Player {player}, choose a square (1-9): ").strip()
        if answer not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Please enter a number from 1 to 9")
        elif board[int(answer) - 1] != " ":
            print("That square is taken, choose another")
        else:
            board[int(answer) - 1] = player
            print()
            return

def check_winner(board):
    """Checks if there is a winner on the board.

    Returns the winning symbol ("X" or "O"), or None if nobody has won yet.
    """
    for line in WINNING_LINES:
        a, b, c = line
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None

def check_draw(board):
    """Checks if the game is a draw (no empty spaces left)."""
    for square in board:
        if square == " ":
            return False
    return True

def switch_player(player):
    """Switches the current player from X to O or O to X."""
    if player == "X":
        return "O"
    else:
        return "X"

def play_round():
    """Plays one round of Tic Tac Toe, with the players taking turns."""
    board = create_board()
    player = choose_player()
    while not check_draw(board):
        ask_move(board, player)
        print_board(board)
        if check_winner(board):
            print(f"Player {player} wins!")
            return
        player = switch_player(player)
    print("It's a draw!")

def main():
    """Main function to run the Tic Tac Toe game."""
    print("Welcome to Tic-Tac-Toe!")
    print("Take turns placing your symbol. Three in a row wins.")
    print("The squares are numbered like this:")
    print_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    playing = True
    while playing:
        play_round()
        again = input("Play again? (y/n): ")
        playing = again.lower() == "y"
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
