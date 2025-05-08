import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scores
from border import Boarder


screen = turtle.Screen()
screen.setup(width=800, height=550)
screen.title("Snake Game.")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scores = Scores()

upper_line = Boarder()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.17)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extent()
        scores.increase_scores()

    # Collision with walls
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 250 or snake.head.ycor() < -275:
        scores.reset()
        # snake.reset()
        is_game_on = False
        scores.game_over()

    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scores.reset()
            # snake.reset()
            is_game_on = False
            scores.game_over()

screen.exitonclick()
