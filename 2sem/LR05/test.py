import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Исходные данные
a, b, n = 2, 3, 10
delta_x = (b - a) / n
x = np.linspace(a, b, n + 1)  # Массив x_i (11 точек)
y = np.log(np.tan(x / np.sqrt(10)))  # Массив y_i

# Вывод таблицы значений
print("Таблица значений функции:")
print("i\tx_i\t\ty_i")
for i, (xi, yi) in enumerate(zip(x, y)):
    print(f"{i}\t{xi:.3f}\t\t{yi:.6f}")


# Функции-полиномы для аппроксимации
def poly2(x, a0, a1, a2):
    return a0 + a1 * x + a2 * x**2

def poly3(x, a0, a1, a2, a3):
    return a0 + a1 * x + a2 * x**2 + a3 * x**3

def poly4(x, a0, a1, a2, a3, a4):
    return a0 + a1 * x + a2 * x**2 + a3 * x**3 + a4 * x**4

def poly5(x, a0, a1, a2, a3, a4, a5):
    return a0 + a1 * x + a2 * x**2 + a3 * x**3 + a4 * x**4 + a5 * x**5

# Аппроксимация для каждой степени
popt2, _ = curve_fit(poly2, x, y)
popt3, _ = curve_fit(poly3, x, y)
popt4, _ = curve_fit(poly4, x, y)
popt5, _ = curve_fit(poly5, x, y)

# Вычисление аппроксимированных значений
y_poly2 = poly2(x, *popt2)
y_poly3 = poly3(x, *popt3)
y_poly4 = poly4(x, *popt4)
y_poly5 = poly5(x, *popt5)


# Вычисление абсолютной и относительной погрешностей
def calculate_errors(y_true, y_pred):
    abs_errors = np.abs(y_true - y_pred)
    rel_errors = np.abs((y_true - y_pred) / y_true) * 100
    return abs_errors, rel_errors

abs_errors2, rel_errors2 = calculate_errors(y, y_poly2)
abs_errors3, rel_errors3 = calculate_errors(y, y_poly3)
abs_errors4, rel_errors4 = calculate_errors(y, y_poly4)
abs_errors5, rel_errors5 = calculate_errors(y, y_poly5)

# Максимальные погрешности
max_abs_errors = {
    "Poly2": np.max(abs_errors2),
    "Poly3": np.max(abs_errors3),
    "Poly4": np.max(abs_errors4),
    "Poly5": np.max(abs_errors5)
}

print("\nМаксимальные абсолютные погрешности:")
for degree, error in max_abs_errors.items():
    print(f"{degree}: {error:.6f}")


# Графики исходной функции и аппроксимаций
plt.figure(figsize=(12, 6))
plt.scatter(x, y, color='black', label='Исходная функция')
plt.plot(x, y_poly2, label='Полином 2-й степени')
plt.plot(x, y_poly3, label='Полином 3-й степени')
plt.plot(x, y_poly4, label='Полином 4-й степени')
plt.plot(x, y_poly5, label='Полином 5-й степени')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.title('Аппроксимация функции полиномами')
plt.show()


# Выбор полинома с минимальной максимальной погрешностью
best_degree = min(max_abs_errors, key=max_abs_errors.get)
print(f"\nНаилучшая аппроксимация: {best_degree} (максимальная погрешность = {max_abs_errors[best_degree]:.6f})")