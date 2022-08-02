from turtle import Screen
from padle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()
score_board = Score()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # Detect R paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    # Detect L paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

screen.exitonclick()
