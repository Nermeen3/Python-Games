from turtle import Turtle

class Dot(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.penup()
        self.x = 10
        self.y = 10

    def move_dot(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.x, y + self.y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def origin(self):
        self.bounce_y()
        self.bounce_x()
        self.goto(0, 0)
