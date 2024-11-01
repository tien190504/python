# import modules
from tkinter import *


# define all functions
# TODO define your 17 new functions. Each one must print out the name of the menu command it is binded to.

def popup_menu_event(event):
    # find the x and y positions where the user clicked the right mouse button
    x_position_of_click = event.x_root
    y_position_of_click = event.y_root
    # post/place the pop menu where the user clicked.
    popup_menu.post(x_position_of_click, y_position_of_click)


# create window
window = Tk()
window.title("Exercise 13")
window.geometry("400x300")

# create widgets
popup_menu = Menu(window)
menu_bar = Menu(window)
e# TODO create your widgets

# configure widgets
# TODO configure your menus
popup_menu.add_command(label="Copy")
popup_menu.add_command(label="Paste")

# bind widget events to functions
window.bind("<Button-3>", popup_menu_event)

# configure window
window.config(menu=menu_bar)

# open window
window.mainloop()
