from tkinter import *
import random

root = Tk()
root.geometry("850x300")
root.config(background="#000000")

player_score = 0
computer_score = 0

def computer_wins():
    global player_score, computer_score
    computer_score += 1
    winner_lbl.config(text="HAHA I WIN >:)")
    player_score_lbl.config(text=f"Your score: {player_score}")
    computer_score_lbl.config(text=f"My score: {computer_score}")

def player_wins():
    global player_score, computer_score
    player_score += 1
    winner_lbl.config(text="Dammit. You won.")
    player_score_lbl.config(text=f"Your score: {player_score}")
    computer_score_lbl.config(text=f"My score: {computer_score}")

def tie():
    global player_score, computer_score
    winner_lbl.config(text="How about that. It's a tie.")
    player_score_lbl.config(text=f"Your score: {player_score}")
    computer_score_lbl.config(text=f"My score: {computer_score}")

heading_lbl = Label(root, text="ROCK, PAPER, SCISSORS SHOOTOUT", bg="#000000", fg="#b00d0d", font=("Constantia", 20, "bold"))
heading_lbl.pack()
winner_lbl = Label(root, text="Let the games begin", bg = "#000000", fg="#b00d0d", font=("Constantia", 15, "bold"))
winner_lbl.pack()

frame = Frame(root, bg="#000000")
frame.pack()

player_options = Label(frame, text="Available weapons:", bg="#000000", fg="#089cf2", font=("Constantia", 14, "bold"))
player_options.grid(row=0, column=0, pady=8)

rock_btn = Button(frame, text="ROCK", width=15, bg="#4f554a", fg="#000000", font=("Constantia", 14, "bold"))
rock_btn.grid(row=1, column=1, padx=8, pady=5)
paper_btn = Button(frame, text="PAPER", width=15, bg="#eef3eb", fg="#000000", font=("Constantia", 14, "bold"))
paper_btn.grid(row=1, column=2, padx=8, pady=5)
scissors_btn = Button(frame, text="SCISSORS", width=15, bg="#ff0000", fg="#000000", font=("Constantia", 14, "bold"))
scissors_btn.grid(row=1, column=3, padx=8, pady=5)

score_lbl = Label(frame, text="Score: ", bg="#000000", fg="#089cf2", font=("Constantia", 14, "bold"))
score_lbl.grid(row=3, column=0)

player_choice_lbl = Label(frame, text="You chose: ", bg="#000000", fg="#00fe48", font=("Constantia", 14, "bold"))
player_choice_lbl.grid(row=4, column=1, pady=5)
player_score_lbl = Label(frame, text="Your score: ", bg="#000000", fg="#00fe48", font=("Constantia", 14, "bold"))
player_score_lbl.grid(row=4, column=2, pady=5)

computer_choice_lbl = Label(frame, text="I chose: ", bg="#000000", fg="#fe0048", font=("Constantia", 14, "bold"))
computer_choice_lbl.grid(row=5, column=1, pady=5)
computer_score_lbl = Label(frame, text="My score: ", bg="#000000", fg="#fe0048", font=("Constantia", 14, "bold"))
computer_score_lbl.grid(row=5, column=2, pady=5)

root.mainloop()