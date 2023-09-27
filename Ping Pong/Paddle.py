from turtle import Turtle


class Paddle:

    def __init__(self, x, y):
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.speed('fastest')
        self.paddle.shape('square')
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(x, y)
        self.make_line()

    @staticmethod
    def make_line():
        line = []
        new_y = 280
        for i in range(8):
            b = Turtle("square")
            line.append(b)
            line[i].penup()
            line[i].shapesize(stretch_wid=2, stretch_len=0.2)
            line[i].color("white")
            line[i].goto(0, new_y)
            new_y -= 80

    def go_up(self):
        new_y = self.paddle.ycor() + 15
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 15
        self.paddle.goto(self.paddle.xcor(), new_y)
