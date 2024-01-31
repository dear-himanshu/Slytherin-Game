import random
import turtle
from turtle import Turtle

class Blocks():

    def arrange(self):
        for position in range(-290,310,20):
            self.create_blocks((290,position))
            self.create_blocks((-290, position))
            self.create_blocks((position,290))
            self.create_blocks((position,-290))


    def create_blocks(self,position):
        new_blocks = Turtle("square")
        new_blocks.penup()
        new_blocks.color("blue")
        new_blocks.goto(position)


