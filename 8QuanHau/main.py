# Chuyển đổi vị trí ví dụ "C1" thành tọa độ (hàng, cột)
def parse_position(position):
    column = ord(position[0].upper()) - ord('A')  # Cột A-H sẽ tương ứng với 0-7
    row = int(position[1]) - 1  # Hàng 1-8 sẽ tương ứng với 0-7
    return row, column


# Kiểm tra xem có thể đặt quân hậu tại vị trí (row, col) mà không bị ăn hay không
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


# Thuật toán giải bài toán 8 quân hậu bằng backtracking
def solve_n_queens(board, row, solutions):
    if row == len(board):
        solutions.append(board[:])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(board, row + 1, solutions)
            board[row] = -1  # Backtrack


# Tìm tất cả các lời giải cho bài toán 8 quân hậu, với một quân đã cố định
def find_solutions_with_fixed_queen(fixed_position):
    fixed_row, fixed_col = parse_position(fixed_position)

    board = [-1] * 8  # Khởi tạo bàn cờ 8x8, mỗi hàng có -1 tức là chưa đặt quân hậu
    board[fixed_row] = fixed_col  # Đặt quân hậu cố định

    solutions = []
    solve_n_queens(board, 0, solutions)

    # Lọc ra những lời giải có quân hậu cố định tại vị trí mong muốn
    valid_solutions = [sol for sol in solutions if sol[fixed_row] == fixed_col]

    return valid_solutions


# In bàn cờ từ lời giải
def print_board(solution):
    for row in range(8):
        line = ['.'] * 8
        line[solution[row]] = 'Q'
        print(' '.join(line))
    print()


# Ví dụ sử dụng với đầu vào là "C1"
position = "B1"
solutions = find_solutions_with_fixed_queen(position)

# In tất cả các lời giải tìm được
if solutions:
    print(f"Tìm thấy {len(solutions)} cách đặt 8 quân hậu với quân hậu tại {position}:")
    for solution in solutions:
        print_board(solution)
else:
    print(f"Không tìm thấy lời giải nào với quân hậu tại {position}.")
