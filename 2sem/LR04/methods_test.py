import math

def left_rectangle_integral(func, a, b, precision=1e-3):
    """
    Вычисляет интеграл методом левых прямоугольников с заданной точностью.
    """
    n = 1
    integral_prev = 0.0
    while True:
        h = (b - a) / n
        integral = 0.0
        for i in range(n):
            x = a + i * h
            integral += func(x)
        integral *= h
        
        if n > 1 and abs(integral - integral_prev) < precision:
            break
        integral_prev = integral
        n *= 2
    return integral

def mid_rectangle_integral(func, a, b, precision=1e-3):
    """
    Вычисляет интеграл методом средних прямоугольников с заданной точностью.
    """
    n = 1
    integral_prev = 0.0
    while True:
        h = (b - a) / n
        integral = 0.0
        for i in range(n):
            x = a + (i + 0.5) * h
            integral += func(x)
        integral *= h
        
        if n > 1 and abs(integral - integral_prev) < precision:
            break
        integral_prev = integral
        n *= 2
    return integral

def right_rectangle_integral(func, a, b, precision=1e-3):
    """
    Вычисляет интеграл методом правых прямоугольников с заданной точностью.
    """
    n = 1
    integral_prev = 0.0
    while True:
        h = (b - a) / n
        integral = 0.0
        for i in range(n):
            x = a + (i + 1) * h
            integral += func(x)
        integral *= h
        
        if n > 1 and abs(integral - integral_prev) < precision:
            break
        integral_prev = integral
        n *= 2
    return integral

def trapezoidal_integral(func, a, b, precision=1e-3):
    """
    Вычисляет интеграл методом трапеций с заданной точностью.
    """
    n = 1
    integral_prev = 0.0
    while True:
        h = (b - a) / n
        integral = 0.5 * (func(a) + func(b))
        for i in range(1, n):
            x = a + i * h
            integral += func(x)
        integral *= h
        
        if n > 1 and abs(integral - integral_prev) < precision:
            break
        integral_prev = integral
        n *= 2
    return integral

def simpson_integral(func, a, b, precision=1e-3):
    """
    Вычисляет интеграл методом Симпсона с заданной точностью.
    """
    n = 2  # Должно быть четным для метода Симпсона
    integral_prev = 0.0
    while True:
        h = (b - a) / n
        integral = func(a) + func(b)
        for i in range(1, n):
            x = a + i * h
            if i % 2 == 0:
                integral += 2 * func(x)
            else:
                integral += 4 * func(x)
        integral *= h / 3
        
        if n > 2 and abs(integral - integral_prev) < precision:
            break
        integral_prev = integral
        n *= 2
    return integral

# Пример использования:
def test_func(x):
    return math.exp(-(x**2)/2)

a = -2
b = 2
precision = 1e-3

print("Метод левых прямоугольников:", left_rectangle_integral(test_func, a, b, precision))
print("Метод средних прямоугольников:", mid_rectangle_integral(test_func, a, b, precision))
print("Метод правых прямоугольников:", right_rectangle_integral(test_func, a, b, precision))
print("Метод трапеций:", trapezoidal_integral(test_func, a, b, precision))
print("Метод Симпсона:", simpson_integral(test_func, a, b, precision))