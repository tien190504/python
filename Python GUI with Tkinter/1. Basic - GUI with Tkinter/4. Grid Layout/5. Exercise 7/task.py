# import modules
from tkinter import *


# define all functions
def login():
    message_label# TODO update the text config of the message_label


def clear_form():
    # get() len() of username entry text.
    username_text = # TODO get the value in the username_entry widget
    username_length = len(username_text)
    # if username_length > 0 then delete() text from entry form up to length
    if username_length > 0:
        username_entry.delete(0, username_length)

    # get() len() of password entry text.
    password_text = password_entry.get()
    password_length = len(password_text)
    # if password_length > 0 then delete() text from entry form up to length
    # TODO clear the password_entry widget


def exit_program():
    print("closing ...")
    # terminate/finish this python program and return code 0; meaning no errors
    exit(0)


# create window
window = Tk()
window.title("Exercise 7")
window.geometry("300x105")

# create widgets
username_label = Label(window, text="Username:")
password_label = Label(window, text="Password:")
message_label = Label(window, text="Welcome")
username_entry = Entry(window)
password_entry = Entry(window)
submit_button = Button(window, text="Submit", command=# TODO config the button to run the login function)
clear_button = Button(window, text="Clear", command=# TODO config the button to run the clear_form function)
close_button = Button(window, text="Close", command=# TODO config the button to run the exit_program function)

# place widgets into window container using the grid layout
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1, columnspan=2)
# TODO layout the widgets using a grid

# open window
window.mainloop()
