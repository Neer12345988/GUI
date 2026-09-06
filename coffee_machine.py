from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.geometry("1000x500")
root.config(background="#ccd5ae")

heading_lbl = Label(root, text="Welcome to your coffee machine!", bg="#ccd5ae", fg="#7A6A53", font=("Arial", 25, "bold"))
heading_lbl.place(x=75, y=10)

drink_lbl = Label(root, text="Drink: ", bg="#ccd5ae", fg="#7A6A53", font=("Constantia", 15, "bold"))
drink_lbl.place(x=25, y=90)
drinks = ["Latte", "Cappuccino", "Americano", "Mocha", "Matcha"]
drink_choices = Combobox(root, value=drinks, width=20, state="readonly")
drink_choices.place(x=225, y=90)

sugar_lbl = Label(root, text="Sugar amount: ", bg="#ccd5ae", fg="#7A6A53", font=("Constantia", 15, "bold"))
sugar_lbl.place(x=25, y=130)

endVal = StringVar()
low_sugar = Radiobutton(root, text="Low", bg="#ccd5ae", value="low", variable=endVal)
low_sugar.place(x=225, y=130)
medium_sugar = Radiobutton(root, text="Medium", bg="#ccd5ae", value="medium", variable=endVal)
medium_sugar.place(x=325, y=130)
high_sugar = Radiobutton(root, text="High", bg="#ccd5ae", value="high", variable=endVal)
high_sugar.place(x=425, y=130)
endVal.set("low")

milk_lbl = Label(root, text="Milk choice: ", bg="#ccd5ae", fg="#7A6A53", font=("Constantia", 15, "bold"))
milk_lbl.place(x=25, y=170)

endVal = StringVar()
whole_milk = Radiobutton(root, text="Whole milk", bg="#ccd5ae", value="w", variable=endVal)
oat_milk = Radiobutton(root, text="")


root.mainloop()