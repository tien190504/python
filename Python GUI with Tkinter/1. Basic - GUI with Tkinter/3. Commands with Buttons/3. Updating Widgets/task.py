# import modules
from tkinter import *


# define all functions
def clicked():
    text = entry_text.get()
    display_text = "Hello," + text + "! How are you?"
    text1# TODO Use the config function to change the text of the text1 Label widget.
    button1.config(state=DISABLED)

# create window
window = Tk()
window.title("Clicking application")
window.geometry("300x350")

# create widgets
text1 = Label(window, text="Enter your name here")
button1 = Button(window, text="Click me!", command=clicked)
entry_text = Entry(window)

# pack widgets into window container
text1.pack()
button1.pack()
entry_text.pack()

# open window
window.mainloop()
