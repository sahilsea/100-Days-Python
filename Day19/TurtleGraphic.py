from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
n = 0
for i in range(0, 20):
    n += 1
    if n % 2 == 0:

        timmy_the_turtle.color('white')
        timmy_the_turtle.forward(10)
    else:
        timmy_the_turtle.color('red')
        timmy_the_turtle.forward(10)
























screen = Screen()
screen.exitonclick()