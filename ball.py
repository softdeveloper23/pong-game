from turtle import Turtle

MOVE_DISTANCE = 20

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(1)
        self.shapesize(1, 1)

    def move(self):
        self.forward(MOVE_DISTANCE)
        new_y = self.ycor() + 10  
        new_x = self.ycor() + 10 
        self.goto(new_x, new_y)