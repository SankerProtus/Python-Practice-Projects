import turtle


class Boarder(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pensize(3)
        self.color("red")
        self.goto(x=-450, y=250)
        self.pendown()
        for x_cors in range(-450, 450, 10):
            self.goto(x=x_cors, y=240)
