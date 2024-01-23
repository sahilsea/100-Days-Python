from tkinter import *

window = Tk("my First GUI")
window.title("My First GUI")
window.minsize(width= 500, height= 500)

# Label
my_label = Label(text= "New Text", font= ("Arial", 24, "italic"))
my_label.grid(column=0, row=0)


# Button
def button_clicked():
    my_label.config(text=input.get())
button = Button(text = "Click me", command = button_clicked)
button.grid(column=1, row=1)
# New Button
button2 = Button(text = "Click me", command = button_clicked)
button2.grid(column=2, row=0)


# Entry
text = Text(height= 2, width= 5)
# Puts cursor in text box
text.focus()  

# Add begininning text
text.insert(END, "Example of multiline text entry.")
# Gets current value in textbox at line 1, character 0.
print(text.get("1.0", END))
text.grid(column=3, row=2)


window.mainloop()