from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x_cor, 0)
        self.shapesize(stretch_wid=5,stretch_len=1)

    def move_up(self):
        if self.ycor()<350:
            new_y = self.ycor()+20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor()>-350:
            new_y = self.ycor()-20
            self.goto(self.xcor(), new_y)