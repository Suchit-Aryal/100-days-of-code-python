from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt", mode='r') as high:
            content=int(high.read())
        self.high_score =content
        high.close()
        self.score=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score:{self.score}    HighScore:{self.high_score}")

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("highscore.txt",mode='w') as high:
                high.write(f'{self.high_score}')
            high.close()
        self.score=0
        self.update_scoreboard()