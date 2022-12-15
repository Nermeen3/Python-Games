from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 50

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.max_cars = 10
        self.car_speed = 10

    def create_car(self):
        # random.randint(0, 6) make probability so it runs randomly
        car = Turtle()
        car.shape("square")
        car.penup()
        car.shapesize(1, 2, 1)
        car.color(random.choice(COLORS))
        car.goto(random.randint(280, 550), random.randint(-250, 250))
        car.setheading(180)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.speed(self.car_speed)
            car.forward(STARTING_MOVE_DISTANCE)
            if car.xcor() < -280:
                self.cars.remove(car)
                car.setx(-400)

    def increase_difficulty(self):
        self.max_cars += 10
        self.car_speed += MOVE_INCREMENT

    def check_collision(self, player):
        for car in self.cars:
            if player.distance(car) < 30:
                return False
        return True
