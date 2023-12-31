from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("orange")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")
        self.move_food()

    def move_food(self):
        x_cor=random.randint(-280,280)
        y_cor=random.randint(-280,280)
        new_position=(x_cor,y_cor)
        self.goto(new_position)
