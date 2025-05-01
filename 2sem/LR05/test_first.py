import numpy as np
import matplotlib.pyplot as plt

# Исходные данные для варианта 3
a = 2
b = 3
n = 10
x_values = np.linspace(a, b, n)
y_values = np.log(np.tan(x_values / np.sqrt(10)))

# Функция для аппроксимации полиномом
def polynomial(x, coefficients):
    return sum(coef * x**i for i, coef in enumerate(coefficients))

# Метод Гаусса для решения СЛАУ
def gauss_elimination(A, B):
    n = len(B)
    
    # Прямой ход метода Гаусса
    for k in range(n):
        # Поиск ведущего элемента
        max_row = k
        for i in range(k + 1, n):
            if abs(A[i, k]) > abs(A[max_row, k]):
                max_row = i
        # Перестановка строк
        A[[k, max_row]] = A[[max_row, k]]
        B[[k, max_row]] = B[[max_row, k]]
        
        # Нормализация текущей строки
        pivot = A[k, k]
        if pivot == 0:
            raise ValueError("Матрица системы вырождена")
        A[k] /= pivot
        B[k] /= pivot
        
        # Исключение переменной из остальных строк
        for i in range(n):
            if i != k and A[i, k] != 0:
                factor = A[i, k]
                A[i] -= A[k] * factor
                B[i] -= B[k] * factor
    
    return B

# Метод наименьших квадратов с ручным методом Гаусса
def least_squares_fit(degree, x, y):
    # Создаем матрицу для системы уравнений
    A = np.zeros((degree + 1, degree + 1))
    B = np.zeros(degree + 1)
    
    for i in range(degree + 1):
        for j in range(degree + 1):
            A[i, j] = np.sum(x**(i + j))
        B[i] = np.sum(y * x**i)
    
    # Решаем систему методом Гаусса
    coefficients = gauss_elimination(A, B)
    return coefficients

# Вычисление значений аппроксимирующего полинома
def evaluate_polynomial(coefficients, x):
    return sum(coef * x**i for i, coef in enumerate(coefficients))

# Вычисление погрешностей
def calculate_errors(y_true, y_pred):
    absolute_errors = np.abs(y_true - y_pred)
    relative_errors = absolute_errors / np.abs(y_true)
    return absolute_errors, relative_errors

# Аппроксимация полиномами
degrees = [2, 3, 4, 5]
results = {}

for degree in degrees:
    coefficients = least_squares_fit(degree, x_values, y_values)
    y_pred = evaluate_polynomial(coefficients, x_values)
    abs_errors, rel_errors = calculate_errors(y_values, y_pred)
    
    results[degree] = {
        'coefficients': coefficients,
        'y_pred': y_pred,
        'abs_errors': abs_errors,
        'rel_errors': rel_errors,
        'max_abs_error': np.max(abs_errors),
        'max_rel_error': np.max(rel_errors)
    }

# Вывод результатов
for degree in degrees:
    print(f"Полином {degree}-й степени:")
    print(f"Коэффициенты: {results[degree]['coefficients']}")
    print(f"Максимальная абсолютная погрешность: {results[degree]['max_abs_error']}")
    print(f"Максимальная относительная погрешность: {results[degree]['max_rel_error']}")
    print()

# Построение графиков
plt.figure(figsize=(12, 8))
plt.scatter(x_values, y_values, label='Исходные данные', color='black')

x_plot = np.linspace(a, b, 100)
for degree in degrees:
    y_plot = evaluate_polynomial(results[degree]['coefficients'], x_plot)
    plt.plot(x_values, y_values, label=f'Полином {degree}-й степени')

plt.title('Аппроксимация функции полиномами')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

# Выбор наилучшего полинома
best_degree = min(degrees, key=lambda d: results[d]['max_abs_error'])
print(f"Наилучшая аппроксимация: полином {best_degree}-й степени")