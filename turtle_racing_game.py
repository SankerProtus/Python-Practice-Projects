from turtle import Turtle
from turtle import Screen
import random

starting_y_position = [-200, -110, 0, 110, 200]
colors = ["red", "blue", "white", "yellow", "green"]
finish_line = 330
window = Screen()
window.setup(width=700, height=500)
window.bgcolor("black")
racing_turtles = []

for turtle_idx in range(len(starting_y_position)):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_idx])
    new_turtle.penup()
    new_turtle.goto(x=-330, y=starting_y_position[turtle_idx])
    racing_turtles.append(new_turtle)

choice = window.textinput(title="Enter your Bet", prompt="Which turtle gonna win the race?: ").lower()

is_race_on = False

if choice:
    is_race_on = True

while is_race_on:
    count, limit = 0, 2
    if choice not in colors:
        print("Invalid input. Please try again.")
        while count < limit:
            again = window.textinput(title="Enter your Bet", prompt="Which turtle is going to win the race?: ").lower()
            if again in colors:
                choice = again
                break
            count += 1

        if count == limit:
            print("Too many invalid attempts. Exiting...")
            is_race_on = False

    for racer in racing_turtles:
        if racer.xcor() > finish_line:
            is_race_on = False
            winner = racer.pencolor()
            if choice == winner:
                print(f"You won!\nThe {choice} turtle won the race.")
            else:
                print(f"Oops! You lose!\nThe {winner} turtle won the race.")

        racer.forward(random.randint(0, 10))

# -----------------------------TO BE CONTINUE. PRINT THE POSITION OF THE USER CHOICE-------------------------

window.exitonclick()
