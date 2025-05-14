import math
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

# Константы и данные
EPS = 1e-3
A = 0
B = 1
X_VALUES = [0, 0.13, 0.26, 0.39, 0.52, 0.65, 0.79, 0.92, 1.05, 1.18, 1.31, 1.44, 1.57]
Y_VALUES = [0, 0.004, 0.033, 0.104, 0.217, 0.358, 0.5, 0.608, 0.65, 0.604, 0.467, 0.254, 0]

# Функции для вычисления интегралов
def func(x):
    return 1 / (9 + x**2)

def left_rectangle_integral(a, b, eps):
    n = 1
    integral_prev = 0.0
    while True:
        h = (b - a) / n
        integral = 0.0
        for i in range(n):
            x = a + i * h
            integral += func(x)
        integral *= h
        
        if n > 1 and abs(integral - integral_prev) < eps:
            break
        integral_prev = integral
        n *= 2
    return integral

def mid_rectangle_integral(a, b, eps):
    n = 1
    integral_prev = 0.0
    while True:
        h = (b - a) / n
        integral = 0.0
        for i in range(n):
            x = a + (i + 0.5) * h
            integral += func(x)
        integral *= h
        
        if n > 1 and abs(integral - integral_prev) < eps:
            break
        integral_prev = integral
        n *= 2
    return integral

def right_rectangle_integral(a, b, eps):
    n = 1
    integral_prev = 0.0
    while True:
        h = (b - a) / n
        integral = 0.0
        for i in range(n):
            x = a + (i + 1) * h
            integral += func(x)
        integral *= h
        
        if n > 1 and abs(integral - integral_prev) < eps:
            break
        integral_prev = integral
        n *= 2
    return integral

def trapezoidal_integral(a, b, eps):
    n = 1
    integral_prev = 0.0
    while True:
        h = (b - a) / n
        integral = 0.5 * (func(a) + func(b))
        for i in range(1, n):
            x = a + i * h
            integral += func(x)
        integral *= h
        
        if n > 1 and abs(integral - integral_prev) < eps:
            break
        integral_prev = integral
        n *= 2
    return integral

def simpson_integral(a, b, eps):
    n = 2
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
        
        if n > 2 and abs(integral - integral_prev) < eps:
            break
        integral_prev = integral
        n *= 2
    return integral

def analytical_integral():
    return 2/3 * math.atan(1/3)

def left_rectangles_table_integral():
    integral = 0.0
    for i in range(len(X_VALUES) - 1):
        integral += Y_VALUES[i] * (X_VALUES[i+1] - X_VALUES[i])
    return integral

def right_rectangles_table_integral():
    integral = 0.0
    for i in range(len(X_VALUES) - 1):
        integral += Y_VALUES[i+1] * (X_VALUES[i+1] - X_VALUES[i])
    return integral

def mid_rectangles_table_integral():
    integral = 0.0
    for i in range(len(X_VALUES) - 1):
        mid_y = (Y_VALUES[i] + Y_VALUES[i+1]) / 2
        integral += mid_y * (X_VALUES[i+1] - X_VALUES[i])
    return integral

def trapezoidal_table_integral():
    integral = 0.0
    for i in range(len(X_VALUES) - 1):
        integral += (Y_VALUES[i] + Y_VALUES[i+1]) * (X_VALUES[i+1] - X_VALUES[i]) / 2
    return integral

def simpson_table_integral():
    if (len(X_VALUES) - 1) % 2 != 0:
        raise ValueError("Для метода Симпсона необходимо четное число интервалов")
    
    integral = Y_VALUES[0] + Y_VALUES[-1]
    h = X_VALUES[1] - X_VALUES[0]
    
    for i in range(1, len(X_VALUES)-1):
        if i % 2 == 1:
            integral += 4 * Y_VALUES[i]
        else:
            integral += 2 * Y_VALUES[i]
    
    integral *= h / 3
    return integral

def technical_spec_table_integral():
    return 0.5

def calculate_results(a, b, eps):
    results = []
    
    # Аналитические методы
    results.append(left_rectangle_integral(a, b, eps))
    results.append(mid_rectangle_integral(a, b, eps))
    results.append(right_rectangle_integral(a, b, eps))
    results.append(trapezoidal_integral(a, b, eps))
    results.append(simpson_integral(a, b, eps))
    results.append(analytical_integral())
    
    # Табличные методы
    results.append(left_rectangles_table_integral())
    results.append(right_rectangles_table_integral())
    results.append(mid_rectangles_table_integral())
    results.append(trapezoidal_table_integral())
    try:
        results.append(simpson_table_integral())
    except ValueError:
        results.append("N/A")
    results.append(technical_spec_table_integral())
    
    return results

