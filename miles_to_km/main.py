from tkinter import *

window =Tk()
window.title("Miles to KM")
window.minsize(width=500,height=300)

My_input = Entry(width=10)
My_input.grid(row=1,column=2)
miles_lable = Label(text="Miles")
miles_lable.grid(column=3,row=1)
is_equal = Label(text="is equal to")
is_equal.grid(row=2,column=1)
number_lable = Label(text="",padx=10)
number_lable.grid(row=2,column=2)
km_lable = Label(text="Km")
km_lable.grid(row=2,column=3)

def convert():
    miles = My_input.get()
    kms = float(miles)*1.609344
    number_lable.config(text=str(kms))

caluculate_button = Button(text="Caluculate",command=convert)
caluculate_button.grid(row=3,column=2)
window.mainloop()