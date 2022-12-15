from turtle import Turtle
FONT = ('digital', 22, 'normal')
scores = [0, 0]

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.shapesize(1, 3, 1)
        self.print_score()

    def print_score(self):
        self.write(f"{scores[0]}          {scores[1]}", False, align="center", font=FONT)

    def increase_score(self, player):
        scores[player] += 1
        self.clear()
        self.print_score()
