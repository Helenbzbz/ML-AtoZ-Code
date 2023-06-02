from turtle import Screen
from setup import setup
from paddle import Left_Paddle, Right_Paddle
from ball import Ball
from score import Scoreboard
import time


screen = Screen()
screen.setup(width = 1000, height = 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

setup()
left_paddle = Left_Paddle()
right_paddle = Right_Paddle()
screen.onkey(key="Up", fun=left_paddle.up)
screen.onkey(key="Down", fun=left_paddle.down)
screen.onkey(key="w", fun=right_paddle.up)
screen.onkey(key="s", fun=right_paddle.down)
ball = Ball()
score = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if ball.object.ycor() > 280 or ball.object.ycor() < -280:
        ball.y_index *= -1
    elif ball.object.distance(left_paddle.paddle) < 25 or ball.object.distance(right_paddle.paddle) < 25:
        ball.x_index *= -1
    elif ball.object.xcor() > 500:
        ball.refresh()
        score.increase_leftscore()
        screen.update()
        time.sleep(0.5)
    elif ball.object.xcor() < -500:
        ball.refresh()
        score.increase_rightscore()
        screen.update()
        time.sleep(0.5)

    ball.move()


screen.exitonclick()