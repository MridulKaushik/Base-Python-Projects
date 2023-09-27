import turtle
from turtle import Turtle
import random as rand

turtle.colormode(255)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.random_x = 110
        self.random_y = 110
        self.random_value()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(self.random_x, self.random_y)
        self.color(self.random_color())
        
        self.speed("fastest")

    def random_value(self):
        self.random_x = rand.randint(-230, 230)
        self.random_y = rand.randint(-230, 230)

    def refresh(self):
        self.random_value() 
        self.color(self.random_color())
        self.goto(self.random_x, self.random_y)

    @staticmethod
    def random_color():
        r = rand.randint(2, 255)
        g = rand.randint(4, 255)
        b = rand.randint(8, 255)
        rand_color = (r, g, b)
        return rand_color
