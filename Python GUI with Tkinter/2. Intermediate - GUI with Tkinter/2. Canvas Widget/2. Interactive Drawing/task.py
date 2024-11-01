# import modules
from tkinter import *


# define all functions
def draw_with_brush(event):
    # find the x and y positions where the user clicked the right mouse button
    x_position_of_click = event.x
    y_position_of_click = event.y

    # define a circle with the mouse click at its center
    x1 = x_position_of_click - 5
    y1 = y_position_of_click - 5
    x2 = x_position_of_click + 5
    y2 = y_position_of_click + 5
    colour = "green"
    outline = "blue"
    # draw a circle while button_1 active and mouse is moving
    # TODO create a oval at the mouse position


# create window
window = Tk()
window.title("Python GUI with tkinter canvas widget")
window.geometry("850x500")

# create widgets
canvas = # TODO create the canvas widget

# place widgets into window container using the pack layout
# TODO place the canvas widhet on the window

# bind widget events to functions
# TODO bind the input event for pressing the left mouse button while moving the mouse to the draw_with_brush function

# open window
window.mainloop()
