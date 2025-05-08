import random
import turtle

food_length, food_width = 0.7, 0.7


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=food_length, stretch_wid=food_width)
        self.penup()
        self.refresh_food()

    def refresh_food(self):
        new_x = random.randint(-350, 350)
        new_y = random.randint(-240, 240)
        self.goto(new_x, new_y)
