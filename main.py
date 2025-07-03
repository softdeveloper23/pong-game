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
    
    # Add a small delay to prevent the loop from running too fast
    # You can adjust this or remove it based on your needs
    

screen.exitonclick()
