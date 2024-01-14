from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        
        super().__init__()
        self.score = 0
        self.color("white")
        
        self.penup()
        self.sety(260)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(arg= (f"Score: {self.score}") , move=False, align="center", font= ("Arial",24,"normal"))
        
    def game_over(self):
        self.goto(0,0)
        self.write(arg= "GAME OVER", move=False, align="center", font= ("Arial",24,"normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

