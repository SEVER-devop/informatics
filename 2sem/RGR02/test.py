import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class NonlinearEquationSolver:
    def __init__(self, root_frame):
        self.frame = ttk.LabelFrame(root_frame, text="Задача 1: Решение нелинейного уравнения")
        self.frame.pack(padx=10, pady=5, fill=BOTH, expand=True)
        
        # Уравнение: x^3 - 3x^2 + 3 = 0
        self.equation = "x³ - 3x² + 3 = 0"
        
        ttk.Label(self.frame, text=f"Уравнение: {self.equation}").pack(pady=5)
        
        # Кнопка для решения
        ttk.Button(self.frame, text="Найти корни", command=self.solve).pack(pady=5)
        
        # Область для графика
        self.figure = plt.figure(figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)
        
        # Область для вывода результатов
        self.result_label = ttk.Label(self.frame, text="")
        self.result_label.pack(pady=5)
    
    def f(self, x):
        return x**3 - 3*x**2 + 3
    
    def df(self, x):
        return 3*x**2 - 6*x
    
    def d2f(self, x):
        return 6*x - 6
    
    def combined_method(self, a, b, eps=0.001, max_iter=100):
        if self.f(a) * self.f(b) > 0:
            raise ValueError("Функция должна иметь разные знаки на концах интервала")
        
        # Выбираем начальную точку
        if self.f(a) * self.d2f(a) > 0:
            x0 = a
            method = "касательных"
        else:
            x0 = b
            method = "касательных"
        
        x_prev = b if x0 == a else a
        x = x0
        
        for _ in range(max_iter):
            if method == "касательных":
                x_new = x - self.f(x)/self.df(x)
                method = "хорд"
            else:
                x_new = x - (self.f(x)*(x - x_prev))/(self.f(x) - self.f(x_prev))
                method = "касательных"
            
            if abs(x_new - x) < eps:
                return x_new
            
            x_prev, x = x, x_new
        
        return x
    
    def find_roots(self):
        x = np.linspace(-2, 4, 1000)
        y = self.f(x)
        
        roots_intervals = []
        for i in range(len(x)-1):
            if y[i] * y[i+1] < 0:
                roots_intervals.append((x[i], x[i+1]))
        
        roots = []
        for a, b in roots_intervals:
            try:
                root = self.combined_method(a, b)
                roots.append(root)
            except ValueError:
                continue
        
        return roots
    
    def plot_function(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        x = np.linspace(-2, 4, 400)
        y = self.f(x)
        
        ax.plot(x, y, label=f'f(x) = {self.equation}')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(True)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('График функции и её корни')
        
        roots = self.find_roots()
        for root in roots:
            ax.plot(root, self.f(root), 'ro', label=f'Корень: {root:.3f}')
        
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys())
        
        self.canvas.draw()
    
    def solve(self):
        self.plot_function()
        roots = self.find_roots()
        
        result_text = "Найденные корни:\n"
        for i, root in enumerate(roots, 1):
            result_text += f"Корень {i}: x = {root:.5f}, f(x) = {self.f(root):.5f}\n"
        
        self.result_label.config(text=result_text)

class IntegralCalculator:
    def __init__(self, root_frame):
        self.frame = ttk.LabelFrame(root_frame, text="Задача 2: Численное интегрирование")
        self.frame.pack(padx=10, pady=5, fill=BOTH, expand=True)
        
        # Интеграл: ∫(1 + 0.7x²)/(1.5 + √(2x² + 0.3)) dx от 0.8 до 2.96
        self.integral_text = "∫(1 + 0.7x²)/(1.5 + √(2x² + 0.3)) dx от 0.8 до 2.96"
        
        ttk.Label(self.frame, text=f"Интеграл: {self.integral_text}").pack(pady=5)
        
        # Кнопка для вычисления
        ttk.Button(self.frame, text="Вычислить интеграл", command=self.calculate).pack(pady=5)
        
        # Область для вывода результатов
        self.result_label = ttk.Label(self.frame, text="")
        self.result_label.pack(pady=5)
    
    def f(self, x):
        return (1 + 0.7*x**2) / (1.5 + np.sqrt(2*x**2 + 0.3))
    
    def three_eighths_method(self, a, b, n):
        if n % 3 != 0:
            raise ValueError("Число разбиений n должно быть кратно 3")
        
        h = (b - a) / n
        x = np.linspace(a, b, n+1)
        y = self.f(x)
        
        sum1 = y[0] + y[-1]
        sum2 = sum(y[i] for i in range(1, n) if i % 3 != 0)
        sum3 = sum(y[i] for i in range(3, n, 3))
        
        return 3*h/8 * (sum1 + 3*sum2 + 2*sum3)
    
    def calculate(self):
        a, b = 0.8, 2.96
        n1, n2 = 9, 12
        
        try:
            integral_n1 = self.three_eighths_method(a, b, n1)
            integral_n2 = self.three_eighths_method(a, b, n2)
            
            error = abs(integral_n1 - integral_n2)
            
            result_text = f"Результаты вычисления интеграла:\n"
            result_text += f"При n={n1}: {integral_n1:.6f}\n"
            result_text += f"При n={n2}: {integral_n2:.6f}\n"
            result_text += f"Разница: {error:.6f}"
            
            self.result_label.config(text=result_text)
        except ValueError as e:
            self.result_label.config(text=f"Ошибка: {str(e)}")

