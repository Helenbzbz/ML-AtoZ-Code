import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
print(player.player.position())
screen.onkey(key = "Up", fun = player.up)

car_manage = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manage.generate_car()
    car_manage.check_move()

    for car in car_manage.cars:
        if player.player.distance(car) < 15:
            score.game_over()
            game_is_on = False
    
    if player.player.ycor() >= 280:
        player.refresh()
        score.level += 1
        car_manage.speed += 1
        score.update()

    screen.update()

screen.exitonclick()


