import math as mt

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk

import numpy as np

from scipy.optimize import root_scalar
from scipy.integrate import quad


'''Классы для нахождения и отображения корней'''
class SolverNonlinearEquations:
    def __init__(self, win_frame):
        self.win_frame = win_frame
        self.fun = "x**3 - 3*x**2 + 3"
        self.name = 'First'
        self.values = []
        self.tk_val = ["-1", "3"]
        self.widgets = []
        self.eps = 1e-3
        self.max_iter = 1000
        self.left_border = -1
        self.right_border = 3
        self.names_methods = ["Корень 1", "Корень 2", "Корень 3", "Scipy"]
        self.names_up = ["", "Значения"]
        
        self.__tkinter_fun_sne()
        plot_graph(self)
        

    def __tkinter_fun_sne(self):
        
        Button(self.win_frame, text="RESET", bg="red", command= lambda: rst(self)).place(x=5, y=5)
        Label(self.win_frame, text="Задание 1: Нелинейное уравнение", font="14", bg='bisque').place(x=50, y=70)
        Label(self.win_frame, text="x^3 - 3x^2 + 3 = 0", font="14", bg='bisque').place(x=120, y=100)
        Label(self.win_frame, text="Левая граница:", font= "14", bg='bisque').place(x=30, y=140)
        entry_a = Entry(self.win_frame, textvariable=StringVar(value=-1), justify=CENTER)
        entry_a.place(x=230, y=145, width=100)

        Label(self.win_frame, text="Правая граница:", font="14", bg='bisque').place(x=30, y=170)
        entry_b = Entry(self.win_frame, textvariable=StringVar(value=3), justify=CENTER)
        entry_b.place(x=230, y=175, width=100)

        Button(self.win_frame, text="Найти корни", font="14", bg='bisque2', command=lambda: disp_info(self)).place(x=30, y=220)
        Button(self.win_frame, text="Построить график", font="10", bg='bisque2', command=lambda: plot_graph(self)).place(x=180, y=220)


        self.widgets.append(entry_a)
        self.widgets.extend([entry_b])

        
    def __f(self, x):
        return x**3 - 3*x**2 + 3

    def __df(self, x):
        return 3*x**2 - 6*x

    def __ddf(self, x):
        return 6*x - 6

    def hord_kasat_method(self):
        roots = []
        x = self.left_border
        b = self.right_border
        eps = self.eps
        h = 0.1

        while x < b:
            x1 = x
            x2 = min(x + h, b)

            if self.__f(x1) * self.__f(x2) < 0:  # есть смена знака
                mid = (x1 + x2) / 2

                if self.__f(x1) * self.__ddf(mid) > 0:
                    x_n = x1
                    x_v_n = x2
                    for _ in range(self.max_iter):
                        de1 = self.__df(x_n)
                        de2 = self.__f(x_v_n) - self.__f(x_n)
                        if abs(de1) < 1e-12 or abs(de2) < 1e-12:
                            break
                        x_next = x_n - self.__f(x_n) / de1
                        x_v_next = x_n - self.__f(x_n) * (x_v_n - x_n) / de2
                        if abs(x_v_next - x_next) < eps:
                            break
                        x_n = x_next
                        x_v_n = x_v_next
                    root = round((x_n + x_v_n) / 2, 6)
                    if all(abs(root - r) > eps for r in roots):
                        roots.append(root)

                elif self.__f(x2) * self.__ddf(mid) > 0:
                    x_n = x1
                    x_v_n = x2
                    for _ in range(self.max_iter):
                        de1 = self.__df(x_v_n)
                        de2 = self.__f(x_v_n) - self.__f(x_n)
                        if abs(de1) < 1e-12 or abs(de2) < 1e-12:
                            break
                        x_next = x_n - self.__f(x_v_n) * (x_v_n - x_n) / de2
                        x_v_next = x_v_n - self.__f(x_v_n) / de1
                        if abs(x_v_next - x_next) < eps:
                            break
                        x_n = x_next
                        x_v_n = x_v_next
                    root = round((x_n + x_v_n) / 2, 6)
                    if all(abs(root - r) > eps for r in roots):
                        roots.append(root)
                else:
                    pass  # ни одно из условий не выполняется

            x += h
        return roots

    def scipy_roots_finder(self):
        a, b = self.left_border, self.right_border
        step = 0.1

        roots = []
        x_values = np.arange(a, b + step, step)

        for i in range(len(x_values) - 1):
            x1, x2 = x_values[i], x_values[i + 1]
            if self.__f(x1) * self.__f(x2) < 0:
                result = root_scalar(self.__f, bracket=[x1, x2], method='brentq')
                root = result.root
                if not any(abs(root - r) < self.eps for r in roots):
                    roots.append(root)
        
        return roots

    def get_roots(self):
        try:
            self.left_border = float(self.widgets[0].get())
            self.right_border = float(self.widgets[1].get())
        except Exception as e:
            return error(e)


        self.values = [i for i in self.hord_kasat_method()]
        self.values.append(self.scipy_roots_finder())
        
