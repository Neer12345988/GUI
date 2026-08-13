from tkinter import *
import random

root = Tk()
root.geometry("1000x1000")
root.config(background="#01ff23")

call = Label(root, text="What's your call?", bg="#01ff23", fg="#000000", font=("Arial", 18, "bold"))
call.grid(row=0, column=2)

heads = Button(root, text="Heads!", bg = "#ffffff", fg="#000000", font=("Arial", 18, "bold"))
heads.grid(row=1, column=1)
tails = Button(root, text="Tails!", bg="#ffffff", fg=
"#000000", font=("Arial", 18, "bold"))
tails.grid(row=1, column=3)


root.mainloop()