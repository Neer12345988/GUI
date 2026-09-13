from tkinter import *
from tkinter.ttk import Combobox

root = Tk()

heading = Label(root, text="Colour change", font=("Arial", 15, "bold"))
heading.pack()

endVal = StringVar()
red_btn = Radiobutton(root, text="Red", variable=endVal, value="red")
red_btn.pack()
green_btn = Radiobutton(root, text="Green", variable=endVal, value="green")
green_btn.pack()
blue_btn = Radiobutton(root, text="Blue", variable=endVal, value="blue")
blue_btn.pack()
endVal.set("red")

root.mainloop()