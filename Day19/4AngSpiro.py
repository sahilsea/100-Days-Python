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

def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.color(random_color())
        tim.circle(50)
        tim.setheading(tim.heading()+gap_size)
    
draw_spirograph(2)

















screen = turtle.Screen()
screen.exitonclick()