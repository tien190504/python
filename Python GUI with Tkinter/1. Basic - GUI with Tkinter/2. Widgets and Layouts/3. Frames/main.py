# import modules
from tkinter import *

# create window
window = Tk()
window.title("Python GUI with Tkinter - Frames")

# create widgets
top_frame = Frame(window)
bottom_frame = Frame(window)
top_frame.pack()
bottom_frame.pack()

text1 = Label(top_frame, text="This application demonstrates frame layout")
button1 = Button(bottom_frame, text="Button 1", fg="green")
button2 = Button(bottom_frame, text="Button 2", fg="red")
button3 = # TODO create the final button, adding it to the bottom_frame

# place widgets into window container using the pack layout
text1.pack()
button1# TODO pack the button onto the LEFT side of the frame
button2# TODO pack the button onto the LEFT side of the frame
button3# TODO pack the button onto the LEFT side of the frame

# open window
window.mainloop()
