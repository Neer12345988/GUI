from tkinter import *

root = Tk()
root.config(background="#48cae4")
root.geometry("610x400")

def convert():
    grams = float(weight_box.get()) * 1000
    pounds = float(weight_box.get()) * 2.20462
    ounces = float(weight_box.get()) * 35.274

    grams_box.delete("1.0", END)
    grams_box.insert(END, grams)

    pounds_box.delete("1.0", END)
    pounds_box.insert(END, pounds)

    ounces_box.delete("1.0", END)
    ounces_box.insert(END, ounces)


heading_lbl = Label(root, text="Weight converter", bg="#48cae4", fg="#03045e", font=("Calibri", 22, "bold"))
heading_lbl.grid(row=0, column=1, padx=10, pady=10)

weight_lbl = Label(root, text="Enter weight in kg: ", bg="#48cae5", fg="#02044d", font=("Calibri", 15))
weight_lbl.grid(row=1, column=0)

weight_box = Entry(root)
weight_box.grid(row=1, column=1)

convert_btn = Button(root, text="CONVERT", bg="#d00000", fg="#000000", font=("Calibri", 12, "bold"), command = convert)
convert_btn.grid(row=1, column=2, padx=10, pady=10)


grams_lbl = Label(root, text="Grams", bg="#48cae6", fg="#008000", font=("Calibri", 15))
grams_lbl.grid(row=3, column=0, padx=10, pady=10)
grams_box = Text(root, width=20, height=2)
grams_box.grid(row=4, column=0, padx=10, pady=10)

pounds_lbl = Label(root, text="Pounds", bg="#48cae7", fg="#ff8204", font=("Calibri", 15))
pounds_lbl.grid(row=3, column=1, padx=10, pady=10)
pounds_box = Text(root, width=20, height=2)
pounds_box.grid(row= 4, column=1, padx=10, pady=10)

ounces_lbl = Label(root, text="Ounces", bg="#48cae9", fg="#e10000", font=("Calibri", 15))
ounces_lbl.grid(row=3, column=2, padx=10, pady=10)
ounces_box = Text(root, width=20, height=2)
ounces_box.grid(row=4, column=2, padx=10, pady=10)

root.mainloop()