# import modules
from tkinter import *


# define all functions
def say_hello():
    print("hello there!")


def popup_menu_event(event):
    # find the x and y positions where the user clicked the right mouse button
    x_position_of_click = event.x_root
    y_position_of_click = event.y_root
    # post/place the pop menu where the user clicked.
    popup_menu.post(x_position_of_click, y_position_of_click)


# create window
window = Tk()
window.title("Exercise 12")
window.geometry("400x300")

# create widgets
popup_menu = Menu(window)
menu_bar = Menu(window)

# TODO create 4 menu's on the menu_bar
# TODO create a submenu

# configure widgets
menu_bar.add_cascade(label="File", menu=file_menu)
# TODO configure your menus and menu commands

# bind widget events to functions
window.bind("<Button-3>", popup_menu_event)

# configure window
window.config(menu=menu_bar)

# open window
window.mainloop()
