import tkinter as tk
from tkinter import ttk, messagebox
import random
import os

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Dark theme colors
        self.bg_color = "#2C3E50"
        self.text_color = "white"
        self.button_color = "#34495E"
        self.accent_color = "#3498DB"
        self.success_color = "#27AE60"
        self.error_color = "#E74C3C"

        # Configure root
        self.root.configure(bg=self.bg_color)

        # Game variables
        self.target_number = 0
        self.lives = 0
        self.max_lives = 0
        self.difficulty = "Medium"  # Default
        self.high_score = self.load_high_score()

        # Create UI
        self.create_widgets()
        self.set_difficulty("Medium")  # Set initial difficulty

    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="Number Guessing Game",
            font=("Arial", 24, "bold"),
            fg=self.text_color,
            bg=self.bg_color
        )
        title_label.pack(pady=(20, 10))

        # High Score Display
        self.high_score_label = tk.Label(
            self.root,
            text=f"Best Score: {self.high_score if self.high_score != float('inf') else 'N/A'}",
            font=("Arial", 14),
            fg=self.text_color,
            bg=self.bg_color
        )
        self.high_score_label.pack(pady=(0, 10))

        # Difficulty Selection
        difficulty_frame = tk.Frame(self.root, bg=self.bg_color)
        difficulty_frame.pack(pady=10)

        tk.Label(
            difficulty_frame,
            text="Select Difficulty:",
            font=("Arial", 12),
            fg=self.text_color,
            bg=self.bg_color
        ).pack(side=tk.LEFT, padx=(0, 10))

        self.difficulty_var = tk.StringVar(value=self.difficulty)
        difficulty_dropdown = ttk.Combobox(
            difficulty_frame,
            textvariable=self.difficulty_var,
            values=["Easy", "Medium", "Hard"],
            state="readonly",
            width=10,
            font=("Arial", 12)
        )
        difficulty_dropdown.pack(side=tk.LEFT)
        difficulty_dropdown.bind("<<ComboboxSelected>>", self.on_difficulty_change)

        # Lives Display
        self.lives_label = tk.Label(
            self.root,
            text=f"Lives Left: {self.lives}",
            font=("Arial", 14),
            fg=self.text_color,
            bg=self.bg_color
        )
        self.lives_label.pack(pady=(10, 5))

        # Progress bar for lives
        self.lives_progress = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=300,
            mode="determinate"
        )
        self.lives_progress.pack(pady=(0, 10))

        # Game info
        self.game_info = tk.Label(
            self.root,
            text="",
            font=("Arial", 12),
            fg=self.text_color,
            bg=self.bg_color
        )
        self.game_info.pack(pady=(0, 10))

        # Input Frame
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(pady=20)

        tk.Label(
            input_frame,
            text="Enter your guess:",
            font=("Arial", 12),
            fg=self.text_color,
            bg=self.bg_color
        ).pack()

        self.guess_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            justify="center",
            width=15
        )
        self.guess_entry.pack(pady=(5, 10))
        self.guess_entry.bind("<Return>", self.make_guess)

        # Guess Button
        self.guess_button = tk.Button(
            self.root,
            text="Submit Guess",
            command=self.make_guess,
            font=("Arial", 12, "bold"),
            bg=self.accent_color,
            fg=self.text_color,
            activebackground="#2980B9",
            activeforeground=self.text_color,
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.guess_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12),
            fg=self.text_color,
            bg=self.bg_color,
            wraplength=400
        )
        self.result_label.pack(pady=(10, 0))

        # New Game Button
        self.new_game_button = tk.Button(
            self.root,
            text="New Game",
            command=self.start_new_game,
            font=("Arial", 12, "bold"),
            bg=self.success_color,
            fg=self.text_color,
            activebackground="#219653",
            activeforeground=self.text_color,
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2"
        )
        self.new_game_button.pack(pady=(20, 0))

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        if difficulty == "Easy":
            self.max_number = 50
            self.max_lives = 10
        elif difficulty == "Medium":
            self.max_number = 100
            self.max_lives = 7
        elif difficulty == "Hard":
            self.max_number = 200
            self.max_lives = 5

        self.target_number = random.randint(1, self.max_number)
        self.lives = self.max_lives

        # Update UI
        self.update_lives_display()
        self.game_info.config(text=f"Guess a number between 1 and {self.max_number}")
        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)

    def on_difficulty_change(self, event):
        self.set_difficulty(self.difficulty_var.get())

    def make_guess(self, event=None):
        try:
            guess = int(self.guess_entry.get().strip())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid integer.")
            return

        if guess < 1 or guess > self.max_number:
            messagebox.showwarning(
                "Out of Range",
                f"Please enter a number between 1 and {self.max_number}."
            )
            return

        # Process the guess
        if guess == self.target_number:
            # Player wins
            attempts = self.max_lives - self.lives + 1
            self.result_label.config(text=f"🎉 Congratulations! You guessed it in {attempts} attempts!", fg=self.success_color)

            # Update high score if needed
            if attempts < self.high_score:
                self.high_score = attempts
                self.save_high_score()
                self.high_score_label.config(text=f"Best Score: {self.high_score}")
                messagebox.showinfo("New High Score!", f"🎉 New High Score! {attempts} attempts!")
            else:
                messagebox.showinfo("You Win!", f"🎉 You won in {attempts} attempts!")

            self.guess_button.config(state="disabled")
        else:
            self.lives -= 1
            self.update_lives_display()

            if self.lives <= 0:
                # Game over
                messagebox.showinfo(
                    "Game Over",
                    f"Game Over! The number was {self.target_number}. Better luck next time!"
                )
                self.guess_button.config(state="disabled")
                self.result_label.config(text=f"Game Over! The number was {self.target_number}", fg=self.error_color)
            else:
                # Give hint
                if guess < self.target_number:
                    hint = "Higher! Try a bigger number."
                else:
                    hint = "Lower! Try a smaller number."

                self.result_label.config(text=f"Incorrect! {hint} You have {self.lives} lives left.", fg=self.error_color)

        self.guess_entry.delete(0, tk.END)

    def update_lives_display(self):
        self.lives_label.config(text=f"Lives Left: {self.lives}")
        # Update progress bar
        progress = (self.lives / self.max_lives) * 100
        self.lives_progress['value'] = progress

    def start_new_game(self):
        self.set_difficulty(self.difficulty)
        self.guess_button.config(state="normal")

    def load_high_score(self):
        try:
            if os.path.exists("highscore.txt"):
                with open("highscore.txt", "r") as f:
                    content = f.read().strip()
                    if content:
                        return int(content)
            return float('inf')  # Return infinity if no high score exists
        except:
            return float('inf')

    def save_high_score(self):
        try:
            with open("highscore.txt", "w") as f:
                f.write(str(self.high_score))
        except:
            pass  # If we can't save, just continue

def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    