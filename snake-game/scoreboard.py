import turtle

Font = ("Verdana", 18, "normal")


class Scores(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_scores.txt.txt") as game_data:
            self.high_score = int(game_data.read())
        self.color("white")
        self.penup()
        self.goto(x=-380, y=250)
        self.hideturtle()
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="left", font=Font)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_scores.txt.txt", "w") as game_data:
                game_data.write(f"{self.high_score}")
        self.score = 0
        self.update_scores()

    def increase_scores(self):
        self.score += 1
        self.update_scores()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over.", align="center", font=Font)
