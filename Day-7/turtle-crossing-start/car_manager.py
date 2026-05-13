import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.movement_speed=STARTING_MOVE_DISTANCE

    def make_cars(self):
        chance=random.randint(1,6)
        if chance==1:
            new_car=Turtle(shape="square")
            new_car.shapesize(stretch_wid=1,stretch_len=5)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_position=random.randint(-270,260)
            new_car.goto(300,random_position)
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars:
            cars.backward(self.movement_speed)

    def level_up(self):
        self.movement_speed+=MOVE_INCREMENT