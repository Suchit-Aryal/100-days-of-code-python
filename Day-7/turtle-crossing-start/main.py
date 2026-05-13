import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player=Player()
cars=CarManager()
score_board=Scoreboard()

screen.onkeypress(key="w",fun=player.move_up)
screen.onkeypress(key="s",fun=player.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.make_cars()
    cars.move()
    for car in cars.all_cars:
        if player.player.distance(car)<30:
            score_board.game_over()
            game_is_on=False
        if player.player.ycor()>=280:
            player.reset_position()
            cars.level_up()
            score_board.level_up()

screen.exitonclick()