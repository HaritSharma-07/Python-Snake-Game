from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.group = []
        self.create_snake()
        self.head = self.group[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.group.append(new_part)

    def extend_snake(self):
        self.add_segment(self.group[-1].position())

    def move(self):
        for segment in range(len(self.group)-1, 0,-1):
            new_x = self.group[segment -1].xcor()
            new_y = self.group[segment -1].ycor()
            self.group[segment].goto(new_x, new_y)
        self.group[0].forward(20)

    def reset(self):
        for part in self.group:
            part.goto(800,800)
        self.group.clear()
        self.create_snake()
        self.head = self.group[0]

    def up(self):
        if self.group[0].heading() != DOWN:
            self.group[0].setheading(UP)

    def down(self):
        if self.group[0].heading() != UP:
            self.group[0].setheading(DOWN)

    def s_left(self):
        if self.group[0].heading() != RIGHT:
            self.group[0].setheading(LEFT)

    def s_right(self):
        if self.group[0].heading() != LEFT:
            self.group[0].setheading(RIGHT)

