from turtle import Turtle

FONT = ('Times New Roman', 14, 'bold')


class scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r+") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 230)
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Your Score = {self.score}  High Score = {self.high_score}", align='center', font=FONT)

    def increase(self):
        self.score += 1
        self.update()

    def Reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.color('white')
    #     self.goto(0, 0)
    #     self.write("Game Over", align='center', font=("Arial", 28, "bold"))
