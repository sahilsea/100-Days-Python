from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)

input_email = Entry(width=35,)
input_email.grid(column=1, row=2, columnspan=2)

input_password = Entry(width=21,)
input_password.grid(column=1, row=3,)

# Button (Generate Password, Add)
generate_pswrd = Button(text="Generate Password")
generate_pswrd.grid(column=2, row=3,)

add_pswrd = Button(text="Add", width= 36)
add_pswrd.grid(column=1, row=4, columnspan=2)





window.mainloop()