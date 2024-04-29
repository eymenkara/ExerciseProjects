from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

SPEED = 0.1

s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

score = ScoreBoard()
food = Food()
game_on = True
while game_on:
    s.update()
    time.sleep(SPEED)
    snake.move_snake()

    # Detect Collision With Food
    if snake.head.distance(food) < 15:
        score.scored()
        snake.extend()
        food.refresh()

    # Detect Collision With Wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.reset_score()
        snake.reset()


    # Detect Collision With Tail
    for i in range(1, len(snake.blocks)):
        if snake.head.distance(snake.blocks[i]) < 15:
            score.reset_score()
            snake.reset()


s.exitonclick()
