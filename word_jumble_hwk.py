from tkinter import *
import random
import tkinter.messagebox

root = Tk()
root.geometry("500x500+500+150")
root.config(background="#FFA908")

score = 0
lives = 3


heading = Label(root, text="Anagrams!", bg="#ffa908", fg="#00003B", font=("Comic Sans MS", 30, "bold"))
heading.pack()

scorelbl = Label(root, text=f"Words: {score}", bg="#FFA908", fg="#023316", font=("Times New Roman", 18))
scorelbl.pack()

liveslbl = Label(root, text=f"Lives: {lives}", bg= "#FFA908", fg="black", font=("Times New Roman", 18))
liveslbl.pack()

anagram = Label(root, bg="#ffa908", fg="#FFFFFF", font=("Verdana", 25))
anagram.pack()

guess = StringVar()
guess_box = Entry(root, font=("Verdana", 25), textvariable=guess, justify="center")
guess_box.pack()

root.mainloop()