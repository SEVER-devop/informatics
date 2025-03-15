import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from scipy.optimize import fsolve

# Функция для вычисления значения функции f(x)
def func(x, equation):
    return eval(equation)

# Производная функции f'(x)
def derivative(x, equation):
    from sympy import diff, symbols
    x_sym = symbols('x')
    expr = eval(f"{equation}")
    deriv_expr = diff(expr, x_sym)
    return float(deriv_expr.subs({x_sym: x}))

# Метод Ньютона-Рафсона для поиска корня
def newton_raphson(func, deriv_func, x0, tol=1e-8, max_iter=1000):
    x = x0
    for _ in range(max_iter):
        fx = func(x)
        dfx = deriv_func(x)
        if abs(dfx) < 1e-12:
            print("Ошибка деления на ноль!")
            break
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Основной класс приложения
class RootFinderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Нахождение корня нелинейного уравнения")
        self.geometry("800x600")

        # Поле ввода уравнения
        self.equation_label = tk.Label(self, text="Уравнение:")
        self.equation_entry = tk.Entry(self, width=40)
        self.equation_label.pack(pady=10)
        self.equation_entry.pack(pady=10)

        # Начальное приближение
        self.x0_label = tk.Label(self, text="Начальное приближение:")
        self.x0_entry = tk.Entry(self, width=15)
        self.x0_label.pack(pady=10)
        self.x0_entry.pack(pady=10)

        # Кнопка для расчета
        self.solve_button = tk.Button(self, text="Найти корень", command=self.solve_equation)
        self.solve_button.pack(pady=10)

        # Текстовое поле для вывода результата
        self.result_text = tk.Text(self, height=3, width=60)
        self.result_text.pack(pady=10)

        # Фрейм для графика
        self.graph_frame = tk.Frame(self)
        self.graph_frame.pack(fill=tk.BOTH, expand=True)

        # Инициализация фигуры и холста для графика
        self.figure = Figure(figsize=(6, 4))
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def solve_equation(self):
        try:
            # Получаем уравнение и начальное приближение
            equation = self.equation_entry.get()
            x0 = float(self.x0_entry.get())
            
            # Проверяем корректность уравнения
            func_value = func(x0, equation)
            if not isinstance(func_value, (int, float)):
                raise ValueError("Некорректное уравнение")
                
            # Решаем уравнение методом Ньютона-Рафсона
            root = newton_raphson(lambda x: func(x, equation),
                                  lambda x: derivative(x, equation),
                                  x0)
                                  
            # Выводим результат
            result_message = f"Корень уравнения: {root:.6f}"
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_message)
            
            # Строим график функции
            x_values = np.linspace(root - 2, root + 2, 500)
            y_values = [func(x, equation) for x in x_values]
            self.axes.clear()
            self.axes.plot(x_values, y_values)
            self.axes.set_title(result_message)
            self.axes.grid(True)
            self.canvas.draw()
            
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, str(e))

    # Новая функция для проверки уравнения
    def check_equation(self, equation):
        try:
            # Пробуем вычислить значение функции в точке 0
            value_at_zero = func(0, equation)
            return True
        except Exception as e:
            return False

    # Добавляем проверку уравнения перед решением
    def validate_and_solve(self):
        equation = self.equation_entry.get()
        if self.check_equation(equation):
            self.solve_equation()
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Некорректное уравнение. Попробуйте снова.")

if __name__ == "__main__":
    app = RootFinderApp()
    app.mainloop()