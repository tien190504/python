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
window.title("Python GUI with tkinter popup menus")
window.geometry("400x300")

# create widgets
popup_menu = # TODO finish the declaration
menu_bar = Menu(window)
file_menu = Menu(menu_bar)
save_menu = Menu(file_menu)


# configure widgets
menu_bar.add_command(label="Hello!", command=say_hello)
menu_bar.add_command(label="Quit", command=window.quit)

menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=say_hello)
file_menu.add_command(label="Open", command=say_hello)
file_menu.add_separator()
file_menu.add_cascade(label="Save", menu=save_menu)

save_menu.add_command(label="Save...")
save_menu.add_command(label="Save as...")

# TODO add a command called "Copy" to the popup_menu
popup_menu.# TODO add a command called "Paste" to the popup_menu

# bind widget events to functions
window.# TODO bind the windows input event for the right mouse button to the function popup_menu_event

# configure window
window.config(menu=menu_bar)


# open window
window.mainloop()
