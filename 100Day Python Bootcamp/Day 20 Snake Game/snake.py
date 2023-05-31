from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
DISTANCE_TO_MOVE = 10

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_body()
        
    def create_body(self):
        for position in STARTING_POSITION:
            new_part = Turtle()
            new_part.speed("fastest")
            new_part.penup()
            new_part.color("white")
            new_part.shape("square")
            new_part.goto(position)
            self.snake_body.append(new_part)

    def move(self):
        for seg_num in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[seg_num-1].xcor()
            new_y = self.snake_body[seg_num-1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].forward(DISTANCE_TO_MOVE)

    def up(self):
        self.snake_body[0].setheading(90)
        self.move()

    def down(self):
        self.snake_body[0].setheading(270)
        self.move()

    def right(self):
        self.snake_body[0].setheading(0)
        self.move()

    def left(self):
        self.snake_body[0].setheading(180)
        self.move()
