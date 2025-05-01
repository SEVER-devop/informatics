import numpy as np
import matplotlib.pyplot as plt

# Исходные данные из варианта 3
a = 2
b = 3
n = 10
x_values = np.linspace(a, b, n)
y_values = np.log(np.tan(x_values / np.sqrt(10)))

# Функция для вычисления интерполяционного многочлена Лагранжа
def lagrange_interpolation(x, x_nodes, y_nodes):
    n = len(x_nodes)
    result = 0.0
    for i in range(n):
        term = y_nodes[i]
        for j in range(n):
            if i != j:
                term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result

# Вычисление промежуточных точек x_j = a + Δx*(j + 0.5), j = 0, 1, ..., n-1
delta_x = (b - a) / n
x_intermediate = np.array([a + delta_x * (j + 0.5) for j in range(n)])
y_exact = np.log(np.tan(x_intermediate / np.sqrt(10)))  # Точные значения
y_lagrange = np.array([lagrange_interpolation(x, x_values, y_values) for x in x_intermediate])  # Значения по Лагранжу

# Вычисление погрешностей
absolute_errors = np.abs(y_exact - y_lagrange)
relative_errors = absolute_errors / np.abs(y_exact)

# Вывод результатов
print("Промежуточные точки (x_j):", x_intermediate)
print("\nТочные значения (y_exact):", y_exact)
print("\nЗначения по Лагранжу (y_lagrange):", y_lagrange)
print("\nАбсолютные погрешности:", absolute_errors)
print("\nОтносительные погрешности:", relative_errors)
