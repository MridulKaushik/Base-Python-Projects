from turtle import Screen
from Paddle import Paddle
from ball import Ball
from Score import Score
import time

game_is_on = True
rpaddle = Paddle(376, 60)
lpaddle = Paddle(-383, -60)
gend = Ball()
line = []
screen = Screen()
left_score = Score(-200, 280)
right_score = Score(200, 280)

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

screen.listen()
screen.onkeypress(rpaddle.go_up, "Up")
screen.onkeypress(rpaddle.go_down, "Down")
screen.onkeypress(lpaddle.go_up, "w")
screen.onkeypress(lpaddle.go_down, "s")
# screen.onkey(begin, "Enter")


while game_is_on:
    time.sleep(gend.move_speed)
    screen.update()
    gend.move()

    # Detect the collision with upper and bottom walls
    if gend.ycor() > 280 or gend.ycor() < -280:
        # MAke the ball bounce
        gend.bounce_y()

    # Detect the collision with the paddle
    if (gend.distance(rpaddle.paddle) < 55 and gend.xcor() > 350) or (
            gend.distance(lpaddle.paddle) < 55 and gend.xcor() < -350):
        gend.bounce_x()

    # Detect when Right paddle misses
    if gend.xcor() > 380:
        left_score.increase()
        gend.reset_ball()

    # Detect when left paddle misses
    if gend.xcor() < -380:
        right_score.increase()
        gend.reset_ball()

    if left_score.score == 5:
        left_score.game_over("Left Player")
        game_is_on = False

    if right_score.score == 5:
        right_score.game_over("Right Player")
        game_is_on = False


screen.exitonclick()
