from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('white', 'white')
        self.goto(0, 0)
        self.x_move = 5
        self.y_move = 5
        self.speed("fastest")
        self.move_speed = 0.04

    def move(self):
        self.penup()
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.04
        self.bounce_x()
