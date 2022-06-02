import turtle
import time
from utils import is_clicked, make_choice

#create a screen
screen = turtle.Screen()

# add shapes into turtle
turtle.register_shape('win.gif')

#crete turtle
robot = turtle.Turtle(shape='turtle')
rock = turtle.Turtle(shape='rock.gif')
paper = turtle.Turtle(shape='paper.gif')
scissor = turtle.Turtle(shape='scissor.gif')

# move turtle to new pos
robot.sety(200)
rock.goto(-200, -200)
paper.sety(-200)
scissor.goto(200, -200)

# click func
def choose_shape(x, y):
    player_choice = None
    robot_choice = None
    choices = ['rock', 'paper', 'scissor']

    # check user click 
    if is_clicked(x, y, rock):
        player_choice = 'rock'
    if is_clicked(x, y, paper):
        player_choice = 'paper'
    if is_clicked(x, y, scissor):
        player_choice = 'scissor'

    # robot random choices
    robot_choice = make_choice(robot, choices)

    # show result
    if player_choice == 'rock' and robot_choice == 'rock':
        turtle.Turtle(shape='draw.gif')
    if player_choice == 'rock' and robot_choice == 'paper':
        turtle.Turtle(shape='lose.gif')
    if player_choice == 'rock' and robot_choice == 'scissor':
        turtle.Turtle(shape='win.gif')   

# listen for mouse click
screen.onclick(choose_shape)

turtle.done()
