# Guess the number game that usues simple GUI provided 
# by the Tkinter library

import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Number Guessing Game")
        
        self.secret_number = random.randint(1, 100)
        self.attempts = 0 
        
        self.instructions_label = tk.Label(self.window, text="Try to guess the number between 1 and 100.")
        self.instructions_label.pack()
        
        self.label = tk.Label(self.window, text="Take a guess")
        self.label.pack()
        
        self.entry = tk.Entry(self.window)
        self.entry.pack()
        
        self.guess_button = tk.Button(self.window, text="Guess", command = self.check_guess)
        self.guess_button.pack()
        
    def check_guess(self):
        try:
            # Get user input for a guess
            guess = int(self.entry.get())
            self.attempts += 1
            
            # Check if the guess is correct
            if guess == self.secret_number:
                messagebox.showinfo("Result", f"Congratulations! You guessed the number after {self.attempts} attempts.")
                self.window.destroy()
            elif (guess < self.secret_number):
                messagebox.showinfo("Result", "Too low. Try again.")
            else: 
                messagebox.showinfo("Result", "Too high. Try again.")
            
        except ValueError: 
            messagebox.showinfo("Error", "Invalid input. Please enter a number between 1 and 100. ")
            
# Check if the script is run as the main program
if __name__ == "__main__":
    game = NumberGuessingGame()
    game.window.mainloop()