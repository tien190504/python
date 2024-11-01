import random
import numpy as np

# Số lượng thành phố (đỉnh)
V = 10

# Danh sách các đỉnh với tên
cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Ma trận chi phí giữa các thành phố
#         A   B   C  D  E   F   G   H  I  J
graph = [[14, 6,  9, 7, 13, 20, 15, 10, 8, 12],  # A
         [6,  0,  8, 5,  7,  10, 9,  4, 6, 10],  # B
         [9,  8,  0, 6,  5,  10, 11, 6,  7, 8],  # C
         [7,  5,  6, 0,  4,  9,  10, 8,  5, 7],  # D
         [13, 7,  5, 4,  0,  6,  8,  9, 3, 4],   # E
         [20, 10, 10, 9, 6,  0,  4,  8, 6, 9],   # F
         [15, 9,  11, 10, 8, 4,  0,  6, 7, 5],   # G
         [10, 4,  6,  8, 9,  8,  6,  0, 4, 5],   # H
         [8,  6,  7,  5, 3,  6,  7,  4, 0, 9],   # I
         [12, 10, 8,  7, 4,  9,  5,  5, 9, 0]]   # J


# Hàm ánh xạ tên thành phố thành chỉ số trong ma trận chi phí
def city_to_index(city):
    return cities.index(city)

# Hàm ánh xạ chỉ số trong ma trận thành tên thành phố
def index_to_city(index):
    return cities[index]

# Hàm tính tổng chi phí của một hành trình
def calculate_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += graph[city_to_index(route[i])][city_to_index(route[i + 1])]
    cost += graph[city_to_index(route[-1])][city_to_index(route[0])]  # Thêm chi phí quay lại thành phố xuất phát
    return cost

# Khởi tạo quần thể ban đầu (tạo ngẫu nhiên các lộ trình)
def initial_population(pop_size, V):
    population = []
    for _ in range(pop_size):
        route = random.sample(cities, V)  # Tạo một hoán vị ngẫu nhiên của các thành phố (sử dụng tên)
        population.append(route)
    return population

# Hàm chọn lọc theo giải đấu (tournament selection)
def tournament_selection(population, fitness, k=3):
    selected = random.sample(list(enumerate(fitness)), k)  # Chọn ngẫu nhiên k cá thể
    selected.sort(key=lambda x: x[1])  # Sắp xếp dựa trên giá trị fitness
    return population[selected[0][0]]  # Trả về cá thể có fitness tốt nhất

# Hàm lai ghép (crossover) - Ordered Crossover (OX)
def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))  # Chọn ngẫu nhiên hai điểm cắt
    child = [None] * size
    child[start:end] = parent1[start:end]  # Lấy đoạn giữa của cha mẹ 1

    # Điền các giá trị còn lại từ cha mẹ 2 theo thứ tự mà không bị trùng lặp
    pos = end
    for city in parent2:
        if city not in child:
            if pos >= size:
                pos = 0
            child[pos] = city
            pos += 1
    return child

# Hàm đột biến (mutation) - Swap Mutation
def mutate(route, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]  # Hoán đổi hai thành phố ngẫu nhiên
    return route

# Hàm di truyền (genetic algorithm)
def genetic_algorithm(graph, V, pop_size=1000, generations=500, mutation_rate=0.1):
    # Bước 1: Khởi tạo quần thể ban đầu
    population = initial_population(pop_size, V)
    
    # Bước 2: Tính toán fitness cho từng cá thể
    fitness = [calculate_cost(route) for route in population]

    # Bước 3: Tiến hóa qua các thế hệ
    for generation in range(generations):
        new_population = []

        # Tạo ra thế hệ mới
        for _ in range(pop_size):
            # Chọn hai cá thể cha mẹ
            parent1 = tournament_selection(population, fitness)
            parent2 = tournament_selection(population, fitness)

            # Lai ghép cha mẹ để tạo con
            child = crossover(parent1, parent2)

            # Đột biến con
            child = mutate(child, mutation_rate)

            # Thêm con vào quần thể mới
            new_population.append(child)

        # Cập nhật quần thể và tính toán lại fitness
        population = new_population
        fitness = [calculate_cost(route) for route in population]
        
        # In ra thế hệ hiện tại và chi phí tốt nhất
        best_cost = min(fitness)
        best_route = population[fitness.index(best_cost)]
        print(f"Generation {generation+1}: Best cost = {best_cost}, Best route = {best_route}")    
        
    # Trả về hành trình tốt nhất và chi phí nhỏ nhất sau khi hoàn thành quá trình tiến hóa
    best_cost = min(fitness)
    best_route = population[fitness.index(best_cost)]
    return best_route, best_cost

# Chạy thuật toán GA cho bài toán TSP với các thành phố
best_route, best_cost = genetic_algorithm(graph, V)
print(f"Final best route: {best_route}")
print(f"Final best cost: {best_cost}")
