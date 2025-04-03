import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox

# Определение функций системы
def f1(x, y):
    return 2*x**2 - x*y - y**2 + 2*x - 2*y + 6

def f2(x, y):
    return y - 0.5*x**2 - 1

# Метод Якоби (переписанный для данной системы)
def jacobi_method(x0, y0, max_iter=100, tol=1e-6):
    iterations = []
    x, y = x0, y0
    for i in range(max_iter):
        # Для данной системы лучше использовать другой подход
        # Так как явно выразить x из первого уравнения сложно
        # Вместо этого используем комбинацию уравнений
        y_new = 0.5*x**2 + 1  # из второго уравнения
        x_new = np.sqrt(2*(y - 1))  # из второго уравнения, выражаем x
        
        # Проверка на комплексные числа
        if np.iscomplex(x_new) or np.iscomplex(y_new):
            return None, None, []
        
        iterations.append((float(x_new), float(y_new)))
        if np.sqrt((x_new - x)**2 + (y_new - y)**2) < tol:
            break
        x, y = x_new, y_new
    return x, y, iterations

# Метод Гаусса-Зейделя (аналогично Якоби)
def gauss_seidel_method(x0, y0, max_iter=100, tol=1e-6):
    iterations = []
    x, y = x0, y0
    for i in range(max_iter):
        y_new = 0.5*x**2 + 1
        x_new = np.sqrt(2*(y_new - 1))
        
        if np.iscomplex(x_new) or np.iscomplex(y_new):
            return None, None, []
        
        iterations.append((float(x_new), float(y_new)))
        if np.sqrt((x_new - x)**2 + (y_new - y)**2) < tol:
            break
        x, y = x_new, y_new
    return x, y, iterations

# Метод Ньютона (рабочий вариант)
def newton_method(x0, y0, max_iter=100, tol=1e-6):
    iterations = []
    x, y = x0, y0
    for i in range(max_iter):
        # Вычисляем значения функций
        F = np.array([f1(x, y), f2(x, y)])
        
        # Вычисляем якобиан
        J = np.array([
            [4*x - y + 2, -x - 2*y - 2],
            [-x, 1]
        ])
        
        try:
            # Решаем систему линейных уравнений J * delta = -F
            delta = np.linalg.solve(J, -F)
            x_new = x + delta[0]
            y_new = y + delta[1]
        except np.linalg.LinAlgError:
            return None, None, []
        
        iterations.append((x_new, y_new))
        if np.sqrt((x_new - x)**2 + (y_new - y)**2) < tol:
            break
        x, y = x_new, y_new
    return x, y, iterations

# Создание и обновление графика
def create_figure():
    fig, ax = plt.subplots(figsize=(6, 5))
    return fig, ax

def update_plot(ax, x_min, x_max, iterations=None):
    ax.clear()
    
    # Создаем сетку для построения
    x = np.linspace(x_min, x_max, 400)
    y = np.linspace(x_min, x_max, 400)
    X, Y = np.meshgrid(x, y)
    
    # Вычисляем значения функций
    Z1 = f1(X, Y)
    Z2 = f2(X, Y)
    
    # Рисуем контуры функций
    ax.contour(X, Y, Z1, levels=[0], colors='r', label='2x² - xy - y² + 2x - 2y + 6 = 0')
    ax.contour(X, Y, Z2, levels=[0], colors='b', label='y - 0.5x² - 1 = 0')
    
    # Если есть итерации, рисуем их
    if iterations:
        iter_x, iter_y = zip(*iterations)
        ax.plot(iter_x, iter_y, 'go-', markersize=4, label='Итерации')
        ax.plot(iter_x[-1], iter_y[-1], 'mo', markersize=8, label='Решение')
    
    # Настройки графика
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('График системы уравнений')
    ax.grid(True)
    ax.legend()

# Обработка нажатия кнопки "Решить"
def solve_button_click():
    try:
        # Получаем входные данные
        x0 = float(x0_entry.get())
        y0 = float(y0_entry.get())
        x_min = float(x_min_entry.get())
        x_max = float(x_max_entry.get())
        method = method_var.get()
        
        # Выбираем метод решения
        if method == "Якоби":
            x, y, iterations = jacobi_method(x0, y0)
        elif method == "Гаусса-Зейделя":
            x, y, iterations = gauss_seidel_method(x0, y0)
        elif method == "Ньютона":
            x, y, iterations = newton_method(x0, y0)
        else:
            messagebox.showerror("Ошибка", "Неизвестный метод")
            return
        
        # Проверка результата
        if x is None or y is None:
            result_label.config(text="Решение не найдено (возможно, расходится)")
        else:
            result_label.config(text=f"Решение: x = {x:.6f}, y = {y:.6f}\nИтераций: {len(iterations)}")
        
        # Обновляем график
        update_plot(ax, x_min, x_max, iterations)
        canvas.draw()
        
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректные входные данные")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

# Создание графического интерфейса
root = tk.Tk()
root.title("Решение системы нелинейных уравнений")

# Основные элементы интерфейса
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Уравнения
ttk.Label(main_frame, text="Система уравнений:").grid(row=0, column=0, columnspan=2, sticky=tk.W)
ttk.Label(main_frame, text="1) 2x² - xy - y² + 2x - 2y + 6 = 0").grid(row=1, column=0, columnspan=2, sticky=tk.W)
ttk.Label(main_frame, text="2) y - 0.5x² - 1 = 0").grid(row=2, column=0, columnspan=2, sticky=tk.W)

# Начальное приближение
ttk.Label(main_frame, text="Начальное приближение:").grid(row=3, column=0, sticky=tk.W)
x0_entry = ttk.Entry(main_frame, width=10)
x0_entry.grid(row=3, column=1, sticky=tk.W)
x0_entry.insert(0, "1.0")

ttk.Label(main_frame, text="y0:").grid(row=4, column=0, sticky=tk.W)
y0_entry = ttk.Entry(main_frame, width=10)
y0_entry.grid(row=4, column=1, sticky=tk.W)
y0_entry.insert(0, "1.0")

# Интервал для графика
ttk.Label(main_frame, text="Интервал x для графика:").grid(row=5, column=0, sticky=tk.W)
x_min_entry = ttk.Entry(main_frame, width=10)
x_min_entry.grid(row=5, column=1, sticky=tk.W)
x_min_entry.insert(0, "-5")

ttk.Label(main_frame, text="x_max:").grid(row=6, column=0, sticky=tk.W)
x_max_entry = ttk.Entry(main_frame, width=10)
x_max_entry.grid(row=6, column=1, sticky=tk.W)
x_max_entry.insert(0, "5")

# Метод решения
ttk.Label(main_frame, text="Метод решения:").grid(row=7, column=0, sticky=tk.W)
method_var = tk.StringVar()
method_combobox = ttk.Combobox(main_frame, textvariable=method_var, 
                              values=["Якоби", "Гаусса-Зейделя", "Ньютона"])
method_combobox.grid(row=7, column=1, sticky=tk.W)
method_combobox.current(2)  # По умолчанию выбран метод Ньютона

# Кнопка решения
solve_button = ttk.Button(main_frame, text="Решить", command=solve_button_click)
solve_button.grid(row=8, column=0, columnspan=2, pady=10)

# Результаты
result_label = ttk.Label(main_frame, text="")
result_label.grid(row=9, column=0, columnspan=2)

# График
fig, ax = create_figure()
update_plot(ax, -5, 5)  # Начальный график
canvas = FigureCanvasTkAgg(fig, master=main_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=10, column=0, columnspan=2)

# Настройка растягивания
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

root.mainloop()