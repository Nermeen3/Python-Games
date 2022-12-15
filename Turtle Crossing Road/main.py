import time
from turtle import Screen
from player import Player
from turtle import Turtle
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Turtle()
player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.move, "w")

print(time.time_ns(), time.time())

while car.check_collision(player):
    time.sleep(0.07)
    screen.update()

    if player.ycor() > player.FINISH_LINE_Y:
        scoreboard.level_up()
        player.new_level()
        car.increase_difficulty()

    if len(car.cars) < car.max_cars:
        car.create_car()
    car.move_cars()

scoreboard.game_over()
screen.exitonclick()
