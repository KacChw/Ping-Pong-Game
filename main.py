from turtle import Turtle, Screen
from paddle import Paddle
from bojo import Bojo
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
bojo = Bojo()
l_score = Scoreboard((-100, 220))
r_score = Scoreboard((100, 220))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    ball.move()
    time.sleep(ball.speed)
    screen.update()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.jump()

    if ball.xcor() > 380:
        ball.reset()
        l_score.update_l()
        ball.speed *= 0.85

    if ball.xcor() < -380:
        ball.reset()
        r_score.update_r()
        ball.speed *= 0.85

screen.exitonclick()

