# import modules
from tkinter import *


# define all functions
def draw_rectangle(event):
    rectangle_height = 20
    rectangle_length = rectangle_height * 2

    # find the x and y positions where the user clicked the right mouse button
    # TODO get the x position from the event
    # TODO get the y position from the event

    # define a rectangle with the mouse click at its center
    # TODO draw a rectangle with the mouse click at it's center


# create window
window = Tk()
window.title("Exercise 16")
window.geometry("850x500")

# create widgets
canvas = Canvas(window)

# place widgets into window container using the pack layout
canvas.pack(fill=BOTH, expand=1)

# bind widget events to functions
# TODO bind the draw_rectangle function to the input event for mouse button 1 pressed and mouse moving

# open window
window.mainloop()
