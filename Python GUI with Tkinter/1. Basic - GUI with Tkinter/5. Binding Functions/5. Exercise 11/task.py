# import modules
from tkinter import *

# define global variables
previous_colour = "yellow"


# define all functions
def set_colour_previous(event):
    global previous_colour
    window.config(bg=previous_colour)


def set_color_blue(event):
    window.config(bg="blue")


# create window
window = Tk()
window.title("Exercise 11")
window.geometry("300x300")


# bind widget events to functions
window.bind("<Button-1>", set_color_blue)
window.bind("<Button-3>", set_colour_previous)
# TODO bind to the windows input event for the right and left arrow keys

# open window
window.mainloop()
