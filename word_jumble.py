from tkinter import *
import random
import tkinter.messagebox

answers = ["apple", "banana", "coconut", "durian", "fruit", "grapefruit", "horseradish", "jam", "kiwi", "mango", "orange", "pineapple", "rhubarb"]
words = ["epalp", "nanaba", "untcooc", "adnuir", "truif", "uperragift", "reorshidsha", "maj", "ikwi", "agmno", "anoreg", "pnpeepali", "aurhrbb"]

root = Tk()
root.geometry("500x500+500+150")
root.config(background="#40DFFF")

num = random.randrange(0, len(answers), 1)
score = 0
q_count = 0
score_lbl = Label(root)
score_txt = ""

def default():
    global words, num
    jumble_lbl.config(text=words[num])

def reset():
    global words, num
    num = random.randrange(0, len(words), 1)
    jumble_lbl.config(text=words[num])
    input_box.delete(0, END)

def check():
    global answers, words, num, score, q_count, score_lbl, score_txt
    q_count += 1
    ans = input_box.get()
    if ans == answers[num]:
        tkinter.messagebox.showinfo("Correct", "Congratulations!")
        score += 1
    else:
        tkinter.messagebox.showerror("Incorrect", "Unlucky")
    score_txt = f"Score: {score}/{q_count}"
    score_lbl.forget()
    score_lbl = Label(root, text=score_txt, bg="#40dfff", fg="#007e00", font=("Verdana", 18, "normal"))
    score_lbl.pack(side=LEFT)
    reset()

heading_lbl = Label(root, text="WORD JUMBLE GAME", bg="#40dfff", fg = "#000000", font=("Verdana", 30, "bold"))
heading_lbl.pack(pady=5)

jumble_lbl = Label(root, bg="#40dfff", fg="#594F4F", font=("Verdana", 25))
jumble_lbl.pack(pady=30, ipadx=10, ipady=10)

ans = StringVar()
input_box = Entry(root, font=("Verdana", 25), textvariable=ans, justify="center")
input_box.pack(ipadx=5, ipady=5)

check_btn = Button(root, text="CHECK", bg="#00ff00", fg="#070D15", font=("Verdana", 22, "bold"), command=check)
check_btn.pack(pady=40)

reset_btn = Button(root, text="RESET", bg="#ffd500", fg="#070d15", font=("Verdana", 22, "bold"), command=reset)
reset_btn.pack()


default()
root.mainloop()