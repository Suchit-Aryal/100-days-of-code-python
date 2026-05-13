from turtle import Turtle
class MiddleLine(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.pensize(10)
        self.color('white')
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0,330)
        self.pendown()
        self.right(90)
        self.make_line()

    def make_line(self):
        while self.ycor()>=-380:
            self.forward(30)
            self.penup()
            self.forward(30)
            self.pendown()