from turtle import Turtle, Screen
import random

tim = Turtle()
shp_color = ['red', 'green', 'blue', 'DarkOrchid', 'wheat', 'seaGreen', 'SlateGray', 'CornflowerBlue']

cmp_angle = 360
n = 3
for i in range(0, 9):
    for i in range(0, n):
        tim.forward(100)
        tim.left(cmp_angle/n)
    n += 1
    tim.color(random.choice(shp_color))


