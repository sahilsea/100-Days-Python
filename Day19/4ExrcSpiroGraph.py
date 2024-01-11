import turtle
import random


tim = turtle.Turtle()
tim.speed('fastest')
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r,g,b)


n = 0
for i in range(0, 2000):

    tim.circle(50,2)
    tim.color(random_color())
    # tim.tiltangle(n)
    # n += 10
    tim.circle(100)
















screen = turtle.Screen()
screen.exitonclick()