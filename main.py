from turtle import Screen
from paddle import Left_Paddle, Right_Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  

right_paddle = Right_Paddle()
left_paddle = Left_Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")  
screen.onkey(left_paddle.down, "s")  

game_is_on = True
while game_is_on:
    time.sleep(ball.movement_speed)
    screen.update() 
    ball.move()
    
    # Detects a collision with the wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detects a collision with the paddles.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detects right paddle misses.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # Detects left paddle misses.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
