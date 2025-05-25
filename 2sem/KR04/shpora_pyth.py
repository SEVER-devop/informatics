import numpy as np
import matplotlib.pyplot as plt



def f6(x):
    return (x - 3) / (x**2 + 2)


a = -1
b = 4
n = 5
degrees = [2, 3, 4, 5]

x_data = np.linspace(a, b, n + 1)
y_data = np.array([f6(x) for x in x_data])

x_fine_func = np.arange(a, b + 0.01, 0.01)
y_fine_func = f6(x_fine_func)


def gaussian_elimination(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)

    for i in range(n):
        factor = A[i, i]
        for j in range(i, n):
            A[i, j] /= factor
        b[i] /= factor

        for k in range(i + 1, n):
            factor = A[k, i]
            for j in range(i, n):
                A[k, j] -= factor * A[i, j]
            b[k] -= factor * b[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i, j] * x[j]

    return x

def least_squares_approximation(x_data, y_data, degree):
    A = np.zeros((degree + 1, degree + 1))
    b = np.zeros(degree + 1)

    for i in range(degree + 1):
        for j in range(degree + 1):
            A[i, j] = np.sum(x_data**(i + j))
        b[i] = np.sum(y_data * x_data**i)

    coefficients = gaussian_elimination(A, b)
    return coefficients

def evaluate_polynomial(x, coefficients):
    y = 0
    for i, coef in enumerate(coefficients):
        y += coef * (x**i)
    return y

def calculate_errors(x_data, y_data, coefficients):
    y_approx = np.array([evaluate_polynomial(x, coefficients) for x in x_data])
    return y_approx


print('*' * 100)
for degree in degrees:
    print(f'Полином степени {degree}')
    coefficients = least_squares_approximation(x_data, y_data, degree)
    print(f'{coefficients} - Коэффициенты методом МНК')
    print(f'{np.polyfit(x_data, y_data, degree)[::-1]} - Проверка методом np.polyfit (перевернуто)')
    y_approx = calculate_errors(x_data, y_data, coefficients)
    print(f'{y_approx} - Значения аппроксимации в узлах')
    print('*' * 100)


plt.figure(figsize=(12, 10))
for i, degree in enumerate(degrees, 1):
    plt.subplot(2, 2, i)
    plt.plot(x_fine_func, y_fine_func, color='purple', label='Исходная функция f6(x)')
    coefficients = least_squares_approximation(x_data, y_data, degree)
    x_fine = np.linspace(a, b, 500)
    y_approx = evaluate_polynomial(x_fine, coefficients)
    plt.plot(x_fine, y_approx, color='green', label=f'Аппроксимация, степень {degree}')
    plt.title(f'Аппроксимация МНК, степень {degree}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()