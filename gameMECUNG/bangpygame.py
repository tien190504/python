import heapq
import tkinter as tk
import random
import tkinter.messagebox as messagebox


# Khởi tạo cửa sổ game
window = tk.Tk()
window.geometry('758x755')
window.title("DEMO MÊ CUNG")

# Tạo cửa sổ menu riêng
def open_menu():
    menu_window = tk.Toplevel(window)
    menu_window.title("Menu")
    menu_window.geometry('400x200')

    # Nút New Game
    new_game_button = tk.Button(menu_window, text="New Game", font=("Arial", 14), command=lambda: start_new_game(menu_window))
    new_game_button.pack(pady=10)

    # Nút Continue
    continue_button = tk.Button(menu_window, text="Continue", font=("Arial", 14), command=lambda: continue_game(menu_window))
    continue_button.pack(pady=10)

    # Nút Exit
    exit_button = tk.Button(menu_window, text="Exit", font=("Arial", 14), command=exit_game)
    exit_button.pack(pady=10)

# Bắt đầu trò chơi mới
def start_new_game(menu_window):
    menu_window.destroy()  # Đóng menu
    new_game()  # Bắt đầu trò chơi mới

# Tiếp tục trò chơi cũ
def continue_game(menu_window):
    menu_window.destroy()  # Đóng menu
    window.deiconify()  # Hiển thị lại cửa sổ trò chơi

# Thoát game
def exit_game():
    window.quit()

# Khi nhấn nút New Game, cần reset trò chơi
def new_game():
    global start_pos, end_pos, found_path, clicked, player_pos, visited_path
    # đặt lại các giá trị
    start_pos = None
    end_pos = None
    player_pos = None
    found_path = []
    clicked = 0
    visited_path = []
    generate_maze()
    draw_maze()

# Kích thước mê cung
maze_size = 30
cell_size = 20
wall_margin = 4  # kích thước của tương

# Khởi tạo mê cung với tất cả là tường
maze = [[0 for _ in range(maze_size)] for _ in range(maze_size)]
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

start_pos = None
end_pos = None
player_pos = None
visited_path = []
clicked = 0  # Đếm số lần click để phân biệt điểm bắt đầu và kết thúc
game_won = False

# Tạo khung vẽ
canvas = tk.Canvas(window, width=maze_size * cell_size, height=maze_size * cell_size)
canvas.pack()

# Vẽ mê cung
def draw_maze():
    canvas.delete("all")
    for row in range(maze_size):
        for col in range(maze_size):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            if maze[row][col] == 0:
                canvas.create_rectangle(x1, y1, x2, y2, fill="Black")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            if start_pos == (row, col):
                canvas.create_oval(x1, y1, x2, y2, fill="Blue")
            if end_pos == (row, col):
                canvas.create_oval(x1, y1, x2, y2, fill="Green")
            if player_pos == (row, col):
                canvas.create_oval(x1, y1, x2, y2, fill="Red")

            if (row, col) in visited_path:
                canvas.create_rectangle(x1, y1, x2, y2, fill="LightGreen")
    if player_pos:
        x1 = player_pos[1] * cell_size
        y1 = player_pos[0] * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        canvas.create_oval(x1, y1, x2, y2, fill="Red")

# Tạo mê cung bằng DFS
def generate_maze():
    def dfs(x, y):
        random.shuffle(direction)
        for dx, dy in direction:
            nx, ny = x + 2 * dx, y + 2 * dy
            if (0 <= nx < maze_size) and (0 <= ny < maze_size) and (maze[nx][ny] == 0):
                maze[y + dy][x + dx] = 1
                maze[nx][ny] = 1
                dfs(nx, ny)

    for row in range(maze_size):
        for col in range(maze_size):
            maze[row][col] = 0

    start_x, start_y = random.randint(0, maze_size // 2) * 2, random.randint(0, maze_size // 2) * 2
    maze[start_y][start_x] = 1
    dfs(start_x, start_y)

# Hiển thị menu lúc khởi động
open_menu()

# Ẩn cửa sổ game khi menu đang hiển thị
window.withdraw()

# Khởi tạo mê cung và vẽ nó
generate_maze()
draw_maze()

window.mainloop()
