import turtle as t


class MainTurtle(t.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(x=0, y=-280)

    def move_forward(self):

        self.forward(10)

    def move_backwards(self):

        self.forward(-10)

    def restart_turtle(self):

        self.goto(x=0, y=-280)