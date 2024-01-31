import random
from turtle import Turtle
import turtle
STARTING_POSITIONS = [(10,-10), (-10,-10), (-30,-10)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
turtle.colormode(255)
COLOR_LIST=[(236, 234, 230), (238, 229, 234), (228, 238, 232), (227, 233, 240),
              (237, 40, 115), (142, 27, 70), (219, 162, 59),
 (238, 71, 36), (14, 144, 89), (182, 166, 43), (31, 126, 191), (54, 190, 229)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
            new_segment=Turtle("square")
            new_segment.penup()
            new_segment.color(random.choice(COLOR_LIST))
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        #add new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



