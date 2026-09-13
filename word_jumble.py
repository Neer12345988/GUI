from tkinter import *
import random
import tkinter.messagebox

answers = ["apple", "banana", "coconut", "durian", "fruit", "grapefruit", "horseradish", "jam", "kiwi", "mango", "orange", "pineapple", "rhubarb"]
words = ["epalp", "nanaba", "untcooc", "adnuir", "truif", "uperragift", "reorshidsha", "maj", "ikwi", "agmno", "anoreg", "pnpeepali", "aurhrbb"]

num = random.randrange(0, len(answers), 1)
score = 0
q_count = 0

def default():
    global words, num
    jumble_lbl.config(text=words[num])

def reset():
    global words, num
    num = random.randrange(0, len(words), 1)
    jumble_lbl.config(text=words[num])
    input_box.delete(0, END)

root = Tk()
root.geometry("500x500+500+150")
root.config(background="#40DFFF")

heading_lbl = Label(root, text="WORD JUMBLE GAME", bg="#40dfff", fg = "#000000", font=("Verdana", 30, "bold"))
heading_lbl.pack(pady=5)

jumble_lbl = Label(root, bg="#40dfff", fg="#594F4F", font=("Verdana", 25))
jumble_lbl.pack(pady=30, ipadx=10, ipady=10)

ans = StringVar()
input_box = Entry(root, font=("Verdana", 25), textvariable=ans, justify="center")
input_box.pack(ipadx=5, ipady=5)

check_btn = Button(root, text="CHECK", bg="#00ff00", fg="#070D15", font=("Verdana", 22, "bold"))
check_btn.pack(pady=40)

reset_btn = Button(root, text="RESET", bg="#ffd500", fg="#070d15", font=("Verdana", 22, "bold"), command=reset)
reset_btn.pack()


default()
root.mainloop()