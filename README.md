# Number Guessing Game
Welcome to the **Number Guessing Game**! This simple game challenges the player to guess a random number within a specified range, with a limited number of attempts.

## Game Description
The game will randomly choose a number within a specified range. The player has a limited number of attempts to guess the correct number. After each guess, the game will provide feedback on whether the guess is too high, too low, or correct. If the player guesses the number within the allowed attempts, they win; otherwise, the game reveals the correct number.

## Features
- Random number selection between 1 and 100.
- Player has 10 attempts to guess the correct number.
- Feedback on whether the guess is too high or too low.
- Handles invalid inputs gracefully (e.g., non-numeric input).
- Displays the correct number if the player fails to guess within 10 attempts.

## How to Play
1. Run the script.
2. The game will ask you to input your guess within a specified range (1 to 100).
3. After each guess, the game will tell you if your guess was too high, too low, or correct.
4. You have 10 attempts to guess the correct number.

## Requirements
- Python 3.x or later.

## Example
Here are some example outputs for different scenarios in Number Guessing Game:

### Example 1: Correct Guess
```
Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.
You have 10 attempts to guess it correctly.
Attempt 1: Enter your guess: 45
Too low! Try again.
Attempt 2: Enter your guess: 75
Too high! Try again.
Attempt 3: Enter your guess: 60
Too high! Try again.
Attempt 4: Enter your guess: 55
Too low! Try again.
Attempt 5: Enter your guess: 50
Congratulations! You guessed the number 50 correctly in 5 attempts.
```

### Example 2: Invalid Input (Non-Numeric Input)
```
Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.
You have 10 attempts to guess it correctly.
Attempt 1: Enter your guess: abc
Invalid input! Please enter a number between 1 and 100.
Attempt 2: Enter your guess: 30
Too low! Try again.
Attempt 3: Enter your guess: 35
Congratulations! You guessed the number 35 correctly in 3 attempts.
```

### Example 3: Out of Range Guess
```
Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.
You have 10 attempts to guess it correctly.
Attempt 1: Enter your guess: 150
Out of range! Please enter a number between 1 and 100.
Attempt 2: Enter your guess: 25
Too low! Try again.
Attempt 3: Enter your guess: 75
Too high! Try again.
Attempt 4: Enter your guess: 70
Congratulations! You guessed the number 70 correctly in 4 attempts.
```

### Example 4: Player Runs Out of Attempts
```
Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.
You have 10 attempts to guess it correctly.
Attempt 1: Enter your guess: 20
Too low! Try again.
Attempt 2: Enter your guess: 50
Too low! Try again.
Attempt 3: Enter your guess: 80
Too high! Try again.
Attempt 4: Enter your guess: 70
Too high! Try again.
Attempt 5: Enter your guess: 60
Too high! Try again.
Attempt 6: Enter your guess: 55
Too high! Try again.
Attempt 7: Enter your guess: 40
Too low! Try again.
Attempt 8: Enter your guess: 45
Too low! Try again.
Attempt 9: Enter your guess: 50
Too low! Try again.
Attempt 10: Enter your guess: 49
Sorry, you've used 10 attempts! The correct number was 51.
```

These are examples of typical outputs during gameplay, showing correct guesses, invalid inputs, out-of-range guesses, and when the player runs out of attempts.

## Author
- Created and maintained by **Sohag Chakraborty**  
  GitHub: [**@csesohag02**](https://github.com/csesohag02)
