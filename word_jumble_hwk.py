from tkinter import *
import random
import tkinter.messagebox

root = Tk()
root.geometry("500x500+500+150")
root.config(background="#FFA908")

answers = ["beak", "cause", "deaf", "earth", "elbow", "finger", "grab", "melon", "priest", "silent", "teacher", "thing", "wolf"]
words = ["bake", "sauce", "fade", "heart", "below", "fringe", "brag", "lemon", "stripe", "listen", "cheater", "night", "flow"]

num = random.randrange(0, len(answers), 1)
score = 0
lives = 3

def default():
    global words, num
    anagram.config(text=words[num])

def check():
    global answers, words, num, score, scorelbl, lives, liveslbl
    ans = guess_box.get()
    if ans == answers[num]:
        tkinter.messagebox.showinfo("Score +1", "Correct")
        score += 1
    elif ans != answers[num] and lives > 0:
        tkinter.messagebox.showerror("Lives -1", "Cat sat on the keyboard?")
        lives -= 1
    else:
        tkinter.messagebox.showerror("Wrong", "You're out of lives. GAME OVER")
    scorelbl.forget()
    scorelbl = Label(root, text=f"Words: {score}", bg="#FFA908", fg="#023316", font=("Times New Roman", 18))
    scorelbl.pack()
    liveslbl = Label(root, text=f"Lives: {lives}", bg= "#FFA908", fg="black", font=("Times New Roman", 18))
    liveslbl.pack()


heading = Label(root, text="Anagrams!", bg="#ffa908", fg="#00003B", font=("Comic Sans MS", 30, "bold"))
heading.pack()

scorelbl = Label(root, text=f"Words: {score}", bg="#FFA908", fg="#023316", font=("Times New Roman", 18))
scorelbl.pack()

liveslbl = Label(root, text=f"Lives: {lives}", bg= "#FFA908", fg="black", font=("Times New Roman", 18))
liveslbl.pack()

anagram = Label(root, bg="#ffa908", fg="#FFFFFF", font=("Verdana", 25))
anagram.pack()

guess = StringVar()
guess_box = Entry(root, font=("Verdana", 25), textvariable=guess, justify="center")
guess_box.pack()

checkbtn = Button(root, text="CHECK", bg="#ff0000", fg="#000000", font=("Times New Roman", 20, "bold"), command=check)
checkbtn.pack(pady=20)

#while lives > 0:
default()

root.mainloop()