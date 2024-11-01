# import modules
from tkinter import *


# define all functions
def clicked():
    button1.config(# TODO update the button config when it is clicked)


# create window
window = Tk()
window.title("Exercise 4")
window.geometry("300x350")

# create widgets
button1 = Button(window, fg="black", bg="white", text="Click me!", command=clicked)

# pack widgets into window container
button1.pack()

# open window
window.mainloop()
