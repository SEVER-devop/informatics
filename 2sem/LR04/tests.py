def integrate_from_table(x_values, y_values, method='simpson', precision=1e-3):
    n = len(x_values)
    h = x_values[1] - x_values[0]  # предполагаем равномерную сетку
    
    if method == 'left_rect':
        # Левые прямоугольники: сумма всех y, кроме последнего
        integral = sum(y_values[:-1]) * h
        
    elif method == 'right_rect':
        # Правые прямоугольники: сумма всех y, кроме первого
        integral = sum(y_values[1:]) * h
        
    elif method == 'mid_rect':
        # Средние прямоугольники: среднее между соседними y
        integral = sum((y_values[i] + y_values[i+1]) / 2 for i in range(n-1)) * h
        
    elif method == 'trapezoid':
        # Метод трапеций: (y0 + yn)/2 + сумма остальных y
        integral = (y_values[0] + y_values[-1]) / 2 + sum(y_values[1:-1])
        integral *= h
        
    elif method == 'simpson':
        # Метод Симпсона (требует четного числа интервалов)
        if (n - 1) % 2 != 0:
            raise ValueError("Для метода Симпсона число интервалов должно быть четным!")
        integral = y_values[0] + y_values[-1]
        for i in range(1, n-1):
            if i % 2 == 1:
                integral += 4 * y_values[i]
            else:
                integral += 2 * y_values[i]
        integral *= h / 3
        
    else:
        raise ValueError(f"Неизвестный метод: {method}")
    
    return integral

x_values = [0, 0.13, 0.26, 0.39, 0.52, 0.65, 0.79, 0.92, 1.05, 1.18, 1.31, 1.44, 1.57]
y_values = [0, 0.004, 0.033, 0.104, 0.217, 0.358, 0.5, 0.608, 0.65, 0.604, 0.467, 0.254, 0]

print("Левые прямоугольники:", integrate_from_table(x_values, y_values, 'left_rect'))
print("Правые прямоугольники:", integrate_from_table(x_values, y_values, 'right_rect'))
print("Средние прямоугольники:", integrate_from_table(x_values, y_values, 'mid_rect'))
print("Трапеции:", integrate_from_table(x_values, y_values, 'trapezoid'))
print("Симпсон:", integrate_from_table(x_values, y_values, 'simpson'))