class DifferentialEquationSolver:
    def __init__(self, root_frame):
        self.frame = ttk.LabelFrame(root_frame, text="Задача 3: Решение дифференциального уравнения")
        self.frame.pack(padx=10, pady=5, fill=BOTH, expand=True)
        
        # Уравнение: y' = 0.158(x² + sin(0.8x)) + 1.164y
        self.equation = "y' = 0.158(x² + sin(0.8x)) + 1.164y"
        
        ttk.Label(self.frame, text=f"Уравнение: {self.equation}").pack(pady=5)
        ttk.Label(self.frame, text="Интервал: [0.2, 1.2], шаг: 0.1, y(0.2) = 0.25").pack(pady=5)
        
        # Кнопка для решения
        ttk.Button(self.frame, text="Решить уравнение", command=self.solve).pack(pady=5)
        
        # Область для графика
        self.figure = plt.figure(figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)
        
        # Таблица для результатов
        self.tree = ttk.Treeview(self.frame, columns=('x', 'y'), show='headings')
        self.tree.heading('x', text='x')
        self.tree.heading('y', text='y(x)')
        self.tree.pack(pady=5)
    
    def f(self, x, y):
        return 0.158 * (x**2 + np.sin(0.8*x)) + 1.164 * y
    
    def improved_euler(self, x0, y0, h, n):
        x = np.zeros(n+1)
        y = np.zeros(n+1)
        x[0] = x0
        y[0] = y0
        
        for i in range(n):
            x_half = x[i] + h/2
            y_half = y[i] + (h/2) * self.f(x[i], y[i])
            
            x[i+1] = x[i] + h
            y[i+1] = y[i] + h * self.f(x_half, y_half)
        
        return x, y
    
    def solve(self):
        x0, y0 = 0.2, 0.25
        h = 0.1
        n = int((1.2 - 0.2) / h)
        
        x, y = self.improved_euler(x0, y0, h, n)
        
        # Построение графика
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, 'b-o', label='Приближенное решение')
        ax.grid(True)
        ax.set_xlabel('x')
        ax.set_ylabel('y(x)')
        ax.set_title('Решение дифференциального уравнения')
        ax.legend()
        self.canvas.draw()
        
        # Заполнение таблицы
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for i in range(len(x)):
            self.tree.insert('', 'end', values=(f"{x[i]:.1f}", f"{y[i]:.4f}"))

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Домашнее задание 02 (Вариант 3)")
        
        # Создаем меню-бар
        self.create_menu_bar()
        
        # Фреймы для задач (изначально скрыты)
        self.frame_eq = ttk.Frame(root)
        self.frame_int = ttk.Frame(root)
        self.frame_diff = ttk.Frame(root)
        
        # Инициализация решателей задач
        self.eq_solver = NonlinearEquationSolver(self.frame_eq)
        self.int_calculator = IntegralCalculator(self.frame_int)
        self.diff_solver = DifferentialEquationSolver(self.frame_diff)
        
        # Показываем первую задачу по умолчанию
        self.show_frame(self.frame_eq)

    def create_menu_bar(self):
        """Создает меню-бар с кнопками выбора задачи"""
        menubar = Menu(self.root)
        
        # Добавляем выпадающее меню "Задачи"
        task_menu = Menu(menubar, tearoff=0)
        task_menu.add_command(label="Нелинейное уравнение", command=lambda: self.show_frame(self.frame_eq))
        task_menu.add_command(label="Численное интегрирование", command=lambda: self.show_frame(self.frame_int))
        task_menu.add_command(label="Дифференциальное уравнение", command=lambda: self.show_frame(self.frame_diff))
        
        menubar.add_cascade(label="Выбор задания", menu=task_menu)
        self.root.config(menu=menubar)

    def show_frame(self, frame):
        """Показывает выбранный фрейм и скрывает остальные"""
        self.frame_eq.pack_forget()
        self.frame_int.pack_forget()
        self.frame_diff.pack_forget()
        
        frame.pack(fill=BOTH, expand=True)


if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.geometry("900x700")
    root.mainloop()