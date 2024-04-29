from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_speed = 1
        self.y_speed = 1

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_speed = self.y_speed * -1
            self.goto(self.xcor() + self.x_speed, self.ycor() + self.y_speed)
        else:
            self.goto(self.xcor() + self.x_speed, self.ycor() + self.y_speed)

    def bounce(self):
        self.x_speed = self.x_speed * -1

    def reset_pos(self):
        self.goto(0,0)
        self.x_speed *= -1

