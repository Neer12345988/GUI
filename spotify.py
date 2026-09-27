from tkinter import *

root = Tk()
root.config(background="#002700")
root.geometry("750x500")

playing_song = ""

def play():
    global playing_song, playing_lbl, playlist
    index = playlist.get(playlist.curselection())
    if index:
        playing_song = index
        playing_lbl.forget()
        playing_lbl = Label(root, text=f"Now playing: {playing_song}", bg="#002700", fg="#ffeeff", font=("Verdana", 15, "bold"))
        playing_lbl.pack()

headinglbl = Label(root, text="Your playlist", bg="#002700", fg="#ffeeff", font=("Verdana", 30, "bold"))
headinglbl.pack()

frame = Frame(root, bg="#002700")
frame.pack()

play_btn = Button(frame, text="PLAY", bg="#031634", fg="#ffffee", font=("Verdana", 25, "bold"), command=play)
play_btn.pack(side=RIGHT, padx=50)

playlist = Listbox(frame, width=100)
for song in ["I Wanna Be Yours", "Let Down", "Mr. Brightside", "Don't Look Back In Anger", "Heaven Knows I'm Miserable Now"]:
    playlist.insert(END, song)
playlist.pack(pady=50)


playing_lbl = Label(root, text=f"Now playing: {playing_song}", bg="#002700", fg="#ffeeff", font=("Verdana", 15, "bold"))
playing_lbl.pack()



root.mainloop()