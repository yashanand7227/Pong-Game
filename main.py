from turtle import Screen
from paddles import Paddle
from ball import Ball
import time, random
from scoreboard import Scoreboard

POSITIONS = [(-350, 0), (350,0)]
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()
paddle1 = Paddle(POSITIONS[1])
paddle2 = Paddle(POSITIONS[0])
ball = Ball()

screen.listen()
screen.onkey(paddle1.move_up, 'Up')
screen.onkey(paddle1.move_down, 'Down')
screen.onkey(paddle2.move_up, 'w')
screen.onkey(paddle2.move_down, 's')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    #detect collision with wall
    if abs(ball.ycor()) > 280:
        ball.bounce()

    # detect collision with paddles
    if abs(ball.xcor()) > 335:
        if paddle2.distance(ball)<50:
            ball.hit_paddle()
        elif paddle1.distance(ball)<50:
            ball.hit_paddle()

    #detect out of bounds
    #r sided miss
    if ball.xcor()>380:
        scoreboard.score1 += 1
        ball.reset_position()
    #l sided miss
    if ball.xcor()<-380:
        scoreboard.score2 += 1
        ball.reset_position()
    scoreboard.update_score()

screen.exitonclick()