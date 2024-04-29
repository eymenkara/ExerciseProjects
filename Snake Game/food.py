from turtle import Turtle
import random

X_CORDS = []
Y_CORDS = []

for i in range(-280, 281, 20):
    X_CORDS.append(i)
    Y_CORDS.append(i)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.choice(X_CORDS), random.choice(Y_CORDS))




