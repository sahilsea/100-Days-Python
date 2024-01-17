from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_y_position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(5,1)
        self.penup()
        self.goto(x_y_position)
        self.go_up()
        self.go_down()
    
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    
































