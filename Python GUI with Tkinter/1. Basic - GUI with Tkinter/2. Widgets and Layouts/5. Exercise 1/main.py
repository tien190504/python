# import modules
from tkinter import *

# create window
window = Tk()
window.title("Exercise 1")

# create widgets
top_frame = Frame(window)
middle_frame = Frame(window)
bottom_frame = Frame(window)

text1 = Label(top_frame, text="This application demonstrates frame layout")
# TODO Create and frame your 4 buttons here

# place widgets into window container using the pack layout
top_frame.pack()
middle_frame.pack()
bottom_frame.pack()
text1.pack()
# TODO Pack your 4 buttons into the window

# open window
window.mainloop()
