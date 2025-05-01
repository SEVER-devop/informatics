import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
a, b, n = 2, 3, 10
delta_x = (b - a) / n

# Табулирование функции
x = np.linspace(a, b, n + 1)
y = np.log(np.tan(x / np.sqrt(10)))

# Вывод таблицы значений
print("Таблица значений функции:")
print("i\tx_i\t\ty_i")
for i, (xi, yi) in enumerate(zip(x, y)):
    print(f"{i}\t{xi:.3f}\t\t{yi:.6f}")



def least_squares(x, y, degree):
    """Реализация метода наименьших квадратов"""
    n = len(x)
    A = np.zeros((degree + 1, degree + 1))
    B = np.zeros(degree + 1)
    
    # Формирование матрицы системы уравнений
    for i in range(degree + 1):
        for j in range(degree + 1):
            A[i, j] = np.sum(x**(i + j))
        B[i] = np.sum(y * x**i)
    
    # Решение системы методом Гаусса
    coeffs = np.linalg.solve(A, B)
    return coeffs

def polynomial(x, coeffs):
    """Вычисление значения полинома"""
    return sum(c * x**i for i, c in enumerate(coeffs))





# Аппроксимация полиномами 2-5 степени
degrees = [2, 3, 4, 5]
poly_coeffs = {}
poly_values = {}

for degree in degrees:
    coeffs = least_squares(x, y, degree)
    poly_coeffs[degree] = coeffs
    poly_values[degree] = polynomial(x, coeffs)
    
    print(f"\nКоэффициенты полинома {degree}-й степени:")
    for i, c in enumerate(coeffs):
        print(f"a_{i} = {c:.6f}")







def calculate_errors(y_true, y_pred):
    abs_errors = np.abs(y_true - y_pred)
    rel_errors = np.abs((y_true - y_pred) / y_true) * 100
    return abs_errors, rel_errors

# Вычисление погрешностей
errors = {}
for degree in degrees:
    abs_err, rel_err = calculate_errors(y, poly_values[degree])
    errors[degree] = {'absolute': abs_err, 'relative': rel_err}
    
    print(f"\nМаксимальная абсолютная погрешность (степень {degree}): {np.max(abs_err):.6f}")
    print(f"Максимальная относительная погрешность (степень {degree}): {np.max(rel_err):.6f}%")






plt.figure(figsize=(12, 6))
plt.scatter(x, y, color='black', label='Исходная функция', zorder=3)

# Построение графиков аппроксимаций
x_plot = np.linspace(a, b, 100)
for degree in degrees:
    y_plot = polynomial(x_plot, poly_coeffs[degree])
    plt.plot(x_plot, y_plot, label=f'Полином {degree}-й степени')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Аппроксимация функции полиномами')
plt.legend()
plt.grid(True)
plt.show()







# Находим полином с минимальной максимальной погрешностью
best_degree = min(degrees, key=lambda d: np.max(errors[d]['absolute']))
best_error = np.max(errors[best_degree]['absolute'])

print(f"\nНаилучшая аппроксимация: полином {best_degree}-й степени")
print(f"Максимальная абсолютная погрешность: {best_error:.6f}")