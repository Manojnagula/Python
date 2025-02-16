from tkinter import *
import random
import string
from tkinter import messagebox
import json

PASSWORD_FILE = r"c:\Users\Manoj\Downloads\passwords.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    li=[]
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special_chars=string.punctuation
    li.append(random.choice(upper))
    li.append(random.choice(lower))
    li.append(random.choice(special_chars))
    length = random.choice([5,10])
    for _ in range(length):
        source = random.choice([upper,lower,special_chars])
        li.append(source[random.randrange(0,len(source))])
    random.shuffle(li)
    password = "".join(li)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def delete_all_entries():
    website_entry.delete(0,END)
    password_entry.delete(0,END)
def password_saving():
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        new_data = {
             website:{
                  "email":email,
                  "password":password
             }
        }
        if len(website) == 0 or len(password)==0:
            messagebox.showinfo(title="Oops", message="Please make sure to enter the credentials")
        else:
            try:
                with open(PASSWORD_FILE,'r') as passwords_file:
                    data=json.load(passwords_file)
            except FileNotFoundError:
                with open(PASSWORD_FILE,'w') as passwords_file:
                    json.dump(new_data,passwords_file,indent=4)
            else:    
                data.update(new_data)
                with open(PASSWORD_FILE,'w') as passwords_file:
                    json.dump(data,passwords_file,indent=4)
            finally:    
                delete_all_entries()

# ---------------------------- search credentials ------------------------------- #
def search_creds():
    website = website_entry.get()
    try:
        with open(PASSWORD_FILE,'r') as password_file:
            data = json.load(password_file)
            password = data[website]['password']
            email = data[website]['email']
    except KeyError:
            messagebox.showinfo(title="Error", message=r"No such website")
            
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message=r"No password data file found")
            
    else:
            messagebox.showinfo(title="Credentials", message=f"website : {website}\n email : {email}\n password : {password}")
    finally:
         delete_all_entries()
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file=r"password-manager-start\logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#lables
website_label = Label(text="Website")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2,column=0)
password_lable = Label(text="password")
password_lable.grid(row=3,column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"example@gmail.com")
password_entry=Entry()
password_entry.grid(row=3,column=1,columnspan=1)

# Buttons
generate_password_button = Button(text="Generate Password",width=15,command=generate_password)
generate_password_button.grid(row=3,column=2,columnspan=1)
search_button = Button(text="Search",width=15,command=search_creds)
search_button.grid(row=1,column=2,columnspan=1)
add_button = Button(text="Add",width=30,command=password_saving)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()