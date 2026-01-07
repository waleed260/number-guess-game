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

## Controls

- Enter your guess and press Enter to submit
- Use the dropdown to change difficulty at any time
- Click "New Game" to start a new game with the same difficulty

## Game Rules

- The computer generates a random number based on the difficulty level
- Easy: Number between 1-50 with 10 lives
- Medium: Number between 1-100 with 7 lives
- Hard: Number between 1-200 with 5 lives
- Each incorrect guess reduces your lives by 1
- Game ends when you guess correctly or run out of lives
- Your best score (fewest attempts) is saved between sessions

## File Structure

```
num_guess/
├── src/
│   └── num_guess/
│       ├── __init__.py
│       └── main.py          # Main game file
└── highscore.txt            # High score storage (auto-generated)
```

## Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python installations)

## License

This project is created for educational purposes and can be used freely.