from turtle import Turtle , Screen
ALIGNMENT = "center"
FONT = ("Courier",18,"bold")
class GameScoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.high_sre()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def update(self):
        self.score = self.score + 1
        self.update_scoreboard()

    def high_sre(self):
        with open("snake_data.txt") as file:
            self.high_score = file.read()

    def reset_game(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("snake_data.txt", mode ="w") as file1:
                file1.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
