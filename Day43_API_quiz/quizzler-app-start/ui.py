from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background= THEME_COLOR)

        self.score = Label(text= f"Score {0}", font= ('Arial', 17, 'bold'), highlightthickness= 0)
        self.score.grid(row= 0, column= 1)

        self.txt_canvas = Canvas(width= 300, height= 250, background= 'white')
        self.question_txt = self.txt_canvas.create_text(150,120 ,text= "hello",  fill = THEME_COLOR, font= ('Arial', 20, 'italic'))
        self.txt_canvas.grid(row=1, column=0, columnspan= 2, pady = 40)

        right_img = PhotoImage(file="./images/true.png")
        self.right_button = Button(image= right_img)
        self.right_button.grid(row=2, column= 0)

        wrong_img = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image= wrong_img)
        self.wrong_button.grid(row=2, column= 1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.txt_canvas.itemconfig(self.question_txt, text= q_text)

