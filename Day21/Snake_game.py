from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

aall_trtle = []

x_cord = 20
for i in range(0, 3):
    new_trtle = Turtle(shape="square")
    new_trtle.color('white')
    new_trtle.penup()
    new_trtle.setx(x_cord)
    x_cord -= 20
    aall_trtle.append(new_trtle)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    for trtle_num in range(len(aall_trtle) - 1, 0, -1):
        new_x = aall_trtle[trtle_num - 1].xcor()
        new_y = aall_trtle[trtle_num - 1].ycor()
        aall_trtle[trtle_num].goto(new_x, new_y)
    aall_trtle[0].forward(20)
    aall_trtle[0].left(90)



        












screen.exitonclick()