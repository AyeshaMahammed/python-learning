import os
import random

def roll_dice_game():
    no_of_attempts = 0
    log_folder = "logs"
    log_file = os.path.join(log_folder, "rolls.txt")

    # Create folder if it doesn't exist
    if not os.path.exists(log_folder):
        os.mkdir(log_folder)

    # Open the file for writing
    with open(log_file, "w") as file:
        print("Rolling the dice...")

        while True:
            roll = random.randint(1, 6)
            no_of_attempts += 1
            log_line = f"Roll {no_of_attempts}: {roll}\n"
            print(log_line.strip())  # Print without newline
            file.write(log_line)

            if roll == 6:
                break

    print(f"\nIt took {no_of_attempts} rolls to get a 6! Check {log_file} for details.")

# Run the game
roll_dice_game()
