# Number Guessing Game

A professional number guessing game built with Python and Tkinter featuring multiple difficulty levels, lives system, and high score tracking.

## Features

- **Difficulty Levels**: Choose from Easy (1-50, 10 lives), Medium (1-100, 7 lives), or Hard (1-200, 5 lives)
- **Lives System**: Visual "Lives Left" counter that decreases with every wrong guess
- **High Score Tracker**: Saves and displays the best (lowest) attempts score using a highscore.txt file
- **Modern UI**: Dark theme with background color #2C3E50 and white text
- **Pop-up Alerts**: Shows "Game Over" or "You Win" messages with final score
- **Input Validation**: Ensures only integers are accepted with warnings for out-of-range numbers

## Installation

1. Make sure you have Python 3 installed on your system
2. The game uses only built-in Python libraries (tkinter, random, os), so no additional packages are required

## How to Play

1. Run the game using Python: `python src/num_guess/main.py`
2. Select your preferred difficulty level from the dropdown menu
3. Enter your guess in the input field and click "Submit Guess" or press Enter
4. The game will tell you if your guess is too high or too low
5. You have a limited number of lives based on difficulty level
6. Try to guess the number in as few attempts as possible to beat your high score



