from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background= THEME_COLOR)

        # Score
        self.score_lbl = Label(text= f"score: {0}", font= ('Arial', 17, 'bold'), highlightthickness= 0)
        self.score_lbl.grid(row= 0, column= 1)

        # Text Canvas
        self.txt_canvas = Canvas(width= 300, height= 250, background= 'white')
        self.question_txt = self.txt_canvas.create_text(150,120 ,text= "hello", width=280, fill = THEME_COLOR, font= ('Arial', 20, 'italic'))
        self.txt_canvas.grid(row=1, column=0, columnspan= 2, pady = 40)
        
        # True Button
        right_img = PhotoImage(file="./images/true.png")
        self.right_button = Button(image= right_img, command= self.pressed_true,)
        self.right_button.grid(row=2, column= 0)
        
        # False Button
        wrong_img = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image= wrong_img, command= self.pressed_False,)
        self.wrong_button.grid(row=2, column= 1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.txt_canvas.config(bg= "white")
        if self.quiz.still_has_questions():
            self.score_lbl.config(text= f"Score :{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.txt_canvas.itemconfig(self.question_txt, text= q_text)
        else:
            self.txt_canvas.itemconfig(self.question_txt, text= f"The End \n Your Total Score is {self.quiz.score}")
            self.right_button.config(state = "disabled")
            self.wrong_button.config(state = "disabled")

    def pressed_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def pressed_False(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self, is_right):
        if is_right:
            self.txt_canvas.config(bg="green")
        else:
            self.txt_canvas.config(bg= 'red')
        
        self.window.after(300, self.get_next_question,)


