from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.player=Turtle(shape="turtle")
        self.player.penup()
        self.player.left(90)
        self.reset_position()


    def move_up(self):
        if self.player.ycor()<FINISH_LINE_Y:
            self.player.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.player.ycor()>-FINISH_LINE_Y:
            self.player.backward(MOVE_DISTANCE)

    def reset_position(self):
        self.player.goto(0, -280)