from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score1=0
        self.score2=0
        self.goto(-150,330)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score1}\t\t{self.score2}",font=("Arial", 24, "bold"))