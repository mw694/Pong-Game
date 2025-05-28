from turtle import Screen, Turtle
from design import Centerline
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
import time

ball_info = Ball()
score = Scoreboard()

screen = Screen()

round = screen.textinput(title = "Round", prompt = "How many rounds would you like to play?: ")
speed = screen.textinput(title = "Speed Mode", prompt = "Choose the speed: ").lower()

round = int(round)
if speed == "slow":
    ball_speed = 0.1
    
elif speed == "normal":
    ball_speed = 0.05
    
elif speed == "fast":
    ball_speed = 0.01

else:
    ball_speed = 0.05

screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Ping Pong Piang")
screen.tracer(0)
Centerline()
screen.listen()

left_paddle = Paddle((-370, 0))
right_paddle = Paddle((370, 0))

screen.onkey(key = "w", fun = left_paddle.move_up)
screen.onkey(key = "s", fun = left_paddle.move_down)

current_round = 1
while current_round <= round:
    game_is_on = True
    while game_is_on:
        right_paddle.follow_ball(ball_info.ball)
        ball_info.move()
        screen.update()
        time.sleep(ball_speed)

        if ball_info.ball.ycor() >= 290 or ball_info.ball.ycor() <= -290:
            ball_info.bounce_y()

        if ball_info.ball.distance(left_paddle.paddle) < 50 and ball_info.ball.xcor() < -340:
            if ball_info.x_move < 0:
                ball_info.bounce_x()

        if ball_info.ball.distance(right_paddle.paddle) < 50 and ball_info.ball.xcor() > 340:
            if ball_info.x_move > 0:
                ball_info.bounce_x()

        if ball_info.ball.xcor() > 380:
            score.l_score_increase()
            ball_info.reset()
            game_is_on = False

        if ball_info.ball.xcor() < -380:
            score.r_score_increase()
            ball_info.reset()
            game_is_on = False

    current_round += 1

if score.l_score > score.r_score:
    print("You win!")

elif score.r_score > score.l_score:
    print("Com win!")

else:
    print("It's a tie!")


screen.exitonclick()