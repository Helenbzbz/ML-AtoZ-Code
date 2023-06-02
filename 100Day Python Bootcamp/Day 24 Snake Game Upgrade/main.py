from turtle import Screen
from snake import Snake
from food import Food
from socreboard import scoreboard
import time


screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()


snake = Snake()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
food = Food()
score = scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Detect collison with food
    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    # Detection collison with wall
    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -280 or snake.snake_body[0].ycor() < -280 or snake.snake_body[0].ycor() > 280:
        score.reset()
        game_is_on = False
    
    # Detection collison with tail
    for comp in snake.snake_body:
        if comp == snake.head:
            pass
        elif snake.head.distance(comp) < 10:
            game_is_on = False
            score.reset()

screen.exitonclick()