import heapq
import tkinter as tk
import random
import tkinter.messagebox as messagebox



# Khởi tạo cửa sổ game
window = tk.Tk()
window.geometry('758x755')
window.title("DEMO MÊ CUNG")
first_label = tk.Label(text="Demo game mê cung", font=("Arial", 20, "bold"))
first_label.pack(side=tk.TOP)

# Kích thước mê cung
maze_size = 30
cell_size = 20
wall_margin = 4 #kích thước của tương

# Khởi tạo mê cung với tất cả là tường
maze = [[0 for _ in range(maze_size)] for _ in range(maze_size)]
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

start_pos: None = None
end_pos: None = None
player_pos: None = None
visited_path = []
# found_path = []
clicked = 0  # Đếm số lần click để phân biệt điểm bắt đầu và kết thúc

# Tạo khung vẽ
canvas = tk.Canvas(window, width = maze_size * cell_size, height = maze_size * cell_size)
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



# Hàm heuristic sử dụng khoảng cách Manhattan
def heuristic1(a):
    return abs(a[0] - end_pos[0]) + abs(a[1] - end_pos[1])

# Hàm tái tạo đường đi từ điểm bắt đầu đến điểm kết thúc
def reconstruct_path(came_from, current):
    global found_path
    found_path = []
    while current in came_from:
        found_path.append(current)
        current = came_from[current]
    found_path.reverse()  # Đảo ngược để có đường đi từ bắt đầu đến kết thúc

# Hàm tìm đường đi trong mê cung vào nút find path
def find_path():
    global found_path, clicked, player_pos,start_pos, end_pos  # Đảm bảo sử dụng biến toàn cục
    if not player_pos or not end_pos:
        messagebox.showinfo("Thông báo", "Hãy chọn điểm bắt đầu và điểm kết thúc")
        return

    open_set = []
    heapq.heappush(open_set, (0, player_pos))  # Chi phí ước lượng, tọa độ
    came_from = {}  # Lưu trữ đường đi từ ô cha đến ô con
    g_score = {player_pos: 0}
    f_score = {player_pos: heuristic1(start_pos)}  # Chi phí ước lượng từ điểm bắt đầu đến điểm kết thúc

    while open_set:
        current = heapq.heappop(open_set)[1]  # Lấy ô có chi phí thấp nhất

        if current == end_pos:  # Nếu đã đến điểm kết thúc
            reconstruct_path(came_from, current)  # Gọi hàm để tái tạo đường đi
            animation_path()  # Bắt đầu hiệu ứng hoạt hình cho đường đi
            return

        for dx, dy in direction:
            neighbour = (current[0] + dx, current[1] + dy)
            if 0 <= neighbour[0] < maze_size and 0 <= neighbour[1] < maze_size and maze[neighbour[0]][neighbour[1]] == 1:
                tentative_g_score = g_score[current] + 1  # Giả sử chi phí giữa hai ô là 1

                if tentative_g_score < g_score.get(neighbour, float('inf')):
                    came_from[neighbour] = current
                    g_score[neighbour] = tentative_g_score
                    f_score[neighbour] = tentative_g_score + heuristic1(neighbour)

                    # Chỉ thêm vào open_set nếu chưa có
                    if neighbour not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbour], neighbour))
    messagebox.showinfo("Thông báo", "Không tìm thấy đường đi")
    reset_position()
    draw_maze()

def reset_position():
    global start_pos, end_pos, player_pos, clicked
    player_pos = None
    start_pos = None
    end_pos = None
    clicked = 0
#hàm nút new game
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
# Hàm xử lý sự kiện khi nhấp chuột để chọn điểm bắt đầu và kết thúc
def click_event(event):
    global start_pos, end_pos, clicked, player_pos
    col = event.x // cell_size
    row = event.y // cell_size

    if 0 <= row < maze_size and 0 <= col < maze_size:  # Kiểm tra tọa độ hợp lệ
        if maze[row][col] == 1:  # Chỉ cho phép chọn điểm trên đường
            if clicked == 0:  # Chọn điểm bắt đầu
                start_pos = (row, col)
                player_pos = (row, col) #Đặt điểm bắt đầu của người chơi tại điểm bắt đầu
                clicked += 1
                draw_maze()
            elif clicked == 1:  # Chọn điểm kết thúc
                if start_pos == (row, col):
                    messagebox.showwarning("Lỗi", "Điểm bắt đầu không được bằng điểm kết thúc")
                else:
                    end_pos = (row, col)
                    clicked += 1
                    draw_maze()
    # else:
    #     messagebox.showwarning("Tọa độ không thuộc mê cung")

# Tạo sự kiện click để chọn vị trí
canvas.bind("<Button-1>", click_event)

# Hàm tạo hiệu ứng
def animation_path(step=0):
    if step < len(found_path):
        row, col = found_path[step]
        if end_pos != (row, col):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            canvas.create_oval(x1, y1, x2, y2, fill="Yellow")
        window.after(15, animation_path, step + 1)  # Điều chỉnh thời gian cho hiệu ứng

#Hàm di chuyển người chơi
def move_player(dx, dy):
    global player_pos
    if player_pos:
        new_pos = (player_pos[0] + dx, player_pos[1] + dy)
        if 0 <= new_pos[0] < maze_size and 0 <= new_pos[1] < maze_size and maze[new_pos[0]][new_pos[1]] == 1:
            visited_path.append(player_pos)
            player_pos = new_pos
            draw_maze()
            if player_pos == end_pos:
                messagebox.showinfo("Chúc mừng!", "Bạn đã đến đích!")

#Hàm xử lý phím
def key_event(event):
    if event.keysym == "Up":
        move_player(-1, 0)
    elif event.keysym == "Down":
        move_player(1, 0)
    elif event.keysym == "Left":
        move_player(0, -1)
    elif event.keysym == "Right":
        move_player(0, 1)
    if event.state & 0x0004 and event.keysym == "f":
        find_path()
#Tạo button để chứa các nút
button_frame = tk.Frame(window)
button_frame.pack(side=tk.TOP)

#liên kết sự kiện move player
window.bind("<Key>", key_event)
# Tạo nút để tìm đường đi
find_button = tk.Button(button_frame, text="Find path", command=find_path)
find_button.pack(side=tk.LEFT)

#Tạo nút new game để đổi mới trò chơi
new_game_buttoon = tk.Button(button_frame, text="New Game", command=new_game)
new_game_buttoon.pack(side=tk.LEFT)

#Hàm nút thoát
exit_button = tk.Button(button_frame, text="Exit", command=exit)
exit_button.pack(side=tk.LEFT)

# Khởi tạo mê cung và vẽ nó
generate_maze()
draw_maze()

window.mainloop()

