from turtle import Turtle

FONT = ("Courier", 21, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.update_Level()

    def update_Level(self):
        self.color('black')
        self.clear()
        self.goto(-220, 250)
        self.write(arg= f"Level: {self.level}" , move= False, align= "center", font= FONT)

    def increase_level(self):
        self.level += 1
        self.update_Level()

    def game_over(self):
        self.color('black')
        self.goto(0,0)
        self.write(arg= "GAME OVER " , move= False, align= "center", font= ("Arial", 25, "normal"))


