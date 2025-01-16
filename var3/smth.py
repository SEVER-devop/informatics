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
    step_count = 1  # Количество шагов в текущем направлении
    steps_done = 0  # Количество выполненных шагов в текущем "рейсе"

    for i in range(n * n):
        matrix[x][y] = i + 1  # Заполняем случайным числом от 1 до 100

        # Рассчитываем следующую позицию
        next_x = x + directions[current_direction][0]
        next_y = y + directions[current_direction][1]

        # Переходим к следующему шагу
        x, y = next_x, next_y
        steps_done += 1

        # Проверяем, нужно ли менять направление
        if steps_done == step_count:
            # Меняем направление
            current_direction = (current_direction + 1) % 4
            steps_done = 0

            # Увеличиваем количество шагов каждые два направления
            if current_direction % 2 == 0:
                step_count += 1

    return matrix

n = 5
spiral_matrix = create_spiral_matrix(n)

# Выводим матрицу
for row in spiral_matrix:
    print(' '.join(map(str, row)))