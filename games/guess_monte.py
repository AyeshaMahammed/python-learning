#SHUFFLE LIST FUNCTION
def shuffle_list(my_list):
    import random
    random.shuffle(my_list)
    return my_list

#PLAYER GUESS FUNCTION
def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number between 0 and 2: ")
    return int(guess)

#CHECK GUESS FUNCTION
def check_guess(my_list, guess):
    if my_list[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(my_list)


#MAIN FUNCTION
#INITIAL LIST
my_list = ['','O','']
#SHUFFLE LIST
new_suffled_list = shuffle_list(my_list)
#USER GUESS
guess = player_guess()
#CHECK GUESS
check_guess(new_suffled_list, guess)


# This code is a simple guessing game where the player has to guess the position of an item in a shuffled list.
# The list is shuffled, and the player is prompted to guess the index of the item.
# If the guess is correct, a success message is displayed; otherwise, the correct list is shown.
# The game uses functions to shuffle the list, get the player's guess, and check the guess.
# The game is interactive and provides feedback to the player based on their input.
# The code is structured to be easy to read and understand, with clear function names and comments explaining each part.
# The game can be expanded or modified to include more features, such as multiple rounds, scoring, or different items to guess.
# The game is a fun way to practice basic programming concepts such as lists, functions, and user input.