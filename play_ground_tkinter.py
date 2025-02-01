from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

my_lable = Label(text="Iam a lable", font=("Arial",24,"bold"))
my_lable.grid(side='left')
def listen():
    my_lable.config(text=my_input.get())
myButton = Button(text="button",font=("Arial",24,"bold"),command=listen)
myButton.pack(side="top")
my_input = Entry()
my_input.pack()
window.mainloop()
