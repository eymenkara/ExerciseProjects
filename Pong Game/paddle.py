from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, coordinate):
        super().__init__()
        self.create_paddle(coordinate)
        self.go_up()
        self.go_down()

    def create_paddle(self, coordinate):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coordinate)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


