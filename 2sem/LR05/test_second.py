import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
a, b, n = 2, 3, 10
delta_x = (b - a) / n

# Узлы интерполяции
x_nodes = np.linspace(a, b, n + 1)
y_nodes = np.log(np.tan(x_nodes / np.sqrt(10)))

# Промежуточные точки для вычисления
x_interp = a + delta_x * (np.arange(n) + 0.5)
y_exact = np.log(np.tan(x_interp / np.sqrt(10)))


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

# Вычисление интерполированных значений
y_interp = np.array([lagrange_interpolation(x, x_nodes, y_nodes) for x in x_interp])

# Абсолютная погрешность
abs_errors = np.abs(y_exact - y_interp)

# Относительная погрешность (%)
rel_errors = np.abs((y_exact - y_interp) / y_exact) * 100

# Максимальная погрешность
max_abs_error = np.max(abs_errors)
max_rel_error = np.max(rel_errors)



print("Результаты интерполяции:")
print("j\tx_j\t\tТочное y\tИнтерполированное y\tАбс. погрешность\tОтн. погрешность (%)")
for j in range(n):
    print(f"{j}\t{x_interp[j]:.3f}\t{y_exact[j]:.6f}\t{y_interp[j]:.6f}\t\t{abs_errors[j]:.6f}\t\t{rel_errors[j]:.6f}")

print(f"\nМаксимальная абсолютная погрешность: {max_abs_error:.6f}")
print(f"Максимальная относительная погрешность: {max_rel_error:.6f}%")



plt.figure(figsize=(12, 6))
plt.scatter(x_nodes, y_nodes, color='red', label='Узлы интерполяции', zorder=3)
plt.scatter(x_interp, y_exact, color='green', label='Точные значения', zorder=2)
plt.scatter(x_interp, y_interp, color='blue', label='Интерполированные значения', zorder=1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция многочленом Лагранжа')
plt.legend()
plt.grid(True)
plt.show()