from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forward_mv():
    tim.forward(10)
def back_mv():
    tim.backward(10)
def left_mv():
    tim.left(10)
def right_mv():
    tim.right(10)
def clear_art():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key = "w", fun= forward_mv)
screen.onkey(key = "s", fun= back_mv)
screen.onkey(key = "a", fun= left_mv)
screen.onkey(key = "d", fun= right_mv)
screen.onkey(key = "c", fun= clear_art)


screen.exitonclick()