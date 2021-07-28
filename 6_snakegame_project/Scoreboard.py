from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard_table(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 250)
        self.score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.color("white")
        self.increase_score()
        self.hideturtle()
        self.update_score_board()


    def update_score_board(self):
        self.clear()
        self.write(arg=f"Score= {self.score} Highest_score = {self.highest_score}", move=False, align=ALIGNEMENT, font=FONT)

    def my_reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt","w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_score_board()

    def increase_score(self):
        self.score += 1
        self.update_score_board()


