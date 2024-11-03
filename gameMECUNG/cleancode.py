import heapq
import tkinter as tk
import random
import tkinter.messagebox as messagebox

# Class MazeGame để tạo và điều khiển game mê cung
class MazeGame:
    def __init__(self, maze_size=30, cell_size=20):
        # Khởi tạo cửa sổ và thiết lập các thuộc tính cơ bản của game
        self.window = tk.Tk()
        self.window.geometry('758x755')
        self.window.title("DEMO MÊ CUNG")

        # Tiêu đề của game
        self.first_label = tk.Label(text="Demo game mê cung", font=("Arial", 20, "bold"))
        self.first_label.pack(side=tk.TOP)

        # Thiết lập kích thước mê cung và kích thước mỗi ô vuông
        self.maze_size = maze_size
        self.cell_size = cell_size

        # Tạo ma trận mê cung
        self.maze = [[0 for _ in range(self.maze_size)] for _ in range(self.maze_size)]
        # Các hướng di chuyển có thể
        self.direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # Các biến khởi tạo điểm bắt đầu, điểm kết thúc, và vị trí người chơi
        self.start_pos = None
        self.end_pos = None
        self.player_pos = None
        self.visited_path = []   # Đường đi người chơi đã đi qua
        self.found_path = []     # Đường tìm được từ thuật toán tìm đường
        self.clicked = 0         # Số lần nhấp chuột để chọn điểm bắt đầu và kết thúc
        self.game_won = False    # Trạng thái chiến thắng của game

        # Tạo canvas để vẽ mê cung
        self.canvas = tk.Canvas(self.window, width=self.maze_size * self.cell_size, height=self.maze_size * self.cell_size)
        self.canvas.pack()

        # Gán sự kiện nhấn chuột và nhấn phím
        self.canvas.bind("<Button-1>", self.click_event)
        self.window.bind("<Key>", self.key_event)

        # Tạo khung nút điều khiển
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(side=tk.TOP)

        # Nút tìm đường
        self.find_button = tk.Button(self.button_frame, text="Find path", command=self.find_path)
        self.find_button.pack(side=tk.LEFT)

        # Nút tạo game mới
        self.new_game_button = tk.Button(self.button_frame, text="New Game", command=self.new_game)
        self.new_game_button.pack(side=tk.LEFT)

        # Nút thoát game
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.on_closing)
        self.exit_button.pack(side=tk.LEFT)
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Tạo mê cung ngẫu nhiên và vẽ mê cung
        self.generate_maze()
        self.draw_maze()
        self.window.mainloop()

    def draw_maze(self):
        # Vẽ lại toàn bộ mê cung
        self.canvas.delete("all")
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                x1, y1 = col * self.cell_size, row * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size

                # Màu sắc của ô: đen là tường, trắng là đường
                color = "Black" if self.maze[row][col] == 0 else "white"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

                # Vẽ điểm bắt đầu, kết thúc, và vị trí người chơi
                if self.start_pos == (row, col):
                    self.canvas.create_oval(x1, y1, x2, y2, fill="Blue")
                if self.end_pos == (row, col):
                    self.canvas.create_oval(x1, y1, x2, y2, fill="Green")
                if self.player_pos == (row, col):
                    self.canvas.create_oval(x1, y1, x2, y2, fill="Red")

                # Đánh dấu đường đi đã đi qua
                if (row, col) in self.visited_path:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="LightGreen")
                    
        if self.player_pos:
            x1 = self.player_pos[1] * self.cell_size
            y1 = self.player_pos[0] * self.cell_size
            x2 = x1 + self.cell_size
            y2 = y1 + self.cell_size
            self.canvas.create_oval(x1, y1, x2, y2, fill="Red")

    def generate_maze(self):
        # Tạo mê cung ngẫu nhiên bằng thuật toán tìm đường theo chiều sâu (DFS)
        def dfs(x, y):
            random.shuffle(self.direction)
            for dx, dy in self.direction:
                nx, ny = x + 2 * dx, y + 2 * dy
                if 0 <= nx < self.maze_size and 0 <= ny < self.maze_size and self.maze[nx][ny] == 0:
                    self.maze[y + dy][x + dx] = 1
                    self.maze[nx][ny] = 1
                    dfs(nx, ny)
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                self.maze[row][col] = 0

        # Chọn điểm ngẫu nhiên để bắt đầu tạo đường
        start_x = random.randint(0, self.maze_size // 2) * 2
        start_y = random.randint(0, self.maze_size // 2) * 2
        self.maze[start_y][start_x] = 1
        dfs(start_x, start_y)

    def heuristic(self, a):
        # Tính khoảng cách ước lượng từ điểm hiện tại tới điểm kết thúc
        return abs(a[0] - self.end_pos[0]) + abs(a[1] - self.end_pos[1])

    def reconstruct_path(self, came_from, current):
        # Tái tạo đường đi từ điểm kết thúc đến điểm bắt đầu
        self.found_path = []
        while current in came_from:
            self.found_path.append(current)
            current = came_from[current]
        self.found_path.reverse()  # Đảo ngược để có đường đi từ bắt đầu đến kết thúc

    def find_path(self):
        # Tìm đường đi từ điểm bắt đầu tới điểm kết thúc bằng thuật toán A*
        if not self.player_pos or not self.end_pos or not self.start_pos:
            messagebox.showinfo("Thông báo", "Hãy chọn điểm bắt đầu và điểm kết thúc")
            return

        open_set = []
        heapq.heappush(open_set, (0, self.player_pos))
        came_from = {}
        g_score = {self.player_pos: 0}
        f_score = {self.player_pos: self.heuristic(self.player_pos)}

        while open_set:
            current = heapq.heappop(open_set)[1]
            if current == self.end_pos:
                self.reconstruct_path(came_from, current)
                self.animate_path()
                return
            for dx, dy in self.direction:
                neighbour = (current[0] + dx, current[1] + dy)
                if 0 <= neighbour[0] < self.maze_size and 0 <= neighbour[1] < self.maze_size and self.maze[neighbour[0]][neighbour[1]] == 1:
                    tentative_g_score = g_score[current] + 1

                    if tentative_g_score < g_score.get(neighbour, float('inf')):
                        came_from[neighbour] = current
                        g_score[neighbour] = tentative_g_score
                        f_score[neighbour] = tentative_g_score + self.heuristic(neighbour)

                        if neighbour not in [i[1] for i in open_set]:
                            heapq.heappush(open_set, (f_score[neighbour], neighbour))
        messagebox.showinfo("Thông báo", "Không tìm thấy đường đi")
        self.reset_position()
        self.draw_maze()

    def reset_position(self):
        # Đặt lại trạng thái của điểm bắt đầu, điểm kết thúc, và vị trí người chơi
        self.start_pos = None
        self.end_pos = None
        self.player_pos = None
        self.clicked = 0

    def new_game(self):
        # Tạo game mới với mê cung mới
        self.start_pos = None
        self.end_pos = None
        self.player_pos = None
        self.found_path = []
        self.clicked = 0
        self.visited_path = []
        self.generate_maze()
        self.draw_maze()

    def click_event(self, event):
        # Xử lý sự kiện nhấn chuột để chọn điểm bắt đầu và kết thúc
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if 0 <= row < self.maze_size and 0 <= col < self.maze_size and self.maze[row][col] == 1:
            if self.clicked == 0:  # Chọn điểm bắt đầu
                self.start_pos = (row, col)
                self.player_pos = (row, col)
                self.clicked += 1
                self.draw_maze()
            elif self.clicked == 1:  # Chọn điểm kết thúc
                if self.start_pos == (row, col):
                    messagebox.showwarning("Lỗi", "Điểm bắt đầu không được bằng điểm kết thúc")
                else:
                    self.end_pos = (row, col)
                    self.clicked += 1
                    self.draw_maze()

    def animate_path(self, step=0):
        # Hiển thị đường đi tìm được bằng cách tô màu từng ô
        if step < len(self.found_path):
            row, col = self.found_path[step]
            if self.end_pos != (row, col):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_oval(x1, y1, x2, y2, fill="Yellow")
            self.window.after(15, self.animate_path, step + 1)

    def move_player(self, dx, dy):
        # Di chuyển người chơi theo hướng nhất định
        if self.player_pos and not self.game_won:
            new_pos = (self.player_pos[0] + dx, self.player_pos[1] + dy)
            if 0 <= new_pos[0] < self.maze_size and 0 <= new_pos[1] < self.maze_size and self.maze[new_pos[0]][new_pos[1]] == 1:
                self.visited_path.append(self.player_pos)
                self.player_pos = new_pos
                self.draw_maze()
                if self.player_pos == self.end_pos:
                    messagebox.showinfo("Thông báo", "Bạn đã chiến thắng!")
                    self.game_won = True

    def key_event(self, event):
        # Xử lý sự kiện bàn phím để di chuyển người chơi
        if not self.game_won:
            if event.keysym == "Up":
                self.move_player(-1, 0)
            elif event.keysym == "Down":
                self.move_player(1, 0)
            elif event.keysym == "Right":
                self.move_player(0, 1)
            elif event.keysym == "Left":
                self.move_player(0, -1)

    def on_closing(self):
        # Xử lý sự kiện đóng cửa sổ
        if messagebox.askokcancel("Thoát", "Bạn có muốn thoát không?"):
            self.window.destroy()

if __name__ == "__main__":
    MazeGame()
