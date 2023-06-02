from turtle import Turtle
INITIAL_ANGLE = 30
DISTANCE_TO_MOVE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.object = self.create_ball()
        self.status = True
        self.y_index = 1
        self.x_index = 1
    
    def create_ball(self):
        new_ball = Turtle()
        new_ball.speed("fast")
        new_ball.penup()
        new_ball.color("white")
        new_ball.shape("circle")
        new_ball.goto(0,0)
        return new_ball
    
    def move(self):
        new_x = self.object.xcor() + DISTANCE_TO_MOVE*self.x_index
        new_y = self.object.ycor() + DISTANCE_TO_MOVE*self.y_index
        self.object.goto(new_x, new_y)

    def refresh(self):
        self.object.goto(0,0)