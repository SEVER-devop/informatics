# with open('data.txt', 'w+') as f:
#     f.write("Hello world")

import numpy as np
import random

def create_spiral_matrix(n):
    # Создаем пустую матрицу n x n
    matrix = np.zeros((n, n), dtype=int)

    # Направления для спирали (право, вниз, лево, вверх)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = n // 2, n // 2  # Начальная позиция (центр матрицы)
    current_direction = 0  # Начинаем с направления "право"
    
    # Заполняем матрицу по спирали
    for i in range(n * n):
        matrix[x][y] = i  + 1  # Заполняем случайным числом от 1 до 100
        # Рассчитываем следующую позицию
        next_x = x + directions[current_direction][0]
        next_y = y + directions[current_direction][1]
        
        # Проверяем, нужно ли менять направление
        if (0 <= next_x < n) and (0 <= next_y < n) and (matrix[next_x][next_y] == 0):
            x, y = next_x, next_y
        else:
            # Меняем направление
            current_direction = (current_direction + 1) % 4
            x += directions[current_direction][0]
            y += directions[current_direction][1]

    return matrix

n = 6
spiral_matrix = create_spiral_matrix(n)

# Выводим матрицу
for i in spiral_matrix:
    print(i)