# import modules
from tkinter import *


# define all functions
def say_hello():
    print("hello there!")

# create window
# TODO create the window
window.# TODO give your window a title
window.# TODO give your window some geometry - 400x300 should be ok.


# create widgets
menu_bar = Menu(window)

# configure widgets
menu_bar.add_command(label="Hello!", command=say_hello)
menu_bar.add_command(label="Quit", command=window.quit)

# configure window
window.config(menu=menu_bar)

# open window
window.mainloop()
