from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5 ,stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()



    def fill(self):
        list=[]
        for i in range(-270,290,20):
            list.append(i)
        return list

    def refresh(self):
        self.fill()
        random_x = random.choice(self.fill())
        random_y = random.choice(self.fill())
        self.goto(random_x, random_y)
