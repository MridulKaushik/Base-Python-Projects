from turtle import Turtle
import random as rand


class Turtle_race:

    def __init__(self, numer_of_turtles):
        self.turtle_num = numer_of_turtles
        self.a = []

    def createTurtle(self):
        colors = ["Red", "Blue", "Green", "SkyBlue", "Purple", "Black", "NavyBlue", "Brown"]
        y_axis = -150

        for i in range(self.turtle_num + 1):
            y_axis += 40
            b = Turtle("turtle")
            self.a.append(b)
            self.a[i].penup()
            self.a[i].color(colors[i])
            self.a[i].goto(x=-280, y=y_axis)

    def random_move(self, race_status, user_bet):

        while race_status:
            for turtle in self.a:
                if turtle.xcor() > 280:
                    race_status = False
                    print(turtle.pencolor())
                    if turtle.pencolor().lower() == user_bet:
                        print("You Won the bet", end='\n')
                    else:
                        print("You Lose")
                move = rand.randint(1, 15)
                turtle.forward(move)
