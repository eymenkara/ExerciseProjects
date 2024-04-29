from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(0.0016)
    if ball.xcor() > 380 : # l_paddle wins
        ball.reset_pos()
        scoreboard.l_point()
    elif ball.xcor() < -380: # r_paddle wins
        ball.reset_pos()
        scoreboard.r_point()


    else:
        # paddle (20*100) && ball (20*20) fix
        if ball.xcor() == l_paddle.xcor() + 20:
            if ball.ycor() > l_paddle.ycor() + 70 or ball.ycor() < l_paddle.ycor() - 70:
                ball.move()
                screen.update()
            else:
                ball.bounce()
                ball.move()
                screen.update()

        if ball.xcor() == r_paddle.xcor() - 20:
            if ball.ycor() > r_paddle.ycor() + 60 or ball.ycor() < r_paddle.ycor() - 60:
                ball.move()
                screen.update()
            else:
                ball.bounce()
                ball.move()
                screen.update()
        else:
            ball.move()
            screen.update()






screen.exitonclick()




