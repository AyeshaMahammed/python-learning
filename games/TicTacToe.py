"""
2 player Tic Tac Toe game which takes initials of players and plays the game on the console.
The game is played on a 3x3 grid, and players take turns placing their initials in empty squares.
The first player to get three of their initials in a row (horizontally, vertically, or diagonally) wins the game.
The game ends in a draw if all squares are filled and no player has three initials in a row.
The game is played in the console, and the players are prompted to enter their initials and choose a square to place their initials.
The game is played in a loop until there is a winner or the game ends in a draw.
The game is implemented using a class called TicTacToe, which contains methods for initializing the game, displaying the board, checking for a winner, and playing the game.
"""

def print_board(board):
    """
    Prints the Tic Tac Toe board.
    :
    """
    print("Current board:")
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

initial_board = [" "]*9
print_board([" "]*9)

def check_winner(board):
    """
    Checks if there is a winner.
    :param board: The current state of the board.
    :return: True if there is a winner, False otherwise.
    """
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False

def check_draw(board):
    """
    Checks if the game is a draw.
    :param board: The current state of the board.
    :return: True if the game is a draw, False otherwise.
    """
    return " " not in board

def play_game():
    """
    Main function to play the Tic Tac Toe game.
    """
    board = initial_board
    player1 = input("Enter the initials of Player 1: ")
    player2 = input("Enter the initials of Player 2: ")
    current_player = player1
    while True:
        print_board(board)
        move = int(input(f"{current_player}'s turn. Choose a square (1-9): ")) - 1
        if board[move] == " ":
            board[move] = current_player
            if check_winner(board):
                print_board(board)
                print(f"{current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = player2 if current_player == player1 else player1 # Switch players here

        else:
            print("Square already taken. Try again.")

if __name__ == "__main__":
    play_game()
# This code implements a simple 2-player Tic Tac Toe game in Python.
