from tkinter import Tk, Canvas, PhotoImage, Button
from pandas import read_csv, DataFrame
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# Producing random word from the csv file
try:
    data = read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient= "records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, filp_timer
    window.after_cancel(filp_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = 'black')
    canvas.itemconfig(card_word, text = current_card["French"], fill = 'black')
    canvas.itemconfig(card_background, image= front_img)
    filp_timer = window.after(3000, func= flip_card)


def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = 'white')
    canvas.itemconfig(card_word, text = current_card["English"], fill= 'white')
    canvas.itemconfig(card_background, image =back_img)

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index= False)

# Creating window
window = Tk()
window.config(padx=50, pady=50, background= BACKGROUND_COLOR)
window.title("Flashy")

filp_timer = window.after(3000, func= flip_card)
# Canvas for the flashcard 
canvas = Canvas(width=800, height=526, highlightthickness=0)
front_img = PhotoImage(file= "./images/card_front.png")
back_img = PhotoImage(file= "./images/card_back.png")
card_background = canvas.create_image(400, 263, image = front_img)
canvas.config(background= BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text = "", font= ("Ariel", 40, "italic"), fill= "black")
card_word = canvas.create_text(400, 263, text = "", font = ("Ariel", 60, "bold"), fill= 'black')
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_btn_img = PhotoImage(file = "./images/wrong.png")
wrong_btn = Button(image = wrong_btn_img, highlightthickness = 0, background= BACKGROUND_COLOR, command= next_card)
wrong_btn.grid(row= 1, column=0,)

right_btn_img = PhotoImage(file = "./images/right.png")
right_btn = Button(image = right_btn_img, highlightthickness = 0, background= BACKGROUND_COLOR ,command= is_known)
right_btn.grid(row= 1, column=1,)

next_card()


window.mainloop()
