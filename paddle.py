from turtle import Turtle


class Paddle:

    def __init__(self, position, flipped = False):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(position)

    def move_up(self):
        if self.paddle.ycor() <= 240:
            new_y = self.paddle.ycor() + 40
            self.paddle.goto(self.paddle.xcor(), new_y)
        
    def move_down(self):
        if self.paddle.ycor() >= -220:
            new_y = self.paddle.ycor() -40
            self.paddle.goto(self.paddle.xcor(), new_y)

    def follow_ball(self, ball):
        if ball.xcor() > 0 and self.paddle.ycor() < ball.ycor():
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 10)
        if  ball.xcor() > 0 and self.paddle.ycor() > ball.ycor():
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 10)
