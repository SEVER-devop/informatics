import math as mt

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk

import numpy as np


'''Классы для нахождения и отображения корней'''
class SolverLeastSquares:
    def __init__(self, win_frame) -> None:
        self.win_frame = win_frame
        self.fun = "np.log(np.tan(x/np.sqrt(10)))"
        self.name = 'First'
        self.values = []
        self.values_pogr = []
        self.tk_val = ["2", "3"]

        self.n = 10
        self.widgets = []
        self.left_border = 2
        self.right_border = 3

        self.names_methods = ["Полином 2-й ст", "Полином 3-й ст", "Полином 4-й ст", "Полином 5-й ст"]
        self.names_up = ["", "Коэфициент 1", "Коэфициент 2", "Коэфициент 3", "Коэфициент 4", "Коэфициент 5", "Коэфициент 6"]
        self.names_up_pogr = ["", "Максимальная абсолютная погрешность", "Максимальная относительная погрешность", "Лучшая аппроксимирующая ф-ия"]
        
        self.__tkinter_fun_sne()
        plot_graph(self)
        

    def __tkinter_fun_sne(self) -> None:
        
        Button(self.win_frame, text="RESET", bg="red", command= lambda: rst(self)).place(x=5, y=5)
        Label(self.win_frame, text="Задание 1: МНК", font="14", bg='bisque').place(x=50, y=70)
        Label(self.win_frame, text="ln(tg(x/(10)^(1/2)))", font="14", bg='bisque').place(x=120, y=100)
        Label(self.win_frame, text="Левая граница:", font= "14", bg='bisque').place(x=30, y=140)
        entry_a = Entry(self.win_frame, textvariable=StringVar(value=2), justify=CENTER)
        entry_a.place(x=230, y=145, width=100)

        Label(self.win_frame, text="Правая граница:", font="14", bg='bisque').place(x=30, y=170)
        entry_b = Entry(self.win_frame, textvariable=StringVar(value=3), justify=CENTER)
        entry_b.place(x=230, y=175, width=100)

        Button(self.win_frame, text="Найти корни", font="14", bg='bisque2', command=lambda: disp_info(self, 0, 700)).place(x=30, y=220)
        Button(self.win_frame, text="Построить график", font="10", bg='bisque2', command=lambda: plot_graph(self)).place(x=180, y=220)


        self.widgets.append(entry_a)
        self.widgets.extend([entry_b])



    # def __polynomial(self, x, coefficients) -> int:
    #     return sum(coef * x**i for i, coef in enumerate(coefficients))

    def __gaus_solver(self, matrix_a, matrix_b) -> list:
        n = len(matrix_b)
        
        # Прямой ход метода Гаусса
        for k in range(n):
            max_row = k
            for i in range(k + 1, n):
                if abs(matrix_a[i, k]) > abs(matrix_a[max_row, k]):
                    max_row = i
            matrix_a[[k, max_row]] = matrix_a[[max_row, k]]
            matrix_b[[k, max_row]] = matrix_b[[max_row, k]]
            
            pivot = matrix_a[k, k]
            if pivot == 0:
                raise ValueError("Матрица системы вырождена")
            matrix_a[k] /= pivot
            matrix_b[k] /= pivot
            
            for i in range(n):
                if i != k and matrix_a[i, k] != 0:
                    factor = matrix_a[i, k]
                    matrix_a[i] -= matrix_a[k] * factor
                    matrix_b[i] -= matrix_b[k] * factor
        
        return matrix_b

    def __least_squares_fit(self, degree, x, y) -> list:
        matrix_a = np.zeros((degree + 1, degree + 1))
        matrix_b = np.zeros(degree + 1)
        
        for i in range(degree + 1):
            for j in range(degree + 1):
                matrix_a[i, j] = np.sum(x**(i + j))
            matrix_b[i] = np.sum(y * x**i)
        
        coefficients = self.__gaus_solver(matrix_a, matrix_b)
        return coefficients

    # Вычисление значений аппроксимирующего полинома
    def __evaluate_polynomial(self, coefficients, x) -> int:
        return sum(coef * x**i for i, coef in enumerate(coefficients))

    def __calculate_errors(self, y_true, y_pred) -> list:
        absolute_errors = np.abs(y_true - y_pred)
        relative_errors = absolute_errors / np.abs(y_true)
        return absolute_errors, relative_errors 



    def get_roots(self) -> None:
        try:
            self.left_border = float(self.widgets[0].get())
            self.right_border = float(self.widgets[1].get())
        except Exception as e:
            return error(e)


        degrees = [2, 3, 4, 5]
        results = {}
        x_values = np.linspace(self.left_border, self.right_border, self.n)
        y_values = np.log(np.tan(x_values / np.sqrt(10)))   

        for degree in degrees:
            coefficients = self.__least_squares_fit(degree, x_values, y_values)
            y_pred = self.__evaluate_polynomial(coefficients, x_values)
            abs_errors, rel_errors = self.__calculate_errors(y_values, y_pred)
            
            results[degree] = {
                'coefficients': coefficients,
                'y_pred': y_pred,
                'abs_errors': abs_errors,
                'rel_errors': rel_errors,
                'max_abs_error': np.max(abs_errors),
                'max_rel_error': np.max(rel_errors)
            }
        
        best_degree = min(degrees, key=lambda d: results[d]['max_abs_error'])


        self.values = [[i for i in results[degree]['coefficients']] for degree in degrees]
        self.values_pogr = [[results[degree][i]  for i in ["max_abs_error", "max_rel_error"]] for degree in degrees]
        self.values_pogr[best_degree-2].append("+")
        disp_info(self, 500, 100, self.values_pogr)
        
        
