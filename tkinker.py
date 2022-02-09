# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import date
from dateutil.relativedelta import relativedelta as rdelta

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# Add Calendar
cal = Calendar(root, selectmode='day',
               year=1980, month=8,
               day=18
               )

cal.pack(pady=20)


def grad_date():

    today_date = date.today()
    person_birthsday = cal.selection_get()
    rd = rdelta(today_date, person_birthsday)
    print(type(rd), type(today_date), type(person_birthsday))
    date_label.config(text=f"Selected Date is: {person_birthsday} \n"
                           f"today is: {today_date} \n"
                           f"you age is : {rd.years} years {rd.months} months {rd.days} days")

# Add Button and Label
Button(root, text="Calculate age",
       command=grad_date).pack(pady=20)

date_label = Label(root, text="")
date_label.pack(pady=20)
# Excecute Tkinter
root.mainloop()