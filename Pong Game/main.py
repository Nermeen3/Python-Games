from turtle import Screen
from player import Player
from dot import Dot
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

player1 = Player(-380, 0)
player2 = Player(360, 0)
dot = Dot()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

while True:
    screen.update()
    time.sleep(0.05)
    # player2.move_player2()

    if dot.ycor() >= 270 or dot.ycor() <= -270:
        dot.bounce_y()

    if (int(dot.distance(player2)) < 30 and dot.xcor() >= 350) or (int(dot.distance(player1)) < 40 and dot.xcor() <= -370):
        print("hit")
        dot.bounce_x()
    print(dot.xcor(), dot.distance(player1), dot.distance(player2))

    if dot.xcor() <= -410:
        scoreboard.increase_score(1)
        dot.origin()
    elif dot.xcor() >= 410:
        scoreboard.increase_score(0)
        dot.origin()

    dot.move_dot()

screen.exitonclick()
