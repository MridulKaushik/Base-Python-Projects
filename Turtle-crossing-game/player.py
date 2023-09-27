from turtle import Turtle
from car_manager import COLORS
import random

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 275


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.seth(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.color("black", "black")

    def move(self):
        self.goto(0, self.ycor()+MOVE_DISTANCE)

    def Reset(self):
        self.goto(STARTING_POSITION)
        colory = random.choice(COLORS)
        self.color(colory, colory)
            