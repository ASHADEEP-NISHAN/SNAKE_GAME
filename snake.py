from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
class Snake():
    def __init__(self):
        self.segment = []
        self.create_snake()
    def create_snake(self):
        for i in range(0, 3):
            snake = Turtle("square")
            snake.color("White")
            snake.penup()
            snake.speed("fastest")
            snake.goto(STARTING_POS[i])
            self.segment.append(snake)
    def move(self):
        for position in range(len(self.segment) - 1, 0, -1):
            x_cor = self.segment[position - 1].xcor()
            y_cor = self.segment[position - 1].ycor()
            self.segment[position].goto(x_cor, y_cor)
        self.segment[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.segment[0].heading() == 0:
            self.segment[0].left(90)
        elif self.segment[0].heading() == 180:
            self.segment[0].right(90)

    def down(self):
        if self.segment[0].heading() == 0:
            self.segment[0].right(90)
        elif self.segment[0].heading() == 180:
            self.segment[0].left(90)
    def right(self):
        if self.segment[0].heading() == 90:
            self.segment[0].right(90)
        elif self.segment[0].heading() == 270:
            self.segment[0].left(90)
    def left(self):
        if self.segment[0].heading() == 90:
            self.segment[0].left(90)
        elif self.segment[0].heading() == 270:
            self.segment[0].right(90)
    def add_segment(self,position):
        snake = Turtle("square")
        snake.color("White")
        snake.penup()
        snake.speed("fastest")
        snake.goto(position)
        self.segment.append(snake)
    def extend(self):
        self.add_segment((self.segment[-1]).position())


