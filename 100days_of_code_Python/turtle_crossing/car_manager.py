from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_POSITION = [(300, 210), (300, 140), (300, 70), (300, 0), (300, -70), (300, -140), (300, -210)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.pace = STARTING_MOVE_DISTANCE

    def create_new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(random.choice(STARTING_POSITION))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.pace)

    def speed_up(self):
        self.pace += MOVE_INCREMENT
