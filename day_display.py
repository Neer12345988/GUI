from tkinter import *
from time import strftime

def update():
    day.config(text=f"{strftime("%A")}")

root = Tk()
root.title("Today is...")

heading = Label(root, text="Today is...", font=("Arial", 20, "bold"))
heading.pack()

day = Label(root, text=f"{strftime("%A")}", font=("Arial", 40, "bold"))
day.pack()

update()

root.mainloop()