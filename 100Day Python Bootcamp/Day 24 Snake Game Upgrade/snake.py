from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
DISTANCE_TO_MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_body()
        self.head = self.snake_body[0]
        
    def create_body(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[seg_num-1].xcor()
            new_y = self.snake_body[seg_num-1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(DISTANCE_TO_MOVE)

    def up(self):
        self.head.setheading(UP)
        self.move()

    def down(self):
        self.head.setheading(DOWN)
        self.move()

    def left(self):
        self.head.setheading(LEFT)
        self.move()

    def right(self):
        self.head.setheading(RIGHT)
        self.move()

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def add_segment(self, position):
        new_part = Turtle()
        new_part.penup()
        new_part.color("white")
        new_part.shape("square")
        new_part.goto(position)
        self.snake_body.append(new_part)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.claer()
        self.create_body()
        self.head = self.snake_body[0]