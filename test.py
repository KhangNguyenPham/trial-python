from traceback import print_tb
import turtle

turtle.setup(800, 600)
#create a screen
screen = turtle.Screen()

# add shapes into turtle
turtle.register_shape('win.gif')
turtle.register_shape('lose.gif')
turtle.register_shape('draw.gif')
turtle.register_shape('paper.gif')
turtle.register_shape('rock.gif')
turtle.register_shape('scissor.gif')



#crete turtle
rock = turtle.Turtle(shape='rock.gif')

rock.goto(100, 100)

def is_clicked(x=0, y=0, turtle=None):
    if turtle:
        tx = turtle.xcor()
        ty = turtle.ycor()

        if tx - 50 < x < tx + 50 and ty - 50 < y < ty + 50:
            return True
    return False
    


def choose_shape(x, y):
    print(is_clicked(x, y, rock))


# listen for mouse click
screen.onclick(choose_shape)


turtle.done()