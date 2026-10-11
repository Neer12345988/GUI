from time import strftime
from tkinter import *

def time():
    current_time = strftime("%H:%M:%S %p")
    heading.config(text=current_time)
    heading.after(1000, time)

root = Tk()
root.config(background="#ECE5CE")
root.title("Digital clock")

heading = Label(root, text="", bg="#ECE5CE", fg="#232121", font=("Arial", 40, "bold"))
heading.pack(anchor="center")

time()

root.mainloop()