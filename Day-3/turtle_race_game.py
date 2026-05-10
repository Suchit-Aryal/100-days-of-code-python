from turtle import Turtle,Screen
import random
colors=["red","blue","purple","green"]
screen=Screen()
screen.setup(width=900,height=700)
def make_finish_line():
    finish_line=Turtle(shape="square")
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.goto(400,350)
    finish_line.setheading(270)
    finish_line.pencolor()
    finish_line.pendown()
    finish_line.forward(700)
    finish_line.hideturtle()
turtle=[]
pos_y=-300
for t in range(0,4):
    nigo_turtle=Turtle(shape="turtle")
    nigo_turtle.color(colors[t])
    nigo_turtle.penup()
    nigo_turtle.goto(-400,pos_y)
    pos_y+=200
    turtle.append(nigo_turtle)
game_over=False
make_finish_line()
user_bet=screen.textinput(title="Make your bet",prompt="Choose a color:").lower()
while user_bet not in colors:
    user_bet=screen.textinput(title="Make your bet",prompt="Choose a color:").lower()
while not game_over:
    for t in turtle:
        t.forward(random.randint(5,20))
        current_position=t.position()
        if current_position[0]>401:
            winner=t.pencolor()
            print(f"{t.pencolor()} wins")
            if winner==user_bet:
                print("You win!!!!")
            else:
                print("Take the L loser")
            game_over=True

screen.setup(width=900,height=700)

screen.exitonclick()