from turtle import Turtle
MOVE_DISTANCE=20
class Snake:
    def __init__(self):
        self.body_length = 3
        self.snake_body = []
        self.snake_position = (0, 0)
        self.make_snake()
        self.head=self.snake_body[0]
        self.head.color('blue')

    def add_segment(self,position):
        segment=Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_body.append(segment)
    def make_snake(self):
        for _ in range(self.body_length):
            self.add_segment(self.snake_position)
            self.snake_position=(self.snake_position[0]-20,0)
    def add_length(self):
        self.body_length+=1
        tail=self.snake_body[-1].position()
        self.add_segment(tail)

    def reset(self):
        for sanke in self.snake_body:
            sanke.goto(1000,1000)
        self.body_length = 3
        self.snake_body=[]
        self.make_snake()
        self.head = self.snake_body[0]
        self.head.color('blue')


    def move(self):
        for _ in range(len(self.snake_body)-1,0,-1):
            x_cor=self.snake_body[_-1].xcor()
            y_cor=self.snake_body[_-1].ycor()
            self.snake_body[_].goto(x_cor,y_cor)
        self.head.forward(MOVE_DISTANCE)

        x = self.head.xcor()
        y = self.head.ycor()

        if x > 280:
            self.head.setx(-280)
        elif x < -280:
            self.head.setx(280)

        if y > 280:
            self.head.sety(-280)
        elif y < -280:
            self.head.sety(280)

    def move_up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def move_right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)