class NumericalIntegration:
    def __init__(self, win_frame):
        self.win_frame = win_frame
        self.fun = "(1 + 0.7 * x**2) / (1.5 + (2*x**2 + 0.3)**0.5)"
        self.name = 'First'
        self.values = []
        self.tk_val = ["0.8", "2.96"]
        self.widgets = []
        self.eps = 1e-3
        self.max_iter = 1000
        self.left_border = 0.8
        self.right_border = 2.96
        self.names_methods = ["Корень n=9", "Корень n=12", "Scipy"]
        self.names_up = ["", "Значения"]
        
        self.__tkinter_fun_ni()
        plot_graph(self)
        

    def __tkinter_fun_ni(self):


        # Интеграл
        fig = Figure(figsize=(4, 3), facecolor='bisque')
        ax = fig.add_subplot(111)
        ax.axis('off')
        integral_text = r"$\int_{0{,}8}^{2{,}96} \frac{1 + 0{,}7x^2}{1{,}5 + \sqrt{2x^2 + 0{,}3}} \, dx$"
        ax.text(0.5, 0.5, integral_text, fontsize=10, 
                ha='center', va='center', color='black')
        canvas = FigureCanvasTkAgg(fig, master=self.win_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=-10, y=-35)

        Button(self.win_frame, text="RESET", bg="red", command= lambda: rst(self)).place(x=5, y=5)
        Label(self.win_frame, text="Задание 2: Численное интегрирование", font="14", bg='bisque').place(x=50, y=70)
        Label(self.win_frame, text="Левая граница:", font= "14", bg='bisque').place(x=30, y=140)
        entry_a = Entry(self.win_frame, textvariable=StringVar(value=0.8), justify=CENTER)
        entry_a.place(x=230, y=145, width=100)

        Label(self.win_frame, text="Правая граница:", font="14", bg='bisque').place(x=30, y=170)
        entry_b = Entry(self.win_frame, textvariable=StringVar(value=2.96), justify=CENTER)
        entry_b.place(x=230, y=175, width=100)

        Button(self.win_frame, text="Найти корни", font="14", bg='bisque2', command=lambda: disp_info(self)).place(x=30, y=220)
        Button(self.win_frame, text="Построить график", font="10", bg='bisque2', command=lambda: plot_graph(self)).place(x=180, y=220)


        self.widgets.append(entry_a)
        self.widgets.extend([entry_b])

    def __integral(self, x):
        return (1 + 0.7 * x**2) / (1.5 + (2*x**2 + 0.3)**0.5)
    
    def scipy_roots_finder(self):
        result, error = quad(self.__integral, self.left_border, self.right_border)
        return result
    
    def three_eighths(self):
        a = self.left_border
        b = self.right_border
        roots = []
        for n in [9, 12]:
            if n % 3 != 0:
                raise ValueError("Число разбиений должно быть кратно 3")

            h = (b - a) / n
            x = np.linspace(a, b, n + 1)
            y = self.__integral(x)

            sum3 = np.sum(y[3:-1:3])
            other_indices = [i for i in range(1, n) if i % 3 != 0]
            sum2 = np.sum(y[other_indices])
            
            integral = (3 * h / 8) * (y[0] + y[-1] + 3 * sum2 + 2 * sum3)
            roots.append(integral)
            
        return roots

    def get_roots(self):
        try:
            self.left_border = float(self.widgets[0].get())
            self.right_border = float(self.widgets[1].get())
        except Exception as e:
            return error(e)


        self.values = [i for i in self.three_eighths()]
        self.values.append(self.scipy_roots_finder())

