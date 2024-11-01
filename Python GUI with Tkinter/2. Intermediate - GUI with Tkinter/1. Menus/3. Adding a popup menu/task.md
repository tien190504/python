# Adding a Popup Menu

## Your Task
- Bind the windows input event for the right mouse click to the function `popup_menu_event`.
- Create two commands in the popup menu:
  - One called "Copy"
  - And one called "Paste"

## What is this all about?
A popup menu is a menu which is displayed when you click the right mouse button on some widget. 
In this lesson we made a menu popup when the user clicks the right mouse button on the window.

`popup_menu = Menu(window)`

We then defined a function to display the popup menu wherever the mouse was clicked.
```
def popup_menu_event(event):
    # find the x and y positions where the user clicked the right mouse button
    x_position_of_click = event.x_root
    y_position_of_click = event.y_root
    # post/place the pop menu where the user clicked.
    popup_menu.post(x_position_of_click, y_position_of_click)
```

### Bind Events
When we bind a function to an input event, the function receives an `event` variable every time it is called. 

This variable stores all information about the event. For example, the `event.x_root` and `event.y_root` hold the x and y coordinates of where the mouse was clicked, and we use this to place (with `post()`) the popup menu under the mouse cursor.

***
>## TL;DR
>All this Too Long; Didn't Read it, huh?
>1. Event variable holds lots of info about the input event.
>2. `post(x, y)` places the popup menu at the window coordinates (x,y)
>3. Popup menus are menus that are not stuck in one place, and just 'pop up' when an event happens.
