from turtle import Turtle

FONT = ('Arial', 10, 'normal')


class Score(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align='Left', font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self, winner):
        self.color('white')
        self.goto(0, 0)
        self.write("Game Over", align='center', font=("Arial", 24, "bold"))
        self.goto(0, -35)
        self.color("green")
        self.write(winner+" Wins", align='center', font=("Arial", 28, "bold"))
