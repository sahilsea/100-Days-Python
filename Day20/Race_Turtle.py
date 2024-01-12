from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cord = -90
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_cord)
    y_cord += 30
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win!, The {winning_color} turtle is first.")
            else:
                print(f"You lost!, the {winning_color} turtle is first.")








screen.exitonclick()