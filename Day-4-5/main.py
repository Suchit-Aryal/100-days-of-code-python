from turtle import Screen
import time
from snake_body import Snake
from food import Food
from score_board import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board=ScoreBoard()

screen.listen()
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    while snake.head.distance(food.position())<15:
        food.set_food()
        score_board.increase_score()
        snake.add_length()
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment.position())<10:
            score_board.reset()
            snake.reset()
screen.exitonclick()
