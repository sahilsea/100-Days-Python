from tkinter import *

window = Tk("my First GUI")
window.title("My First GUI")
window.minsize(width= 500, height= 500)

# Label
my_label = Label(text= "New Text", font= ("Arial", 24, "italic"))
my_label.pack()


# Button
def button_clicked():
    my_label.config(text=input.get())
button = Button(text = "Click me", command = button_clicked)
button.pack()


# Entry
text = Text(height= 5, width= 30)
# Puts curson in text box
text.focus()
# Add begininning text
text.insert(END, "Example of multiline text entry.")
# Gets current value in textbox at line 1, character 0.
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # Gets the current value in the spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0 , to= 10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current value.
def scale_used(value):
    print(value)
scale = Scale(from_=0 , to = 100, command= scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    # Print 1 if On button checked, otherwise 0.
    print(checked_state.get())
# Variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text= "Is On?", variable=checked_state, command= checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value= 1, variable= radio_state, command= radio_used)
radiobutton2 = Radiobutton(text="Option 2",value=2, variable= radio_state , command= radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()





window.mainloop()