class SolverDifferentialEquations:
    def __init__(self, win_frame):
        self.win_frame = win_frame
        self.name = 'Third'
        self.values = []
        self.tk_val = ["0.2", "1.2"]
        self.widgets = []
        self.names_methods = ["X", "Y"]
        self.names_up = ["", "Значения"]
        
        self.__tkinter_fun_sde()
        
    
    def __tkinter_fun_sde(self):
        
        Button(self.win_frame, text="RESET", bg="red", command= lambda: rst(self)).place(x=5, y=5)
        Label(self.win_frame, text="Задание 3: Дифференциальное уравнение", font="14", bg='bisque').place(x=50, y=70)
        Label(self.win_frame, text="y' = 0.158 * (x**2 + sin(0.8 * x)) + 1.164 * y", font="14", bg='bisque').place(x=60, y=100)

        Button(self.win_frame, text="Найти корни", font="14", bg='bisque2', command=lambda: disp_info(self)).place(x=140, y=220)

    def __ode_func(self, x, y):
        return 0.158 * (x**2  + np.sin(0.8 * x)) + 1.164 * y

    def broken_line_method(self):
        x0 = 0.2
        y0 = 0.25
        x_end = 1.2
        h = 0.1

        x_vals = [x0]
        y_vals = [y0]
        while x0 < x_end:
            x_half = x0 + h / 2
            y_half = y0 + (h / 2) * self.__ode_func(x0, y0)
            y_next = y0 + h * self.__ode_func(x_half, y_half)
            x0 += h
            y0 = y_next
            x_vals.append(round(x0, 4))
            y_vals.append(round(y0, 4))
        return x_vals, y_vals

    def get_roots(self):
        self.values = [i for i in self.broken_line_method()]
        plot_graph(self)



'''Основной класс'''
class Application:
    def __init__(self, win):
        self.win = win
        self.tk_widgets = []
        
        # Создаем меню-бар
        self.create_menu_bar()
        style = ttk.Style()
        style.configure("Custom.TFrame", background="bisque") 
        self.frame_eq = ttk.Frame(win, style="Custom.TFrame")
        self.frame_int = ttk.Frame(win, style="Custom.TFrame")
        self.frame_diff = ttk.Frame(win, style="Custom.TFrame")
        self.eq_solver = SolverNonlinearEquations(self.frame_eq)
        self.int_calculator = NumericalIntegration(self.frame_int)
        self.diff_solver = SolverDifferentialEquations(self.frame_diff)

        self.show_frame(self.frame_eq)

    def create_menu_bar(self):
        """Создает меню-бар с кнопками выбора задачи"""
        menubar = Menu(self.win)
        
        # Добавляем выпадающее меню "Задачи"
        task_menu = Menu(menubar, tearoff=0, font="15")
        task_menu.add_command(label="Нелинейное уравнение", command=lambda: self.show_frame(self.frame_eq))
        task_menu.add_command(label="Численное интегрирование", command=lambda: self.show_frame(self.frame_int))
        task_menu.add_command(label="Дифференциальное уравнение", command=lambda: self.show_frame(self.frame_diff))
        
        menubar.add_cascade(label="Выбор задания", menu=task_menu)
        self.win.config(menu=menubar)

    def show_frame(self, frame):
        """Показывает выбранный фрейм и скрывает остальные"""
        self.frame_eq.pack_forget()
        self.frame_int.pack_forget()
        self.frame_diff.pack_forget()
        
        frame.pack(fill=BOTH, expand=True)


