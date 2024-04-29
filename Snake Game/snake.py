from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.blocks = []
        self.create_snake()

        self.head = self.blocks[0]

    def create_snake(self):

        for i in range(3):
            n = -20 * i
            self.blocks.append(Turtle("square"))
            current_block = self.blocks[i]
            current_block.color("white")
            current_block.penup()
            current_block.setx(n)

    def extend(self):
        pos_x = self.blocks[-1].xcor()
        pos_y = self.blocks[-1].ycor()
        self.blocks.append(Turtle("square"))
        current_block = self.blocks[-1]
        current_block.color("white")
        current_block.penup()
        current_block.goto(pos_x, pos_y)

    def move_snake(self):
        for b in range(len(self.blocks) - 1, 0, -1):
            x_cor = self.blocks[b - 1].xcor()
            y_cor = self.blocks[b - 1].ycor()
            self.blocks[b].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for block in self.blocks:
            block.goto(1000, 1000)
        self.blocks.clear()
        self.blocks = []

        self.blocks.clear()
        self.create_snake()
        self.head = self.blocks[0]
