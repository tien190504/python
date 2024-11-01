# import modules
from tkinter import *


# define all functions
def say_hello():
    print("hello there!")


# create window
window = Tk()
window.title("Python GUI with tkinter submenus")
window.geometry("400x300")

# create widgets
menu_bar = Menu(window)
file_menu = Menu(menu_bar)
save_menu = # TODO finish the declaration of the save_menu submenu.

# configure widgets
menu_bar.add_command(label="Hello!", command=say_hello)
menu_bar.add_command(label="Quit", command=window.quit)

menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=say_hello)
file_menu.add_command(label="Open", command=say_hello)
file_menu.add_separator()
file_menu.add_cascade(label="Save", menu=save_menu)

# TODO add a"Save..."  command to the save_menu
# TODO add a "Save as..." command to the save_menu submenu

# configure window
window.config(menu=menu_bar)

# open window
window.mainloop()
