from turtle import Screen
from cls_snake import Snake
from cls_food import Food
from cls_scoreboard import Scoreboard
import time

#Window control
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

#Classes
snake = Snake()
food = Food()
scoree = Scoreboard()

#Movements
screen.listen()
screen.onkey(snake.upp , 'Up')
screen.onkey(snake.downn , 'Down')
screen.onkey(snake.leftt , 'Left')
screen.onkey(snake.rightt, 'Right')

#Starting The Game
game_is_on = True
while game_is_on:
    #Snake
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect Collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoree.increase_score()

    #Detect Collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        scoree.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # game_is_on = False
            scoree.reset()
            snake.reset()

        










screen.exitonclick()
