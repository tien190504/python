# import modules
from tkinter import *


# define all functions
# TODO define a function that updates the text option of label1 with "Hello"


# TODO define a function that updates the text option of label1 with "Goodbye"


# create window
window = Tk()
window.title("Exercise 9")
window.geometry("300x300")

# create widgets
label1 = Label()

# place widgets into window container using the pack layout
label1.pack()

# bind widget events to functions
window.bind("# TODO add the input event for when the mouse enters the window.", say_hello)
window.# TODO bind the window to the input event for when the mouse leaves the window

# open window
window.mainloop()
