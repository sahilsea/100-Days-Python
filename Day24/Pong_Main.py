from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time

# Window Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("PONG")
screen.tracer(0)

# Pong Element classes
r_paddle = Paddle((376, 0))
l_paddle = Paddle((-385, 0))
ball = Ball()
score = Scoreboard()


# Paddle Movements
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

# Actual Game
game_over = False
while game_over == False:
    time.sleep(ball.ball_sleep)
    screen.update()
    ball.move()

    #Detect collision with upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()
        ball.ball_sleep *= 0.9

    #Detect collision with left and right wall
    if ball.xcor() > 380:
        ball.ball_reset()
        score.increase_l_score()
        ball.goto(0,0)
    elif ball.xcor() < -380:
        ball.ball_reset()
        score.increase_r_score()
        ball.goto(0,0)










screen.exitonclick()
