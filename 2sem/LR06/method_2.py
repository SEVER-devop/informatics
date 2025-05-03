import math

# Определение системы уравнений
def f1(x, y1, y2):
    return -y1 + 8*y2

def f2(x, y1, y2):
    return y1 + y2

# Точные решения
def exact_y1(x):
    return 2*math.exp(3*x) - 4*math.exp(-3*x)

def exact_y2(x):
    return math.exp(3*x) + math.exp(-3*x)

# Параметры задачи
x0 = 0
y10 = exact_y1(x0)  # 2
y20 = exact_y2(x0)  # 2
x_end = 1
h = 0.1
n = int((x_end - x0)/h) + 1

# Метод Эйлера
def euler_method():
    x = [x0 + i*h for i in range(n)]
    y1 = [0.0]*n
    y2 = [0.0]*n
    y1[0] = y10
    y2[0] = y20
    
    for i in range(n-1):
        y1[i+1] = y1[i] + h * f1(x[i], y1[i], y2[i])
        y2[i+1] = y2[i] + h * f2(x[i], y1[i], y2[i])
    
    return x, y1, y2

# Метод Рунге-Кутта 4-го порядка
def runge_kutta4():
    x = [x0 + i*h for i in range(n)]
    y1 = [0.0]*n
    y2 = [0.0]*n
    y1[0] = y10
    y2[0] = y20
    
    for i in range(n-1):
        # Вычисляем коэффициенты для y1
        k1_y1 = h * f1(x[i], y1[i], y2[i])
        k1_y2 = h * f2(x[i], y1[i], y2[i])
        
        k2_y1 = h * f1(x[i] + h/2, y1[i] + k1_y1/2, y2[i] + k1_y2/2)
        k2_y2 = h * f2(x[i] + h/2, y1[i] + k1_y1/2, y2[i] + k1_y2/2)
        
        k3_y1 = h * f1(x[i] + h/2, y1[i] + k2_y1/2, y2[i] + k2_y2/2)
        k3_y2 = h * f2(x[i] + h/2, y1[i] + k2_y1/2, y2[i] + k2_y2/2)
        
        k4_y1 = h * f1(x[i] + h, y1[i] + k3_y1, y2[i] + k3_y2)
        k4_y2 = h * f2(x[i] + h, y1[i] + k3_y1, y2[i] + k3_y2)
        
        # Обновляем значения
        y1[i+1] = y1[i] + (k1_y1 + 2*k2_y1 + 2*k3_y1 + k4_y1)/6
        y2[i+1] = y2[i] + (k1_y2 + 2*k2_y2 + 2*k3_y2 + k4_y2)/6
    
    return x, y1, y2

# Вычисление решений
x_euler, y1_euler, y2_euler = euler_method()
x_rk, y1_rk, y2_rk = runge_kutta4()


# Вывод таблицы результатов
print("Результаты для y1(x):")
print(" x    | Эйлер      | Рунге-Кутта | Точное")
print("------|------------|-------------|---------")
for i in range(n):
    exact = exact_y1(x_euler[i])
    print(f"{x_euler[i]:.1f}  | {y1_euler[i]:.8f} | {y1_rk[i]:.8f}  | {exact:.8f}")

print("\nРезультаты для y2(x):")
print(" x    | Эйлер      | Рунге-Кутта | Точное")
print("------|------------|-------------|---------")
for i in range(n):
    exact = exact_y2(x_euler[i])
    print(f"{x_euler[i]:.1f}  | {y2_euler[i]:.8f} | {y2_rk[i]:.8f}  | {exact:.8f}")
