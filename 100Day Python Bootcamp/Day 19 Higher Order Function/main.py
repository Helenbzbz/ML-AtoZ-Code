from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make a bet", prompt = "Which turtle win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
reach_goal = False


def setup_turtle(turtle, x_cor, y_cor):
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(x = x_cor, y = y_cor)

turtle_list = [Turtle(), Turtle(), Turtle(), Turtle(), Turtle(), Turtle()]


def check_status():
    for turtle in turtle_list:
        if turtle.xcor() > 180:
            return turtle.pencolor()
    return False


y_cord = -70
for i in range(len(turtle_list)):
    turtle_list[i].color(colors[i])
    turtle_list[i].shape("turtle")
    setup_turtle(turtle_list[i], -200, y_cord)
    y_cord += 30

while reach_goal == False:
    for turtle in turtle_list:
        turtle.forward(random.randint(1, 10))
    reach_goal = check_status()

if reach_goal == user_bet.lower():
    print("You win!")
else:
    print(f"Sorry, the winner is {reach_goal}.")

screen.exitonclick()