def plot_graph(win, a, b):
    x = np.linspace(a, b, 1000)
    y = 1 / (9 + x**2)

    fig = Figure(figsize=(5, 3), facecolor='peachpuff')
    ax = fig.add_subplot(111, facecolor='bisque')
    ax.plot(x, y, color='r', linestyle='-', linewidth=2)
    ax.axhline(y=0, color='gray', linestyle='-', linewidth=1)
    ax.grid(True)
    
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    return canvas

def create_table(win, x, y, title, results, start_row):
    frame = Frame(win, bg="peachpuff", bd=2, relief=GROOVE)
    frame.place(x=x, y=y)
    
    Label(frame, text=title, bg="peachpuff", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
    
    methods = ["Лев. прямоуг.", "Средн. прямоуг.", "Прав. прямоуг.", "Трапеции", "Симпсон", "Аналитический"]
    
    for i, method in enumerate(methods):
        Label(frame, text=method, bg="peachpuff", font=("Arial", 10)).grid(row=i+1, column=0, padx=5, pady=2, sticky=W)
        value = results[start_row + i]
        Label(frame, text=f"{value:.6f}" if isinstance(value, float) else value, 
              bg="peachpuff", font=("Arial", 10)).grid(row=i+1, column=1, padx=5, pady=2)
    
    return frame

def show_results():
    try:
        a = float(left_entry.get())
        b = float(right_entry.get())
        eps = float(accuracy_entry.get())
    except ValueError:
        error_label.config(text="Ошибка: введите числовые значения", fg="red")
        return
    
    if a >= b:
        error_label.config(text="Ошибка: левая граница должна быть меньше правой", fg="red")
        return
    
    error_label.config(text="")
    
    # Очистка предыдущих результатов
    for widget in result_widgets:
        widget.destroy()
    result_widgets.clear()
    
    # Вычисление результатов
    results = calculate_results(a, b, eps)
    
    # Построение графика
    canvas = plot_graph(win, a, b)
    canvas.get_tk_widget().place(x=20, y=150)
    result_widgets.append(canvas.get_tk_widget())
    
    # Создание таблиц с результатами
    table1 = create_table(win, 350, 150, "Аналитические методы", results, 0)
    table2 = create_table(win, 350, 350, "Табличные методы", results, 6)
    
    result_widgets.extend([table1, table2])

def reset_fields():
    left_entry.delete(0, END)
    left_entry.insert(0, "0")
    right_entry.delete(0, END)
    right_entry.insert(0, "1")
    accuracy_entry.delete(0, END)
    accuracy_entry.insert(0, "1e-3")
    error_label.config(text="")
    
    for widget in result_widgets:
        widget.destroy()
    result_widgets.clear()

# Создание основного окна
win = Tk()
win.title("Чернышев. Лабораторная работа №4. Вариант 18")
win.geometry("800x600")
win.config(bg="bisque")

# Переменные для хранения виджетов с результатами
result_widgets = []

# Создание элементов интерфейса
Label(win, text="Чернышев. Вариант 18", font=("Arial", 14, "bold"), bg="bisque").pack(pady=10)

# Поля ввода
input_frame = Frame(win, bg="bisque")
input_frame.pack(pady=10)

Label(input_frame, text="Левая граница:", bg="bisque").grid(row=0, column=0, padx=5)
left_entry = Entry(input_frame, width=10)
left_entry.insert(0, "0")
left_entry.grid(row=0, column=1, padx=5)

Label(input_frame, text="Правая граница:", bg="bisque").grid(row=0, column=2, padx=5)
right_entry = Entry(input_frame, width=10)
right_entry.insert(0, "1")
right_entry.grid(row=0, column=3, padx=5)

Label(input_frame, text="Точность:", bg="bisque").grid(row=0, column=4, padx=5)
accuracy_entry = Entry(input_frame, width=10)
accuracy_entry.insert(0, "1e-3")
accuracy_entry.grid(row=0, column=5, padx=5)

# Кнопки
button_frame = Frame(win, bg="bisque")
button_frame.pack(pady=10)

Button(button_frame, text="Рассчитать", command=show_results).pack(side=LEFT, padx=10)
Button(button_frame, text="Сброс", command=reset_fields).pack(side=LEFT, padx=10)

# Метка для ошибок
error_label = Label(win, text="", bg="bisque", fg="red")
error_label.pack()

# Информация о функции
func_frame = Frame(win, bg="peachpuff", bd=2, relief=GROOVE)
func_frame.place(x=20, y=80)

Label(func_frame, text="Функция: f(x) = 1 / (9 + x²)", bg="peachpuff", font=("Arial", 10)).pack(padx=10, pady=5)
Label(func_frame, text="Интеграл от 0 до 1", bg="peachpuff", font=("Arial", 10)).pack(padx=10, pady=5)

win.mainloop()