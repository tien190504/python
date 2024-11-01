# Adding a menu bar

## Important note for Apple Mac developers
<details>
    <summary>Apple Mac Style Guide</summary>

> ## MacOS Design Theme and Style Guide Requirements
> Apple requires developers to stick to a design theme and style guide that maintains a single user experience across all applications.
>
> MacOS will _not_ warn you if you break the design theme and your widgets will just silently fail to appear.
> 
> We recognise this is a frustrating experience for new macOS GUI developers, so in this lesson we deliberately break the 'menu item on menu bar rule', to help you become aware of the pitfalls of macOS GUI programming.
> 
> ### TL;DR
> - This lesson doesn't work on macOS because macOS enforces a style guide.
> - Complete the lesson to see what macOS does when it doesn't like your code.
> - Learn how to fix it in the next lesson!

</details>

## Your Task
- Build the Tkinter window to make this program work.

## What is this all about?
Menu bar is one of the toolbars which make our programs more usable because it lets us open different windows and properties. It also helps users get a feel for the kind of features our program has. 

As with most of the widgets that we add to our programs, we should create a variable then assign it to the widget. 

In this lesson we have;
1. Created a Menu widget called `menu_bar` and attached it to the `window` container.
2. Then we used the `config()` function to assign `menu_bar` to the window.
3. Finally, we added two commands to the menu;
   1. One runs the function `say_hello`
   2. And the other runs the function `window.quit`.

***
>## TL;DR
>All this Too Long; Didn't Read it, huh?
>1. Use `Menu()` widgets to create menus.

## _Want to Know More?_
- Programming on Mac? Check out the [macOS Design Themes](https://developer.apple.com/design/human-interface-guidelines/macos/overview/themes/) to see what style requirements affect your programs.
