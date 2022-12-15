from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def move_snake(self):
        for i in range(len(self.squares)-1, 0, -1):
            # self.squares[i].goto(self.squares[i-1].xcor(), self.squares[i-1].ycor())
            new_x = self.squares[i - 1].xcor()
            new_y = self.squares[i - 1].ycor()
            self.squares[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def check_collision(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if x <= -280 or x >= 280 or y <= -210 or y >= 210:
            return False
        for square in self.squares[1:]:
            if self.head.distance(square) < 10 and square != self.head:
                return False
        return True

    def add_square(self, position):
        squares = Turtle("square")
        squares.color("white")
        squares.penup()
        squares.goto(position)
        self.squares.append(squares)

    def extend(self):
        self.add_square(self.squares[-1].position())

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