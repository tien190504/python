# import modules
from tkinter import *


# define all functions
def clicked():
    text = entry_text.get()
    print("Hello,", text + "! How are you?")


# create window
window = Tk()
window.title("Clicking application")
window.geometry("300x350")

# create widgets
text1 = # TODO create a label and add it to the window
button1 = # TODO Create a button that used  command=clicked
entry_text = Entry(window)

# pack widgets into window container
text1.pack()
button1.pack()
entry_text.pack()

# open window
window.mainloop()
