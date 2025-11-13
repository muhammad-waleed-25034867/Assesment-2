import tkinter as tk
import random

# Create main window
root = tk.Tk()
root.title("Number Hunt")
root.geometry("350x400")
root.resizable(False, False)
root.config(bg="#454F60")

# Random number
secret_number = random.randint(1, 50)
attempts = 0

# Title
title_label = tk.Label(root, text="Guess Number (1 - 50)", font=("Arial", 14, "bold"), bg="#E8F0FE")
title_label.pack(pady=10)

# Input box
entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#E8F0FE")
result_label.pack(pady=10)

# Attempts label
attempts_label = tk.Label(root, text="Attempts: 0", font=("Arial", 11), bg="#E8F0FE")
attempts_label.pack(pady=5)

# Check guess function
def check_guess():
    global attempts
    guess = entry.get()
    if not guess.isdigit():
        result_label.config(text="Please enter a valid number!", fg="red")
        return
    guess = int(guess)
    attempts += 1
    attempts_label.config(text=f"Attempts: {attempts}")
    
    if guess < secret_number:
        result_label.config(text="Too low! Try again.", fg="blue")
    elif guess > secret_number:
        result_label.config(text="Too high! Try again.", fg="orange")
    else:
        result_label.config(text=f"🎉 Correct! The number was {secret_number}.", fg="green")
        guess_button.config(state="disabled")

# Restart game
def restart_game():
    global secret_number, attempts
    secret_number = random.randint(1, 50)
    attempts = 0
    result_label.config(text="", fg="black")
    attempts_label.config(text="Attempts: 0")
    entry.delete(0, tk.END)
    guess_button.config(state="normal")
    
    # Function to give even/odd hint
def even_odd_hint():
    if secret_number % 2 == 0:
        result_label.config(text="Hint: The number is even!", fg="purple")
    else:
        result_label.config(text="Hint: The number is odd!", fg="purple")
        

# Buttons
guess_button = tk.Button(root, text="Guess", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", command=check_guess)
guess_button.pack(pady=5)

restart_button = tk.Button(root, text="Restart", font=("Arial", 11, "bold"), bg="#2196F3", fg="white", command=restart_game)
restart_button.pack(pady=5)

 # Hint button
hint_button = tk.Button(root, text="Hint (Even/Odd)", font=("Arial", 11, "bold"), bg="#FFC107", fg="white", command=even_odd_hint)
hint_button.pack(pady=5)

# Quit button
quit_button = tk.Button(root, text="Quit", font=("Arial", 11, "bold"), bg="#F44336", fg="white", command=root.destroy)
quit_button.pack(pady=5)

root.mainloop()
