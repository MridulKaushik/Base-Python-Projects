from Snake import snake
from turtle import Screen
from food import Food
from Score import scoreboard
import time

screen = Screen()

screen.setup(width=520, height=520)
screen.bgcolor("black")
screen.title("  NAAGIN KA BADLA ")
screen.tracer(0)

new_snake = snake()
food = Food()
scoreboard = scoreboard()

screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()

    # Detect Collision with food
    if new_snake.head.distance(food) < 14:
        food.refresh()
        scoreboard.increase()
        new_snake.extend()

    # Detect collision with walls
    if new_snake.head.xcor() > 255 or new_snake.head.xcor() < (-250) or new_snake.head.ycor() > 259 or new_snake.head.ycor() < (-250):
        scoreboard.Reset()
        new_snake.new_snake()
        # scoreboard.game_over()
        # game_is_on = False
    
    # Detect collision with Tail 
    # If head collides with any segment of the snake body
    for segment in new_snake.segments[1:]:
        if new_snake.head.distance(segment) < 10:
            scoreboard.Reset()
            new_snake.new_snake()
            # game_is_on = False
            # scoreboard.game_over()


screen.exitonclick()
