from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_sleep = 0.1

    def move(self):
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(x=new_x, y=new_y)

    def ball_reset(self):
        self.goto(0,0)
        self.ball_sleep = 0.1

    def bounce_y(self):
         self.y_move *= -1
        
    def bounce_x(self):
         self.x_move *= -1


