from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        x_dir = self.xcor() + self.x
        y_dir = self.ycor() + self.y
        self.goto(x_dir, y_dir)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1










