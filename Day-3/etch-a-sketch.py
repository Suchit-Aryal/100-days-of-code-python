from turtle import Turtle,Screen
def move_forward():
    timmy.forward(10)
def move_backward():
    timmy.backward(10)
def turn_right():
    timmy.right(10)
def turn_left():
    timmy.left(10)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.hideturtle()
    timmy.home()
    timmy.pendown()
    timmy.showturtle()

timmy=Turtle()
screen=Screen()


screen.listen()
screen.onkey(key="c",fun=clear)
screen.onkeypress(key="w",fun=move_forward)
screen.onkeypress(key="a",fun=turn_left)
screen.onkeypress(key="s",fun=move_backward)
screen.onkeypress(key="d",fun=turn_right)


screen.exitonclick()