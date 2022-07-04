from turtle import Turtle

FONT = ('Courier', 12, 'normal')
ALIGN = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as f:
            self.highscore = int(f.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', 'w') as w:
                w.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
