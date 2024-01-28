from tkinter import *
from tkinter import messagebox
import random
from pyperclip import copy
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]


    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char

    input_password.insert(0, password)
    copy(password)
# ---------------------------- JSON DATA ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
    input_website.get(): {
        "email": input_email.get(),
        "password": input_password.get()
        }
    }
    
    # if len(input_email.get()) != 0 and len(input_password.get()) != 0 and len(input_website.get()) != 0:
    #     is_ok = messagebox.askokcancel(title=input_website.get(), message=f"These are the details entered: \nEmail: {input_email.get()}"
    #                                f"\nPassword:{input_password.get() }\n Press ok to save")
    with open("data.json", mode= 'a') as data:
        json.dump(new_data, data, indent= 4)
        input_website.delete(0, 'end')
        input_email.delete(0, 'end')
        input_password.delete(0, 'end')
    # else:
    #     messagebox.askretrycancel(title= "Oops", message= "You can't leave any field empty!")

# ---------------------------- UI SETUP ------------------------------- #

# Window for the canvas
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas for the lock Picture
canvas = Canvas(width=200, height=200, highlightthickness=0,)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image = lock_img,)
canvas.grid(column=1, row=0)

# Label (Website, Email/Username, Password,)
web_lbl = Label(text="Website:",)
web_lbl.grid(column=0, row=1)
email_lbl = Label(text="Email/Username:")
email_lbl.grid(column=0, row=2)
password_lbl = Label(text="Password:")
password_lbl.grid(column=0, row=3)

# Entries (website, Email, password)
input_website = Entry(width=35,)
input_website.grid(column=1, row=1, columnspan=2)
# input_website.insert(0, "Ex - Google.com")
input_website.focus()
input_email = Entry(width=35,)
input_email.grid(column=1, row=2, columnspan=2)
# input_email.insert(0, "Ex - sahilsea10@gmail.com")
input_password = Entry(width=20,)
input_password.grid(column=1, row=3,)
# input_password.insert(0, "Ex- Mom&Dad#9$123")

# Button (Generate Password, Add)
generate_pswrd = Button(text="Generate Password",command= generatePassword)
generate_pswrd.grid(column=2, row=3,)
add_pswrd = Button(text="Add", width= 35, command= save)
add_pswrd.grid(column=1, row=4, columnspan=2)





window.mainloop()