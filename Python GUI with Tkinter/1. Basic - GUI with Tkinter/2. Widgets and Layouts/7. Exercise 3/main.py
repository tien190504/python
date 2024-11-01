from tkinter import *

window = Tk()
window.title("Exercise 3")

top_frame = Frame(window)
# TODO declare/create your frames here
top_frame.pack()
# TODO pack your frames here
text1 = Label(top_frame, text="This application demonstrates frame layout")
# TODO create your second Label here
# TODO create your 4 buttons here

text1.pack()
# TODO don't forget to pack all your new widgets!

window.mainloop()
