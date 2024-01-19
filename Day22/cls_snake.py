from turtle import Turtle, Screen
MOVE_DISTANCE = 20
CORDINATES = [(0,0), (20,0), (40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
screen = Screen()

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.upp()

    def create_snake(self):
        for position in CORDINATES:
            self.add_segment(position)
            

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for trtle_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[trtle_num - 1].xcor()
            new_y = self.segments[trtle_num - 1].ycor()
            self.segments[trtle_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def upp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def rightt(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def leftt(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def downn(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

