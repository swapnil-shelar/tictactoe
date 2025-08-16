## Show info player1 with X
## show info player2 with O

def show_info():
    print(f"Player1 with symbol X")
    print(f"Player2 with symbol O")

#Display blank board
def display_board(row):
    print("Current Board:")
    print("--------------")
    print(" | " + row[0] + " | " + row[1] + " | " + row[2] + " |")
    print("--------------")
    print(" | " + row[3] + " | " + row[4] + " | " + row[5] + " |")
    print("--------------")
    print(" | " + row[6] + " | " + row[7] + " | " + row[8] + " |")
    print("--------------")

# take input from players
def take_input(player):
    while True:
        try:
            position = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid input. Please enter a number between 1 and 9.")
            else:
                return position
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Switch players
def switch_player(current_player):
    return 'player1' if current_player == 'player2' else 'player2'

# check if the game is over
def is_game_over(board):
    # This function would check for win conditions or draw (not implemented in this snippet)
    if ' ' not in board:
        print("It's a draw!")
        return True
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
        (0, 4, 8), (2, 4, 6)              # diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            print(f"Player {'player1' if board[condition[0]] == 'X' else 'player2'} wins!")
            return True
    return False

# start the game
def start_game():
    current_player = 'player1'
    while True:
        display_board(board)
        position = take_input(current_player)
        
        if board[position] != ' ':
            print("This position is already taken. Try again.")
            continue
        
        board[position] = 'X' if current_player == 'player1' else 'O'
        if is_game_over(board):
            display_board(board)
            break

        current_player = switch_player(current_player)


board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']
player1 = 'X'
player2 = 'O'
show_info()
start_game()