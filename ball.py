import time

from turtle import Turtle
starting_position = (0, 0)
class Ball:

    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.shapesize(0.5)
        self.ball.penup()
        self.ball.goto(starting_position)
        self.x_move = 10
        self.y_move = 10


    def move(self):
        self.ball.setx(self.ball.xcor() + self.x_move)
        self.ball.sety(self.ball.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.ball.goto(0, 0)    
        self.bounce_x()
