import turtle as t
from cars import Car
from main_turtle import MainTurtle
from scoreboard import Scoreboard
import time
import gc

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Project by Luisgap")
screen.colormode(255)
screen.listen()
screen.tracer(0)

main_turtle = MainTurtle()
scoreboard = Scoreboard()

screen.onkeypress(main_turtle.move_forward,"Up")
screen.onkeypress(main_turtle.move_forward,"w")
screen.onkeypress(main_turtle.move_forward,"W")

screen.onkeypress(main_turtle.move_backwards,"Down")
screen.onkeypress(main_turtle.move_backwards,"s")
screen.onkeypress(main_turtle.move_backwards,"S")

game_is_on = True

cars_objects = []
cars_limit = 10
count = 0

while game_is_on:

    screen.update()
    time.sleep(0.1)
    # print(f" The count is: {count}")

    # # Detecting collisions with cars (1):
    #
    # for i in cars_objects:
    #
    #     if i.distance(main_turtle) < 25:
    #         game_is_on = False
    #         print(i.distance(main_turtle))

    # print(count)
    # Detecting collisions with cars (2):

    count += 1

    for i in cars_objects:

        if i.distance(main_turtle) < 25:
            game_is_on = False
            scoreboard.game_over()
            # print(i.distance(main_turtle))

    if count >= cars_limit:

        new_car = Car()
        cars_objects.append(new_car)
        count = 0

    for i in cars_objects:
        i.move()

        # Detecting collisions with cars (3):

        if i.distance(main_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()
            # print(i.distance(main_turtle))

    # Detect passing level:

    if main_turtle.ycor() > 290:

        cars_limit -= 1

        main_turtle.restart_turtle()
        scoreboard.update_level()

    # print(f"The cars limit is: {cars_limit}")
    # print(f"The quantity of cars is {len(cars_objects)}")

    # Cleaning memory:

    for i in cars_objects:
        if i.xcor() < -1000:
            i.reset()
            i.hideturtle()
            cars_objects.remove(i)
            del i

screen.exitonclick()
