from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.hideturtle()
        self.goto(-50,260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level :{self.level}",font=FONT)

    def level_up(self):
        self.level+=1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(-50,0)
        self.write(f"Game Over!!!\nLevel:{self.level}",font=FONT)