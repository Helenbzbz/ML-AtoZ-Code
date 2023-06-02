from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
CAR_FREQUENCY = 9
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = (1)
        self.cars = []

    def generate_car(self):
    # Slow this down by creating a random chance of creating or not
        if random.randint(0, 10) > 7:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            ycor = random.randint(-12, 13)
            new_car.goto(280, ycor*20)
            self.cars.append(new_car)
    
    def check_move(self):
        for car in self.cars:
            if car.xcor() > -350:
                car.goto(car.xcor()-MOVE_INCREMENT, car.ycor())
