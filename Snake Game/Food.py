from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.random_position()
        self.score = 0

    def random_position(self):
        x = random.randint(-200, 200)
        y = random.randint(-180, 180)
        self.goto(x, y)

