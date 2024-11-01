# My First Tkinter Window
## Your Task
1. Finish the code to create a simple window which displays the text "Hello World!".
 
## What is this all about?
This is the smallest example of a Tkinter app that creates a window. 

### Here's how it works
1. We import the module Tkinter `import tkinter`
2. We start the window manager with the `tkinter.Tk()` method and assign it to the variable `window`. 
   1. This creates a blank window with close, maximize and minimize buttons.
3. We name the title of the window `window.title("some text you chose")`. 
4. We add a Label to the window, so we can display text `Label(text="Hello World!")`. 
   1. We `pack()` the widget into the window. 
5. Finally, we call `mainloop()` to display the window until you manually close it.

***
>## TL;DR
>All this Too Long; Didn't Read it, huh?
>- Importing the Tkinter module means you can use the Tkinter commands.
>  - Make a window `window = tinter.Tk()`
>  - Make a label `label = Label()`
>  - Pack the label into the window `label.pack()`
  
## _Want to Know More?_
- Use the following resources as study aids for this course. 
  - [Python docs on Tkinker](https://docs.python.org/3/library/tk.html)
  - [Tk Documentation](https://tcl.tk/man/tcl8.6/TkCmd/contents.htm)
