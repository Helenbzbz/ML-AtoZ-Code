from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.player = self.create_player()
        self.refresh()
    
    def create_player(self):
        new_ball = Turtle()
        new_ball.speed("fast")
        new_ball.penup()
        new_ball.color("black")
        new_ball.shape("turtle")
        return new_ball
    
    def refresh(self):
        self.player.setheading(90)
        self.player.goto(0, -280)

    def up(self):
        if self.player.ycor() < FINISH_LINE_Y:
            self.player.forward(MOVE_DISTANCE)