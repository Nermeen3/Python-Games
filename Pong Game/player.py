from turtle import Turtle
# players = [Turtle() for i in range(2)]
scores = [0, 0]

class Player(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(1, 3, 1)
        self.goto(x, y)
        self.setheading(90)

    def move_player2(self):
        if self.ycor() >= 270:
            self.setheading(270)
        if self.ycor() <= -270:
            self.setheading(90)
        self.speed(50)
        self.forward(30)

    def up(self):
        if self.ycor() <= 220:
            self.sety(self.ycor() + 50)

    def down(self):
        if self.ycor() >= -220:
            self.sety(self.ycor() - 50)
