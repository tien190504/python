# Adding a Submenu
Now let’s create some submenus!
## Your Task
- Create a submenu called `save_menu` and attach it to the `file_menu` Menu widget.
- Add two commands to the `save_menu`
  - "Save..."
  - And "Save as..."
## What is this all about?

Much like the previous lesson, but instead of the `add_command()`, we use the `add_cascade()` function to make the menu extend, or "pulldown" from the parent `file_menu`.
 
We also included a separator to improve the usability and aesthetics of our file menu by using the `.add_separator()` function.

***
>## TL;DR
>All this Too Long; Didn’t Read it, huh?
1. Submenus are just menus that are connected to a parent menu instead of the window, e.g., `save_menu = Menu(file_menu)` 
