from turtle import Screen
# import random as rand
from turtleRace import Turtle_race

race = Turtle_race(6)
screen = Screen()
screen.setup(width=600, height=600)
race.createTurtle()
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race?\nEnter a color: ").lower()
print(user_bet)

is_race_on = False

if user_bet:
    is_race_on = True

race.random_move(race_status=is_race_on, user_bet=user_bet)

# tom = Turtle()
#
# def move_forward():
#     tom.forward(10)
#
#
# def move_backward():
#     tom.backward(10)
#
#
# def clockwise_turn():
#     change = tom.heading()+10
#     tom.setheading(change)
#
#
# def anticlockwise_turn():
#     shift = tom.heading()-10
#     tom.setheading(shift)
#
#
# def clear():
#     screen.clear()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="b", fun=move_backward)
# screen.onkey(key="d", fun=clockwise_turn)
# screen.onkey(key="a", fun=anticlockwise_turn)
# screen.onkey(key='c', fun=clear)
# screen.onkey(move_backward, "Down")
# screen.onkey(move_forward, "Up")
# screen.onkey(clockwise_turn, "Left")
# screen.onkey(anticlockwise_turn, "Right")
#
screen.exitonclick()
