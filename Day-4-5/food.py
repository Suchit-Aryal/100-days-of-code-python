import random
from turtle import Turtle
def random_pos():
    return (random.randint(-270,270),(random.randint(-270,270)))
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color('blue')
        self.pensize(20)
        self.set_food()


    def set_food(self):
        self.hideturtle()
        self.goto(random_pos())
        self.showturtle()


