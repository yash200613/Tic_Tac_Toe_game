import tkinter as tk
from tkinter import messagebox
import random

def check_winner():
    global winner

    winning_combinations = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in winning_combinations:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"{buttons[combo[0]]['text']} wins!")
            winner = True
            return

    # Check for draw
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        winner = True


def player_move(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = "X"
        check_winner()
        if not winner:
            root.after(500, computer_move)  # delay for realism


def computer_move():
    if winner:
        return

    empty_buttons = [i for i, button in enumerate(buttons) if button["text"] == ""]

    if empty_buttons:
        move = random.choice(empty_buttons)
        buttons[move]["text"] = "O"
        check_winner()


def restart_game():
    global winner
    winner = False
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")


# Create main window
root = tk.Tk()
root.title("Tic-Tac-Toe (Player vs Computer)")

buttons = [
    tk.Button(root, text="", font=("normal", 25), width=6, height=2,
              command=lambda i=i: player_move(i))
    for i in range(9)
]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

winner = False

restart_button = tk.Button(root, text="Restart", font=("normal", 14), command=restart_game)
restart_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

root.mainloop()
