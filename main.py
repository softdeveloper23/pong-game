from turtle import Screen
from paddle import Left_Paddle, Right_Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  

right_paddle = Right_Paddle()
left_paddle = Left_Paddle()
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")  
screen.onkey(left_paddle.down, "s")  


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update() 
    ball.move() 
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()
