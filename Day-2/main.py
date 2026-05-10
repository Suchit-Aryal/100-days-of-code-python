import turtle
import colorgram
from turtle import Turtle,Screen
import random
def random_color():
    return random.randint(0,len(colors)-1)
colors=colorgram.extract("img.jpg",10)
timmy=Turtle()
turtle.colormode(255)
timmy.speed('fastest')
timmy.penup()
timmy.goto(-400,-300)
timmy.pendown()
def square():
    while timmy.ycor()<=300:
        rgb = colors[random_color()].rgb
        timmy.color(rgb.r, rgb.g, rgb.b)
        timmy.dot(15)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        current_post=timmy.position()
        if current_post[0]>=400:
            timmy.penup()
            timmy.goto(-400,current_post[1]+50)
            timmy.pendown()
square()
screen=Screen()
screen.colormode(255)
screen.exitonclick()