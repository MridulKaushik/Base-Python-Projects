from turtle import Turtle

FONT = ("Courier", 22, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-270, 260)
        self.level = 1
        self.Write()

    def Write(self):
        self.write(f"Level:{self.level}", align='center', font=FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.Write()

    def game_over(self):
        self.color('black')
        self.goto(0, 0)
        self.write("Game Over", align='center', font=("Arial", 28, "bold"))
