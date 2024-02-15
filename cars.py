import turtle as t
import random


class Car(t.Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(180)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.red = random.randint(0, 255)
        self.green = random.randint(0, 255)
        self.blue = random.randint(0, 255)
        self.color((self.red, self.green, self.blue))
        self.new_y = random.randint(-250, 250)
        self.goto(x=1000,y=self.new_y)

    def move(self):
        self.forward(20)

    def __del__(self):
        print("Object destroyed")