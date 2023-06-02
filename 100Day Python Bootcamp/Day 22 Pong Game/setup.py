from turtle import Turtle

def setup():
    drawer = Turtle()
    drawer.hideturtle()
    drawer.penup()
    drawer.goto(0, 300)
    drawer.pendown()
    drawer.pencolor("white")
    drawer.setheading(270)
    drawer.forward(600)
    
