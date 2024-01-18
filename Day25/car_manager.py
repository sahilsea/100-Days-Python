from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager():
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        # self.create_cars()
        # self.add_cars()

        
    # def create_cars(self):
    #     for i in range(randint(20, 40)):
    #         self.add_cars()

    def add_cars(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(1, 2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(x=300, y=(randint(-250, 250)))
            self.car_list.append(new_car)

    def move_car(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        


        
