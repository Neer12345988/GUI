from tkinter import *
import calendar

def show_calendar():
    new_root = Tk()
    new_root.geometry("550x550")
    new_root.title("CALENDAR WINDOW")
    new_root.config(background="#f2fbef")

    year = int(year_box.get())
    cal_contents = calendar.calendar(year)
    calendar_lbl = Label(new_root, text=cal_contents, font=("Consolas", 10, "bold"))
    calendar_lbl.pack()
    new_root.mainloop()

# Main window
if __name__ == "__main__":
    root = Tk()
    root.geometry("350x400")
    root.title("Calendar")
    root.config(background="#f1faee")

    heading_lbl = Label(root, text="Calendar", bg= "#f1faee", fg= "#212529", font=("Arial", 25, "bold"))
    heading_lbl.pack(padx=10, pady=10)

    year_lbl = Label(root, text="Enter year: ", bg="#f2faee", fg="#222529", font=("Arial", 18, "bold"))
    year_lbl.pack(padx=10, pady=10)

    year_box = Entry(root, font= ("Arial", 18, "bold"), justify="center")
    year_box.pack(padx=10, pady=10)

    show_btn = Button(root, text="Show", bg="#43aa8b", fg="#f8961e", font=("Arial", 18, "bold"), command=show_calendar)
    show_btn.pack(padx= 10, pady= 10)

    exit_btn = Button(root, text="Exit", bg="#ff0000", fg="#000000", font=("Arial", 18, "bold"), command=exit)
    exit_btn.pack(padx=10, pady=10)


    root.mainloop()