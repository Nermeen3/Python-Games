from turtle import Turtle
FONT = ('Arial', 12, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.goto(0, 180)
        with open("highest.txt", "r") as file:
            self.highest = int(file.read())
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score}    Highest Score: {self.highest}", False, align="center", font=FONT)

    def renew_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def save_highest(self):
        if self.score > self.highest:
            with open("highest.txt", "w") as file:
                file.write(str(self.score))

    def game_over(self):
        self.goto(0, 0)
        self.save_highest()
        self.write("GAME OVER!", False, align="center", font=('Arial', 30, 'normal'))

