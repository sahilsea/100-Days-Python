from tkinter import *

# Window
window = Tk()
window.minsize(height=150, width=200)
window.title("Mile to Km Converter")
window.config(padx=50, pady=30)


# Entry (User Input)
usr_input = Entry(width= 6)
usr_input.insert(END, "0")
usr_input.focus()
usr_input.grid(column=1, row=0)

# Label (Unit)
unit_label = Label(text="Miles", font=("Arial", 20, "bold"))
unit_label.grid(column=2, row=0 )

# Label2 (Equivalent)
eq_label = Label(text="is equal to" )
eq_label.grid(column=0, row=1)

# Label3 (Unit Text Km)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Label4 (Result)
result_label = Label(text="0")
result_label.grid(column=1, row=1)

# Button (Calculate)
def button_clicked():
    result_label.config(text = (float(usr_input.get()) * 1.6))
button = Button(text="Calculate", command= button_clicked)
button.grid(column=1, row=2)



























window.mainloop()