from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        
        super().__init__()
        self.score = 0
        with open("../Day26/data.txt") as data:
            high_score_data = (data.read())
            self.high_score = int(high_score_data)
        self.color("white")
    
        self.penup()
        self.sety(260)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(arg= (f"Score: {self.score} High Score: {self.high_score}") , move=False, align="center", font= ("Arial",24,"normal"))
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg= "GAME OVER", move=False, align="center", font= ("Arial",24,"normal"))
    def reset(self):
        if self.score > self.high_score:
            with open("../Day26/data.txt", mode= 'w') as data:
                data.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

