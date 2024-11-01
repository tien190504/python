# import modules
from tkinter import *

# define variables with global scope
counter = 0


# define all functions
def increase_value(event):
    global counter
    counter = counter + 1
    label1.config(text=str(counter))


def decrease_value(event):
# TODO make the counter decrease by 1 before updating the text of label1.


# create window
window = Tk()
window.title("Exercise 8")
window.geometry("100x105")

# create widgets
label1 = Label(window, text="0", width=10)
button1 = Button(window, text="Counter", width=10)

# place widgets into window container using the grid layout
label1.grid(row=0, column=0)
button1.grid(row=1, column=0)

# bind widget events to functions
button1.bind("<Button-1>", increase_value)
button1.bind("# TODO insert the input event to bind to", insert the name of the function that decreases the counter)

# open window
window.mainloop()
