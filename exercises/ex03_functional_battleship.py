"""EX03 - Functional Battleship!"""


__author__ = "730665579"

import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(size: int, col_or_row: str) -> int:
    """Prompt user to input their guess for column or row."""
    assert col_or_row == "row" or col_or_row == "column"
    row_or_col_choice: int = int(input(f"Guess a {col_or_row}: "))
    # Ensure the user's guess is within the grid size.
    while row_or_col_choice < 1 or row_or_col_choice > size: 
        row_or_col_choice = int(input(f"The grid is only {size} by {size}. Try again: "))
    return row_or_col_choice


def print_grid(size: int, row_guess: int, col_guess: int, correct: bool) -> None:
    """Print the grid with the user's guesses marked."""
    # Determine the symbol to represent the guess.
    guessbox: str = RED_BOX if correct else WHITE_BOX
    row_counter = 1
    # Loop through each row of the grid.
    while row_counter <= size:
        row_string: str = ""
        column_counter: int = 1
        # Loop through each column of the grid.
        while column_counter <= size:
            # Mark the guessed location with the right symbol.
            if column_counter == col_guess and row_counter == row_guess:
                row_string += guessbox
            else:
                row_string += BLUE_BOX
            column_counter += 1
        row_counter += 1
        print(row_string)


def correct_guess(col_secret: int, row_secret: int, col_guess: int, row_guess: int) -> bool:
    """Check if the user's guess matches the secret ship location."""
    return col_guess == col_secret and row_guess == row_secret


def main(size: int, col_secret: int, row_secret: int) -> None:
    """Run the main game loop."""
    count: int = 1
    # Iterate through each turn.
    while count <= 5:
        print(f'=== Turn {count}/5 ===')
        # Get user's guesses for column and row.
        row_guess = input_guess(size, 'row')
        col_guess = input_guess(size, 'column')
        # Check if the guess is correct.
        correct = correct_guess(col_secret, row_secret, col_guess, row_guess)
        # Print the grid with the user's guess marked.
        print_grid(size, col_guess, row_guess, correct)
        # Provide feedback based on correctness of the guess.
        if correct:
            print('Hit!')
            print(f'You won in {count}/5 turns!')
            return  # Exit the function when the guess is correct
        else:
            print('Miss!')
            count += 1
    if correct is not True:
        print('X/5 - Better luck next time!')


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))