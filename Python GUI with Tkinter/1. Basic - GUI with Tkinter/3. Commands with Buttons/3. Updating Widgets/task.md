# Updating Widgets

## Your Task
1. Inside the clicked function use `config()` to modify the `text1` label.

```
    text = entry_text.get()
    display_text = "Hello," + text + "! How are you?"
    text1.config(text=display_text)
```

## What is this all about?
The `config()` function is the `print()` of the Tkinter GUI world. It allows your code to display/change the text in your Tkinter widgets.

***
>## TL;DR
>All this Too Long; Didn't Read it, huh?
1. You can use `config()` to update `Labels` and print text onto GUI widgets.

## _Want to Know More?_
- Does the `config()` function work on other widgets as well? Try disabling `button1` inside the function with `.config(state=DISABLED)`, so the button can only be pressed once.
    - What else can you change to provide visual feedback to the user?
