from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240, 270)
        self.level = 1
        self.print_level()

    def print_level(self):
        self.write(f"Level: {self.level}", False, align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.print_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Courier", 24, "normal"))



