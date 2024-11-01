# import modules
from tkinter import *

# define variables with global scope
counter = 0


# define all functions
def increase_value(event):
    global counter
    counter = counter + 1
    label1.config(text=str(counter))


# create window
window = Tk()
window.title("Python GUI with tkinter binding events")
window.geometry("100x105")

# create widgets
label1 = Label(window, text="0", width=10)
button1 = Button(window, text="Counter", width=10)

# place widgets into window container using the grid layout
label1.grid(row=0, column=0)
button1.grid(row=1, column=0)

# bind widget events to functions
button1.bind("# TODO enter the name of the input event you want the button to bind to", increase_value)

# open window
window.mainloop()
