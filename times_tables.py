from tkinter import *
from tkinter import ttk

def table():
    calculation = ""
    for i in range(1, endVal.get() + 1):
        prod = num.get() * i
        calculation += f"{num.get()} x {i} = {prod} \n"

    display_lbl.configure(text=calculation)

root = Tk()
root.config(background="#0000ff")

title_lbl = Label(root, text="Times tables", bg="#0000ff", fg="#fb8b24", font=("Arial", 35, "bold"))
title_lbl.grid(row=0, column=0, columnspan=3, pady=25)

number_lbl = Label(root, text="Number and range: ", bg="#0000ff", fg="#ffd60a", font=("Arial", 15, "bold"))
number_lbl.grid(row=1, column=0, padx=10)

# Combobox (dropdown) creation
num = IntVar()
numbers_box = ttk.Combobox(root, textvariable=num, width=6, state="readonly")
numbers_box.grid(row=1, column=1)
numbers_box["values"] = tuple(range(101))

# Radio buttons
endVal = IntVar()
r10 = Radiobutton(root, text="10", variable=endVal, value=10, bg="#0000ff", fg="#ffffff", selectcolor="red")
r10.grid(row=1, column=2)
r20 = Radiobutton(root, text="20", variable=endVal, value=20, bg="#0000ff", fg="#ffffff", selectcolor="red")
r20.grid(row=2, column=2)
r30 = Radiobutton(root, text="30", variable=endVal, value=30, bg="#0000ff", fg="#ffffff", selectcolor="red")
r30.grid(row=3, column=2)
endVal.set(10)

generate_btn = Button(root, text="GENERATE", bg="#999999", fg="#000000", font=("Arial", 10, "bold"), width=12, command=table)
generate_btn.grid(row=4, column=0, columnspan=2)

display_lbl = Label(root, text="", bg="#0000ff", fg="#787878", font=("Arial", 10, "bold"))
display_lbl.grid(row=5, column=0, pady=25)

root.mainloop()