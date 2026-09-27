from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.config(background="#FC9D9A")
root.title("The Memoriser")

def add():
    listbox.insert(END, input_box.get())
    input_box.delete(0, END)

def remove():
    index = listbox.curselection()
    if index:
        listbox.delete(index)

def save():
    save_file = asksaveasfile(defaultextension=".txt")
    if save_file is not None:
        for item in listbox.get(0, END):
            print(item.strip(), file=save_file)
        listbox.delete(0, END)

def open():
    open_file = askopenfile(title="open file")
    if open_file is not None:
        listbox.delete(0, END)
        items = open_file.readlines()
        for item in items:
            listbox.insert(END, item.strip())

heading_lbl = Label(root, text="Memoriser", background="#FC9D9A", fg="#501C00", font=("Constantia", 30, "bold"))
heading_lbl.pack()

open_btn = Button(root, text="OPEN", background="#0B4C52", fg="#380000", font=("Calibri", 16, "bold"), width=15, command=open)
open_btn.pack(side=LEFT, padx=5, pady=5)

delete_btn = Button(root, text="DELETE", background="#0b4c52", fg="#380000", font=("Calibri", 16, "bold"), width=15, command=remove)
delete_btn.pack(side=RIGHT, padx=5, pady=5)

add_btn = Button(root, text="ADD", bg="#53777A", fg="#1A0101", font=("Calibri", 16, "bold"), width=15, command=add)
add_btn.pack(padx=5, pady=5)

input_box = Entry(root, width=35, justify="center")
input_box.pack(padx=5, pady=5)

save_btn = Button(root, text="SAVE", background="#53777A", fg="#1a0101", font=("Calibri", 16, "bold"), width=15, command=save)
save_btn.pack(padx=5, pady=5)

frame = Frame(root)
frame.pack(side=RIGHT)
scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame, width=70, yscrollcommand=scrollbar.set, background="#777777")
for i in range(1, 21):
    listbox.insert(END, f"list{i}")
listbox.pack(side=LEFT, padx=5)

scrollbar.config(command=listbox.yview)

root.mainloop()