def error(er='Ошибка'):
    er_win = Toplevel(win)
    er_win.title("Ошибка")
    er_win.geometry("350x150")
    Label(er_win, text=er, font="30", bg="red").pack()


def plot_graph(obj) -> None:

    try:
        if obj.name != "Third":
            obj.left_border = float(obj.widgets[0].get())
            obj.right_border = float(obj.widgets[1].get())
    except Exception as e:
        return error(e)
    
    if obj.name != "Third":
        x = np.linspace(obj.left_border, obj.right_border, 1000)
        y = eval(obj.fun)
    else:
        x = obj.values[0]
        y = obj.values[1]

    fig = Figure(figsize=(4, 4), facecolor='peachpuff')
    ax = fig.add_subplot(facecolor='bisque')
    
    ax.plot(x, y, color='r', linestyle='solid', linewidth=2)

    ax.axhline(y=0, color='gray', linestyle='-', linewidth=1)
    fig.patch.set_edgecolor('whitesmoke')
    fig.patch.set_linewidth(2) 

    canvas1 = FigureCanvasTkAgg(fig, master = obj.win_frame)
    canvas1.draw()
    canvas1.get_tk_widget().place(x=-1, y=300)
    obj.widgets.append(canvas1)


def disp_info(obj) -> None:

    obj.get_roots()
    values = obj.values
    names_methods = obj.names_methods
    names_up = obj.names_up
    table_frame = Frame(master=obj.win_frame, bg="peachpuff")
    table_frame.place(x=500, y=250)
    obj.widgets.append(table_frame)
    print(len(values))

    for i in range(len(names_up)):
        cell = Label(table_frame, text=f"{names_up[i]}", bg="peachpuff", font="15" )
        cell.grid(row=0, column=i, padx=20)

    for i in range(len(values)):
        if i != len(values)-1:
            cell = Label(table_frame, text=f"{names_methods[i]}", bg="peachpuff", font="15" )
            cell.grid(row=i+1, column=0, padx=20, pady=20)
        else:
            cell = Label(table_frame, text=f"{names_methods[-1]}", bg="peachpuff", font="15" )
            cell.grid(row=i+1, column=0, padx=20, pady=20)
        if type(values[i]) == type([]) or type(values[i]) == type(()):
            for j in range(len(values[i])):
                cell = Label(table_frame, text=f"{values[i][j]}", bg="peachpuff", font="15" )
                cell.grid(row=i+1, column=j+1, padx=20)
        else:
            cell = Label(table_frame, text=f"{values[i]}", bg="peachpuff", font="15" )
            cell.grid(row=i+1, column=1, padx=20)
        if len(values) == 1:
            cell = Label(table_frame, text=f"Корней нет", bg="peachpuff", font="15" )
            cell.grid(row=1, column=1, padx=20)
            cell = Label(table_frame, text=f"Ошибка", bg="peachpuff", font="15" )
            cell.grid(row=1, column=0, padx=20)

def tkinter_fun() -> None: 
    win.title("РГР №2 Вершинин АТ-24-01")
    win.state('zoomed')
    win.resizable(0, 0)
    win.attributes("-alpha", 0.96)
    win.config(bg="bisque")
    Label(text="Вершинин Сергей АТ-24-01\nВариант №3", font="30", bg="bisque").place(x=100, y=10)

def rst(obj) -> None:
    values = obj.tk_val
    for i in range(len(obj.widgets)):
        if "matplotlib.backends.backend_tkagg.FigureCanvasTkAgg" in str(obj.widgets[i]):
            obj.widgets[i].get_tk_widget().destroy()
        elif ".!frame" in str(obj.widgets[i]) and ".!entry" not in str(obj.widgets[i]):
            obj.widgets[i].destroy()
        elif type(None) != type(obj.widgets[i]):
            obj.widgets[i].delete(0, END)
            obj.widgets[i].insert(0, values[i])
    if obj.name == "First":
        plot_graph(obj)
        



win = Tk()
app = Application(win)
tkinter_fun()
win.mainloop()
