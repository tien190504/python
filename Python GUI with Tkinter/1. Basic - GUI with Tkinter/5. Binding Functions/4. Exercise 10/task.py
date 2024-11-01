# import modules
from tkinter import *

# define global variables
# TODO make a variable to store the previous colour


# define all functions
# TODO define a function that changes the window background to the previous colour.


def set_color_blue(event):
    window.config(bg="blue")


# create window
window = Tk()
window.title("Exercise 10")
window.geometry("300x300")


# bind widget events to functions
window.bind("<Button-1>", set_color_blue)
window.bind("<Button-3>", set_colour_previous)

# open window
window.mainloop()
