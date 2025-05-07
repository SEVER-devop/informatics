import numpy as np
import matplotlib.pyplot as plt

# Определяем параметры задачи
h = 0.1  # шаг
x0 = 0.0  # начальная точка
xn = 1.0  # конечная точка
y0 = 4.0  # y(0)
y_prime0 = 1.0  # y'(0)

# Функция, представляющая ОДУ второго порядка y'' = f(x, y, y')
def f(x, y, y_prime):
    return y + 2*np.exp(x) - x**2

# Точное решение
def exact_solution(x):
    return (1 + x)*np.exp(x) + np.exp(-x) + x**2 + 2

# Метод Эйлера для ОДУ второго порядка
def euler_method():
    x = np.arange(x0, xn + h, h)
    y = np.zeros_like(x)
    y_prime = np.zeros_like(x)
    
    y[0] = y0
    y_prime[0] = y_prime0
    
    for i in range(1, len(x)):
        y_prime[i] = y_prime[i-1] + h * f(x[i-1], y[i-1], y_prime[i-1])
        y[i] = y[i-1] + h * y_prime[i-1]
    
    return x, y

# Метод Рунге-Кутты 4-го порядка для ОДУ второго порядка
def runge_kutta_4():
    x = np.arange(x0, xn + h, h)
    y = np.zeros_like(x)
    y_prime = np.zeros_like(x)
    
    y[0] = y0
    y_prime[0] = y_prime0
    
    for i in range(1, len(x)):
        # Преобразуем ОДУ второго порядка в систему двух ОДУ первого порядка
        def system(Y, x_val):
            return np.array([Y[1], f(x_val, Y[0], Y[1])])
        
        Y = np.array([y[i-1], y_prime[i-1]])
        
        k1 = h * system(Y, x[i-1])
        k2 = h * system(Y + 0.5*k1, x[i-1] + 0.5*h)
        k3 = h * system(Y + 0.5*k2, x[i-1] + 0.5*h)
        k4 = h * system(Y + k3, x[i-1] + h)
        
        Y_new = Y + (k1 + 2*k2 + 2*k3 + k4) / 6
        
        y[i] = Y_new[0]
        y_prime[i] = Y_new[1]
    
    return x, y

# Вычисление решений
x_euler, y_euler = euler_method()
x_rk, y_rk = runge_kutta_4()

# Точное решение
x_exact = np.linspace(x0, xn, 100)
y_exact = exact_solution(x_exact)

# Вывод таблицы результатов
print(" x\t Эйлер\t Рунге-Кутта 4\t Точное решение")
print("----------------------------------------------")
for i in range(len(x_euler)):
    exact = exact_solution(x_euler[i])
    print(f"{x_euler[i]:.1f}\t{y_euler[i]:.6f}\t{y_rk[i]:.6f}\t{exact:.6f}")