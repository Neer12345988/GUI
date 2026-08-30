from tkinter import *
import random
import tkinter.messagebox

root = Tk()
root.geometry("400x350")
root.config(background="#a2d2ff")

number = random.randint(1, 20)

def confirm():
    name = name_box.get()
    tkinter.messagebox.showinfo("Name", f"Hello {name}. Guess my number. It's between 1 and 20.")
    
def check_num():
    guess = number_box.get()
    guess = int(guess)
    if guess > number:
        tkinter.messagebox.showinfo("Guess too high", "That guess was higher than my number")
    if guess < number:
        tkinter.messagebox.showinfo("Guess too low", "That guess was lower than my number")
    if guess == number:
        tkinter.messagebox.showinfo("Congratulations!", "You guessed my number!")

heading_lbl = Label(root, text="Guess my number", bg="#a2d2ff", fg="#000000", font= ("Arial", 20, "bold"))
heading_lbl.pack()

name_lbl = Label(root, text="Name: ", bg="#a2d2ff", fg="#363636", font=("Arial", 16, "bold"))
name_lbl.place(x=10, y=60)
name_box = Entry(root, width=20)
name_box.place(x=100, y=65)
ok_btn = Button(root, text="OK", bg="#c7c3c3", fg="#000000", width=5, font=("Arial", 16, "bold"), command=confirm)
ok_btn.place(x=250, y=60)

number_lbl = Label(root, text="Number: ", bg="#a2d2ff", fg="#363636", font=("Arial", 16, "bold"))
number_lbl.place(x=10, y=180)
number_box = Entry(root, width=20)
number_box.place(x=120, y=185)
number_btn = Button(root, text="GUESS", bg="#c7c3c3", fg="#000000", width=8, font=("Arial", 16, "bold"), command=check_num)
number_btn.place(x=270, y=180)


root.mainloop()