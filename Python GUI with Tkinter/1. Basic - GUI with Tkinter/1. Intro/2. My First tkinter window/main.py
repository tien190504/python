import # TODO import the tkinter module

window = tkinter.Tk()

# to rename the title of the window
window.title("# TODO personalise your tkinter window")

# pack is used to organize the text window so that it packs the entire window
label = tkinter.Label(window, text="Hello World!")
label.pack()

window.mainloop()