class SolverLagrange:
    def __init__(self, win_frame) -> None:
        self.win_frame = win_frame
        self.fun = "np.log(np.tan(x/np.sqrt(10)))"
        self.name = 'First'

        self.values = []
        self.tk_val = ["2", "3"]
        self.widgets = []

        self.n = 10
        self.left_border = 2
        self.right_border = 3

        self.names_methods = ["X", "Y точные", "Y Лагранж"]
        self.names_up = ["", "Значения"]
        
        self.__tkinter_fun_se()
        plot_graph(self)
        

    def __tkinter_fun_se(self) -> None:
        Button(self.win_frame, text="RESET", bg="red", command= lambda: rst(self)).place(x=5, y=5)
        Label(self.win_frame, text="Задание 2: Многочлен Лагранжа", font="14", bg='bisque').place(x=50, y=70)
        Label(self.win_frame, text="ln(tg(x/(10)^(1/2)))", font="14", bg='bisque').place(x=120, y=100)
        Label(self.win_frame, text="Левая граница:", font= "14", bg='bisque').place(x=30, y=140)
        entry_a = Entry(self.win_frame, textvariable=StringVar(value=2), justify=CENTER)
        entry_a.place(x=230, y=145, width=100)

        Label(self.win_frame, text="Правая граница:", font="14", bg='bisque').place(x=30, y=170)
        entry_b = Entry(self.win_frame, textvariable=StringVar(value=3), justify=CENTER)
        entry_b.place(x=230, y=175, width=100)

        Button(self.win_frame, text="Найти корни", font="14", bg='bisque2', command=lambda: disp_info(self, 0, 700)).place(x=30, y=220)
        Button(self.win_frame, text="Построить график", font="10", bg='bisque2', command=lambda: plot_graph(self)).place(x=180, y=220)


        self.widgets.append(entry_a)
        self.widgets.extend([entry_b])



    def __lagrange_interpolation(self, x, x_nodes, y_nodes) -> int:
        n = len(x_nodes)
        result = 0.0
        for i in range(n):
            term = y_nodes[i]
            for j in range(n):
                if i != j:
                    term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
            result += term
        return result


    def get_roots(self) -> None:
        try:
            self.left_border = float(self.widgets[0].get())
            self.right_border = float(self.widgets[1].get())
        except Exception as e:
            return error(e)


        x_values = np.linspace(self.left_border, self.right_border, self.n)
        y_values = np.log(np.tan(x_values / np.sqrt(10)))

        delta_x = (self.left_border - self.right_border) / self.n
        x_intermediate = np.array([self.left_border + delta_x * (j + 0.5) for j in range(self.n)])
        y_exact = np.log(np.tan(x_intermediate / np.sqrt(10)))  # Точные значения
        y_lagrange = np.array([self.__lagrange_interpolation(x, x_values, y_values) for x in x_intermediate])  # Значения по Лагранжу


        absolute_errors = np.abs(y_exact - y_lagrange)
        relative_errors = absolute_errors / np.abs(y_exact)

        print("\nАбсолютные погрешности:", absolute_errors)
        print("\nОтносительные погрешности:", relative_errors)

        self.values = [[round(i,4) for i in x_intermediate],
                       [round(i,4) for i in y_exact],
                       [round(i,4) for i in y_lagrange]]


'''Основной класс'''
class Application:
    def __init__(self, win) -> None:
        self.win = win
        self.tk_widgets = []
        
        # Создаем меню-бар
        self.create_menu_bar()
        style = ttk.Style()
        style.configure("Custom.TFrame", background="bisque") 
        self.frame_squares = ttk.Frame(win, style="Custom.TFrame")
        self.frame_lagrange = ttk.Frame(win, style="Custom.TFrame")
        self.solver_squares = SolverLeastSquares(self.frame_squares)
        self.solver_lagrange = SolverLagrange(self.frame_lagrange)

        self.show_frame(self.frame_squares)

    def create_menu_bar(self) -> None:
        """Создает меню-бар с кнопками выбора задачи"""
        menubar = Menu(self.win)
        
        # Добавляем выпадающее меню "Задачи"
        task_menu = Menu(menubar, tearoff=0, font="15")
        task_menu.add_command(label="Задание 1 МНК", command=lambda: self.show_frame(self.frame_squares))
        task_menu.add_command(label="Задание 2 Лагранж", command=lambda: self.show_frame(self.frame_lagrange))
        
        menubar.add_cascade(label="Выбор задания", menu=task_menu)
        self.win.config(menu=menubar)

    def show_frame(self, frame) -> None:
        """Показывает выбранный фрейм и скрывает остальные"""
        self.frame_squares.pack_forget()
        self.frame_lagrange.pack_forget()
        
        frame.pack(fill=BOTH, expand=True)


def error(er='Ошибка') -> None:
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


def disp_info(obj, x_cord=500, y_cord=250, dop_values=None) -> None:
    
    if not(dop_values):
        obj.get_roots()
        values = obj.values
        names_methods = obj.names_methods
        names_up = obj.names_up
    else:
        values = obj.values_pogr
        names_methods = obj.names_methods
        names_up = obj.names_up_pogr

    table_frame = Frame(master=obj.win_frame, bg="peachpuff")
    table_frame.place(x=x_cord, y=y_cord)
    obj.widgets.append(table_frame)

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
    win.title("Лабораторная работа №5 Вершинин АТ-24-01")
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
