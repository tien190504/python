# Radio Buttons, Check and Message boxes
## Your Task
- Import the messagebox module.
- Place the last three radio buttons and labels.
- Create `button1` that runs the `confirm()` function.

## What is this all about?
In this lesson we made a program that:
1. Allows the user to choose one of the colours
2. And requires them to tick the confirmation box
   1. If the user does not tick the confirmation box, we display a warning message
   2. If the confirmation box is ticked the message acknowledges the users colour choice
 

To be able to read the values in radio and check buttons we need to store them in special Tkinter variable types.
```
yes_no_value = IntVar()
colour_choice = StringVar()
```
In this example we store Integer and String in special Tkinter variable types.
```
radio_button5 = Radiobutton(variable=colour_choice, value="Black")
yes_no_checkbutton = Checkbutton(variable=yes_no_value
```
When we configure the widget, we give it the option `variable=` so it knows where to store the users input. 

We can then use `get()` to find out what the user selected.

```
print(colour_choice.get())
```
And we can use `messagebox` to make a popup window to display messages to the user.

|Message Box Types|
|---|
|showinfo|
|showwarning|
|showerror|
|askquestion|
|askokcancel|
|askyesno|
|askretrycancel|

***
>## TL;DR
>All this Too Long; Didn't Read it, huh?
> 
>1. `Radiobutton()` and `Checkbutton()` both store user input in special Tkinter variables, such as `IntVar()` and `StringVar()`.
>2. You can import the `messagebox` module and make popup messages boxes.

## Want to know more?
- To prepare yourself for the final task in this course, try improving on this task.
  - Instead of defining 5 separate checkButtons change the code to use a for loop.

  <details>
    <summary>hint</summary>

    ```
    for index in range(5):
       # code to make and layout one checkButton goes here ...
    ```
  </details> 
