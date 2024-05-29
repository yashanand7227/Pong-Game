import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5)
        self.penup()
        self.color('white')
        self.goto(0,0)
        self.xmove=10
        self.ymove=10
        self.move_speed = 0.1

    def move_ball(self):
        new_x =self.xcor()+self.xmove
        new_y = self.ycor()+self.ymove
        self.goto(new_x,new_y)

    def bounce(self):
        self.ymove *= -1

    def hit_paddle(self):
        self.xmove *= -1
        self.move_speed*=0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.hit_paddle()