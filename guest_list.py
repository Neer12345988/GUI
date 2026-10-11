from tkinter import *

def add():
    name = name_box.get()
    guest_list.insert(END, name)
    name_box.delete(0, END)

def remove():
    name = guest_list.curselection()
    if name:
        guest_list.delete(name)

root = Tk()
root.config(background="#D35955")
root.title("Party guest list")
root.geometry("1000x1000")

heading = Label(root, text="Guest list", background="#d35955", fg="#69D2E7", font=("Comic Sans MS", 30, "bold"))
heading.pack(pady=15)

frame = Frame(root, background="#d35955")
frame.pack()

frame2 = Frame(root)

name_box = Entry(frame, width=40, justify="center")
name_box.pack(side=LEFT, padx=10)

remove_btn = Button(frame, text="REMOVE", bg="#ff3737", fg="#000000", font=("Arial", 15, "bold"), width=10, command=remove)
remove_btn.pack(side=RIGHT, padx=10)

add_btn = Button(frame, text="ADD", bg="#00ff00", fg="#000000", font=("Arial", 15, "bold"), width=10, command=add)
add_btn.pack(side=RIGHT, padx=10)

guest_list = Listbox(root, width=90)
guest_list.pack(pady=20)





root.mainloop()