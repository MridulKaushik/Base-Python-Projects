from turtle import Turtle
from food import Food

STARTING_POSITION = [(0, 0), (-20, 0), (20, 0)]
MOVE_DISTANCE = 20
SPEED = 1


class snake:

    def __init__(self):
        self.segments = []
        self.speedy = SPEED
        self.Create_snakes()
        self.head = self.segments[0]

    def Create_snakes(self):

        for segment in STARTING_POSITION:
            self.add_segment(segment)
            """A 'for' loop that creates and initializes there coordinates"""

    def add_segment(self, segment):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(segment)
        self.segments.append(new_segment)
        new_segment.speed(self.speedy)
        self.speedy += 0.05

    def move(self):
       
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def new_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.Create_snakes()
        self.head = self.segments[0]

    def extend(self):
        snake_color = Food.random_color()
        for segment in self.segments[0:]:
           segment.color(snake_color)
        self.add_segment(self.segments[-1].position())
