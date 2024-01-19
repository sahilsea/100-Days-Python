import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Cross")
screen.setup(width=600, height=600)
screen.tracer(0)

#Object Classes
player = Player()
car = CarManager()
level = Scoreboard()


#Movement
screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.add_cars()
    car.move_car()

    # Player collision with the Cars
    for car_i in car.car_list:
        if player.distance(car_i) < 20:
            game_is_on = False
            level.game_over()

    # Player level
    if player.ycor() > 280:
        level.increase_level()
        player.goto(0, -280)
        car.level_up()














screen.exitonclick()