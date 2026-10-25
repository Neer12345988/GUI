# Task: create an app where you can edit an item inside the listbox.
# Window Title: "List Editor".
# UI Elements:
# Listbox (Populate it with "Item 1", "Item 2", "Item 3" by default).
# Entry Box (Empty at start).
# Button "Update Item".
# Logic:
# Step 1: When the user clicks an item in the Listbox, that text should appear in the Entry box (Optional: you can use a "Load" button if clicking is too hard).
# Step 2: The user changes the text in the Entry box.
# Step 3: When they click "Update Item", the selected line in the Listbox is replaced by the new text from the Entry box.
# Hint: You will need listbox.delete() and listbox.insert() at the specific index.
from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("List Editor")
root.config(background="#48cae4")

def load():
    index = listbox.curselection()
    if index:
        text = listbox.get(index)
        input_box.delete(0, END)
        input_box.insert(END, text)

def update():
    index = listbox.curselection()
    if index:
        input_text = input_box.get()
        listbox.delete(index)
        listbox.insert(index, input_text)
        input_box.delete(0, END)

items = ["Item 1", "Item 2", "Item 3"]

listbox = Listbox(root, width=40)
listbox.pack(pady=20)

for i in range(3):
    listbox.insert(END, items[i])

input_box = Entry(root, width=50)
input_box.pack(pady=20)

loadbtn = Button(root, text="LOAD ITEM", bg="#32e206", fg="#000000", font=("Arial", 20, "bold"), command=load)
loadbtn.pack(pady=10)

updatebtn = Button(root, text="UPDATE ITEM", bg="#7f848e", fg="#000000", font=("Arial", 20, "bold"), command=update)
updatebtn.pack(pady=10)

root.mainloop()