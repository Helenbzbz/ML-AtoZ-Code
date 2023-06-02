from turtle import Turtle

STARTING_POSITION_LEFT = (-440, 0)
STARTING_POSITION_RIGHT = (440, 0)
PADDLE_LENGTH = 1
PADDLE_WIDTH = 5
DISTANCE_TO_MOVE = 10

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

    def create_paddle(self, position):
        new_part = Turtle()
        new_part.speed("fastest")
        new_part.penup()
        new_part.color("white")
        new_part.shape("square")
        new_part.shapesize(PADDLE_WIDTH, PADDLE_LENGTH)
        new_part.goto(position)
        return new_part
        
class Left_Paddle(Paddle):
    def __init__(self):
        super().__init__()
        self.paddle = self.create_paddle(STARTING_POSITION_LEFT)

    def up(self):
        ycor = self.paddle.ycor()
        if ycor < 230:
            new_cor = (self.paddle.xcor(), ycor+DISTANCE_TO_MOVE)
            self.paddle.goto(new_cor)

    def down(self):
        ycor = self.paddle.ycor()
        if ycor > -230:
            new_cor = (self.paddle.xcor(), ycor-DISTANCE_TO_MOVE)
            self.paddle.goto(new_cor)


class Right_Paddle(Paddle):
    def __init__(self):
        super().__init__()
        self.paddle = self.create_paddle(STARTING_POSITION_RIGHT)

    def up(self):
        ycor = self.paddle.ycor()
        if ycor < 230:
            new_cor = (self.paddle.xcor(), ycor+DISTANCE_TO_MOVE)
            self.paddle.goto(new_cor)

    def down(self):
        ycor = self.paddle.ycor()
        if ycor > -230:
            new_cor = (self.paddle.xcor(), ycor-DISTANCE_TO_MOVE)
            self.paddle.goto(new_cor)