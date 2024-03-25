import tkinter as tk
import random

# Function to check if a player has won
def check_win(board, player):
    for i in range(3):
        # Check rows and columns for a win
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to get empty cells on the board
def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Function to make the computer's move
def computer_move(board):
    empty_cells = get_empty_cells(board)
    if empty_cells:
        return random.choice(empty_cells)

# Function to handle player moves and game state
def make_move(row, col):
    global current_player, game_over
    if board[row][col] == " " and not game_over:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_win(board, current_player):
            status_label.config(text=f"{current_player} wins!")
            game_over = True
        elif all(board[i][j] != " " for i in range(3) for j in range(3)):
            status_label.config(text="It's a draw!")
            game_over = True
        else:
            current_player = "X" if current_player == "O" else "O"
            if current_player == "O":
                computer_row, computer_col = computer_move(board)
                make_move(computer_row, computer_col)

# Function to reset the game
def reset_game():
    global board, current_player, game_over
    board = [[" " for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state=tk.NORMAL)
    # Always start with "O" and let it make the first move
    current_player = "O"
    game_over = False
    status_label.config(text=f"{current_player}'s turn")
    if current_player == "O":
        computer_row, computer_col = computer_move(board)
        make_move(computer_row, computer_col)

# Create the main tkinter window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize the game board
board = [[" " for _ in range(3)] for _ in range(3)]

# Create a 2D list of buttons for the game cells
buttons = [[None, None, None], [None, None, None], [None, None, None]]

# Set the initial player and game state
current_player = "O"  # "O" starts first
game_over = False

# Create a label to display the game status
status_label = tk.Label(root, text=f"{current_player}'s turn", font=('Arial', 15))
status_label.grid(row=0, column=0, columnspan=3)

# Create a "Restart" button
reset_button = tk.Button(root, text="Restart", command=reset_game)
reset_button.grid(row=1, column=0, columnspan=3)

# Create buttons for the game cells and attach the make_move function to them
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=('Arial', 20), width=6, height=2,
                                  command=lambda row=i, col=j: make_move(row, col))
        buttons[i][j].grid(row=i + 2, column=j)

# Let "O" make the first move automatically
computer_row, computer_col = computer_move(board)
make_move(computer_row, computer_col)

# Start the tkinter main loop to run the game
root.mainloop()