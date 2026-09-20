from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.config(background="#FC9D9A")
root.title("The Memoriser")

heading_lbl = Label(root, text="Memoriser", background="#FC9D9A", fg="#501C00", font=("Constantia", 30, "bold"))
heading_lbl.pack()

open_btn = Button(root, text="OPEN", background="#0B4C52", fg="#380000", font=("Calibri", 16, "bold"), width=15)
open_btn.pack(side=LEFT, padx=5, pady=5)

delete_btn = Button(root, text="DELETE", background="#0b4c52", fg="#380000", font=("Calibri", 16, "bold"), width=15)
delete_btn.pack(side=RIGHT, padx=5, pady=5)

add_btn = Button(root, text="ADD", bg="#53777A", fg="#1A0101", font=("Calibri", 16, "bold"), width=15)
add_btn.pack(padx=5, pady=5)

input_box = Entry(root, width=35, justify="center")
input_box.pack(padx=5, pady=5)

save_btn = Button(root, text="SAVE", background="#53777A", fg="#1a0101", font=("Calibri", 16, "bold"), width=15)
save_btn.pack(padx=5, pady=5)

frame = Frame(root)
frame.pack(side=RIGHT)
scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.pack(side=RIGHT, fill=Y)

root.mainloop()