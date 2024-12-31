"""
Created on Tue Dec 31 15:49:41 2024
Author: @csesohag02
GitHub: https://github.com/csesohag02
"""

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Define the range for the guessing game
    start_range, end_range = 1, 100
    print(f"I am thinking of a number between {start_range} and {end_range}.")
    number_to_guess = random.randint(start_range, end_range)
    
    # Maximum number of attempts
    max_attempts = 10
    print(f"You have {max_attempts} attempts to guess it correctly.")
    
    # Loop through the user's attempts
    for attempt in range(1, max_attempts + 1):
        try:
            # Get user's guess
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))

            # Check if the guess is out of range
            if guess < start_range or guess > end_range:
                print(f"Out of range! Please enter a number between {start_range} and {end_range}.")
                continue

            # Check if the guess is correct
            if guess == number_to_guess:
                print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempt} attempts.")
                break
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        
        except ValueError:
            print(f"Invalid input! Please enter a number between {start_range} and {end_range}.")
            continue

    else:
        print(f"Sorry, you've used {max_attempts} attempts! The correct number was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()


"""
Created and maintained by @csesohag02
GitHub: https://github.com/csesohag02
"""
