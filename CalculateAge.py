from tkinter import *
from datetime import datetime
from tkinter import messagebox


root = Tk()
root.geometry('500x350')

def age():
    if my_entry.get():
        try:
            current_year = datetime.now().year
            int(my_entry.get())
            your_age = current_year - int(my_entry.get())
            if your_age < 0:
                messagebox.showerror("Error", "You entered the wrong date of birth.")
            else:
                messagebox.showinfo("Your age", f"Your age is: {your_age}")
        except Exception:
            messagebox.showerror("Error", "You entered the wrong date of birth.")
    else:
        messagebox.showerror("Error", "You forgot to entry toru age!")


my_label = Label(root, text="Enter year born", font=("Helvetica", 24))
my_label.pack(pady=20)


my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

my_btn = Button(root, text="Calculate your age", font=("Helvetica", 18), command=age)
my_btn.pack(pady=20)

root.mainloop()