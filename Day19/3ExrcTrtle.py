import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.pensize(10)
direction = [0, 90, 270, 180, ]
tim.speed('fastest')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r,g,b)


for i in range(0, 50000000):
    tim.forward(30)
    tim.color(random_color())
    tim.left(random.choice(direction))























screen = turtle.Screen()
screen.exitonclick()