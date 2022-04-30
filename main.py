import turtle
import time
from utils import is_clicked, make_choice

#create a screen
screen = turtle.Screen()

# add shapes into turtle
turtle.register_shape('win.gif')
turtle.register_shape('lose.gif')
turtle.register_shape('draw.gif')
turtle.register_shape('paper.gif')
turtle.register_shape('rock.gif')
turtle.register_shape('scissor.gif')


# click func
def choose_shape(x, y):
    pass


# listen for mouse click
screen.onclick(choose_shape)

turtle.done()