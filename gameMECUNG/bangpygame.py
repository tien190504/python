import pygame
import heapq
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ và mê cung
maze_size = 30
cell_size = 20
wall_margin = 4
window_size = maze_size * cell_size

# Khởi tạo cửa sổ game
window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Maze Game')

# Mê cung và các biến khác
maze = [[0 for _ in range(maze_size)] for _ in range(maze_size)]
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
start_pos = None
end_pos = None
player_pos = None
visited_path = []

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (144, 238, 144)


# Hàm tạo mê cung
def generate_maze():
    def dfs(x, y):
        random.shuffle(direction)
        for dx, dy in direction:
            nx, ny = x + 2 * dx, y + 2 * dy
            if (0 <= nx < maze_size) and (0 <= ny < maze_size) and (maze[ny][nx] == 0):
                maze[y + dy][x + dx] = 1
                maze[ny][nx] = 1
                dfs(nx, ny)

    for row in range(maze_size):
        for col in range(maze_size):
            maze[row][col] = 0

    start_x, start_y = random.randint(0, maze_size // 2) * 2, random.randint(0, maze_size // 2) * 2
    maze[start_y][start_x] = 1
    dfs(start_x, start_y)


# Vẽ mê cung
def draw_maze():
    window.fill(BLACK)
    for row in range(maze_size):
        for col in range(maze_size):
            x1 = col * cell_size
            y1 = row * cell_size
            if maze[row][col] == 0:
                pygame.draw.rect(window, BLACK, (x1, y1, cell_size, cell_size))
            else:
                pygame.draw.rect(window, WHITE, (x1, y1, cell_size, cell_size))
            if start_pos == (row, col):
                pygame.draw.ellipse(window, BLUE, (x1, y1, cell_size, cell_size))
            if end_pos == (row, col):
                pygame.draw.ellipse(window, GREEN, (x1, y1, cell_size, cell_size))
            if player_pos == (row, col):
                pygame.draw.ellipse(window, RED, (x1, y1, cell_size, cell_size))
            if (row, col) in visited_path:
                pygame.draw.rect(window, LIGHT_GREEN, (x1, y1, cell_size, cell_size))


# Vòng lặp game chính
generate_maze()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Xử lý phím bấm
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Di chuyển người chơi
                pass
            elif event.key == pygame.K_DOWN:
                # Di chuyển người chơi
                pass
            # Thêm các xử lý khác

    # Vẽ mê cung và cập nhật màn hình
    draw_maze()
    pygame.display.update()

# Thoát khỏi Pygame
pygame.quit()

