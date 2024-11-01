# import modules
from tkinter import *

# create window
window = Tk()
# TODO give the window a title
# TODO make the window 450 by 100 pixels

# create widgets
scale = Scale(window)
spinbox = Spinbox(window)

# configure widgets
scale.config(from_=10, to=500, orient=HORIZONTAL)
spinbox_values = ("One", "Two", "Three")
spinbox.config(values=spinbox_values)

# place widgets into window container using the pack layout
# TODO pack the scale and spinbox widgets into the window

# open window
window.mainloop()
