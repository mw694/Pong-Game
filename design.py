from turtle import Turtle
starting_point = -280
class Centerline:

    def __init__(self):
        self.center_line()

    def center_line(self):
        y_position = starting_point
        for _ in range (30):
             new_rec = Turtle()
             new_rec.shape("square")
             new_rec.shapesize(stretch_wid=0.2, stretch_len=1)
             new_rec.color("white")
             new_rec.setheading(90)
             new_rec.penup()
             new_rec.goto(x=0, y=y_position)
             y_position += 30



