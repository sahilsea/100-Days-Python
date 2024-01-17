from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 260)
        self.write(arg= self.r_score, move= False, align= "center",font= ("Arial",30, "normal"))
        self.goto(-100, 260)
        self.write(arg= self.l_score, move= False, align= "center",font= ("Arial",30, "normal"))


    def increase_r_score(self):
        self.r_score += 1
        self.update_score()

    def increase_l_score(self):
        self.l_score += 1
        self.update_score()

    