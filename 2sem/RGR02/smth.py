import numpy as np
from scipy.optimize import root_scalar

def f(x):
    return x**3 - 3*x**2 + 3

# Интервал поиска
a, b = -10, 10
step = 0.1
tolerance = 1e-6  # Погрешность

roots = []
x_values = np.arange(a, b + step, step)

for i in range(len(x_values) - 1):
    x1, x2 = x_values[i], x_values[i + 1]
    if f(x1) * f(x2) < 0:  # Если функция меняет знак
        result = root_scalar(f, bracket=[x1, x2], method='brentq')
        root = result.root
        # Проверяем, что корень не был добавлен ранее (избегаем дубликатов)
        if not any(abs(root - r) < tolerance for r in roots):
            roots.append(root)

print("Все корни в интервале [{}, {}]:".format(a, b), roots)