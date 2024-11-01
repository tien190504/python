# Data "Entry" Widget

## Your Task
Create an application that takes the users name and prints out “Hello, {name}! How are you?” (where {name} is replaced with the name the user provided) in the run window.

1. Create the window with the `Button` and `Label` widget.
2. Use the command argument `command=...` when making your button as in the previous lesson.

## What is this all about?
The `Entry()` widget is the `input()` of the Tkinter GUI world. It allows users to enter data into the GUI, which your program can access use with the `.get()` function. 

***
>## TL;DR
>All this Too Long; Didn’t Read it, huh?
>1. you can use `.get()` to read the data the user typed into an `Entry()` text box.

## _Want to Know More?_
- Try adding a second `Entry` widget that accepts a password.
  - You can hide a password with asterisks by using the `show="*"` configuration option on your `Entry()` widget.
  - Check out the [Tk documentation on the Entry widgets show command](https://tcl.tk/man/tcl8.6/TkCmd/entry.htm#M10) for more information.
