from turtle import Turtle,Screen
import time
from middle_line import MiddleLine
from scoreboard import ScoreBoard
from paddel import Paddle
from ball import Ball
screen=Screen()
screen.setup(width=800,height=800)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()




score_board=ScoreBoard()
middle_line=MiddleLine()


paddel1=Paddle(-380)
paddel2=Paddle(380)
ball=Ball()


screen.onkeypress(key='w',fun=paddel1.move_up)
screen.onkeypress(key='s',fun=paddel1.move_down)

screen.onkeypress(key='Up',fun=paddel2.move_up)
screen.onkeypress(key='Down',fun=paddel2.move_down)


game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.distance(paddel1)<40:
        ball.collision_x()
    if ball.distance(paddel2)<40:
        ball.collision_x()
    if ball.ycor()>380 or ball.ycor()<-380:
        ball.collision_y()
    if ball.xcor()>400:
        ball.reset_position()
        score_board.score1+=1
        score_board.update_score()
    if ball.xcor() < -400:
        ball.reset_position()
        score_board.score2 += 1
        score_board.update_score()
screen.exitonclick()