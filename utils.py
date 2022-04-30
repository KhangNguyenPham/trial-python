import time
from random import choice


def is_clicked(x=0, y=0, turtle=None):
    if turtle:
        tx = turtle.xcor()
        ty = turtle.ycor()

        if tx - 50 < x < tx + 50 and ty - 50 < y < ty + 50:
            return True
    return False


def make_choice(turtle, choices):
    for _ in range(20):
        robot_choice = choice(choices)
        turtle.shape(robot_choice + '.gif')
        time.sleep(0.1)
    return robot_choice
