import tkinter
window = tkinter.Tk()
window.title("Hangman")
window.geometry("500x500")
window.minsize(width=375, height=567)

#Lable
my_lable = tkinter.Label(text="Hangman", font=("Arial", 24, "bold"), )
my_lable.pack(side=tkinter.TOP)


window.mainloop()