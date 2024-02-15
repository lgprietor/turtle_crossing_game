import turtle as t

FONT = ("Courier", 15, "bold")


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-240, y=270)
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write(f"Game over", move=False, align="center", font=FONT)
