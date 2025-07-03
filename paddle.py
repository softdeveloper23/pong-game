from turtle import Turtle

class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()  
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(1)
        self.shapesize(5, 1)  

class Left_Paddle(Paddle):
    def __init__(self) -> None:
        super().__init__()
        self.goto(-350, 0)
    
    def up(self):
        new_y = self.ycor() + 20  
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20  
        self.goto(self.xcor(), new_y)

class Right_Paddle(Paddle):
    def __init__(self) -> None:
        super().__init__()
        self.goto(350, 0)

    def up(self):
        new_y = self.ycor() + 20  
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20  
        self.goto(self.xcor(), new_y)