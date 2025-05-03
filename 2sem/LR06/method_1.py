import math
import matplotlib.pyplot as plt

# Определение функции и точного решения
def f(x, y):
    return -y * math.cos(x) + math.exp(-math.sin(x))

def exact_solution(x):
    return (x + 1) * math.exp(-math.sin(x))

# Параметры задачи
x0 = 0
y0 = 1
x_end = 1
h = 0.1
n = int((x_end - x0) / h) + 1

# Метод Эйлера
def euler_method():
    x = [x0 + i * h for i in range(n)]
    y = [0.0] * n
    y[0] = y0
    
    for i in range(n-1):
        y[i+1] = y[i] + h * f(x[i], y[i])
    
    return x, y

# Метод Рунге-Кутта 4-го порядка
def runge_kutta4():
    x = [x0 + i * h for i in range(n)]
    y = [0.0] * n
    y[0] = y0
    
    for i in range(n-1):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h/2, y[i] + k1/2)
        k3 = h * f(x[i] + h/2, y[i] + k2/2)
        k4 = h * f(x[i] + h, y[i] + k3)
        
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return x, y

# Метод Адамса (использует первые 4 точки из метода Рунге-Кутта)
def adams_method():
    x = [x0 + i * h for i in range(n)]
    y = [0.0] * n
    
    # Получаем первые 4 точки методом Рунге-Кутта
    x_rk, y_rk = runge_kutta4()
    for i in range(4):
        y[i] = y_rk[i]
    
    for i in range(3, n-1):
        # Используем формулу Адамса-Бэшфорта 4-го порядка
        y[i+1] = y[i] + h * (55*f(x[i], y[i]) - 59*f(x[i-1], y[i-1]) + 
                             37*f(x[i-2], y[i-2]) - 9*f(x[i-3], y[i-3])) / 24
    
    return x, y

# Вычисление решений
x_euler, y_euler = euler_method()
x_rk, y_rk = runge_kutta4()
x_adams, y_adams = adams_method()

# Вывод таблицы результатов
print(" x    | Эйлер    | Рунге-Кутта | Адамс     | Точное")
print("------|----------|-------------|-----------|---------")
for i in range(n):
    exact = exact_solution(x_euler[i])
    print(f"{x_euler[i]:.1f}  | {y_euler[i]:.6f} | {y_rk[i]:.6f}   | {y_adams[i]:.6f} | {exact:.6f}")
