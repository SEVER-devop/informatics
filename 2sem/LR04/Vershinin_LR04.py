from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

import math
import numpy as np


class RootFinder:
    def __init__(self):
        self.values = [None for _ in range(5)]
        self.widgets = []
        self.eps = 1e-3
        self.a = 0
        self.b = 1


    def __func(self, x) -> None:
        return math.log(x + math.sqrt(x*x + 8))


    def __left_rectangle_integral(self, precision=1e-3) -> None:
        func = self.__func
        a = self.a
        b = self.b
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
        self.values[0] = integral


    def __mid_rectangle_integral(self, precision=1e-3) -> None:
        func = self.__func
        a = self.a
        b = self.b
        n = 1
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
        self.values[1] = integral


    def __right_rectangle_integral(self, precision=1e-3) -> None:
        func = self.__func
        a = self.a
        b = self.b
        n = 1
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
        self.values[2] = integral


    def __trapezoidal_integral(self, precision=1e-3) -> None:
        func = self.__func
        a = self.a
        b = self.b
        n = 1
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
        self.values[3] = integral


    def __simpson_integral(self, precision=1e-3) -> None:
        func = self.__func
        a = self.a
        b = self.b
        n = 1
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
        self.values[4] = integral


    def get_roots(self):
        self.__left_rectangle_integral()
        self.__mid_rectangle_integral()
        self.__right_rectangle_integral()
        self.__trapezoidal_integral()
        self.__simpson_integral()

        return self.values




roots = RootFinder()


def error(er='Ошибка'):
    er_win = Toplevel(win)
    er_win.title("Ошибка")
    er_win.geometry("350x150")
    Label(er_win, text=er, font="30", bg="red").pack()


    
def disp_info(ent_accur) -> None:
    try:
        accuracity = float(ent_accur.get())
    except ValueError:
        return error("Введите численные значениия\n в границах")
    roots.eps = accuracity

    values = roots.get_roots()
    names_methods = ["Лев. треуг.", "Средн. треуг.", "Прав. треуг.", "Трапец.", "Симпсон"]
    names_up = ["Методы вычисления", "RES"]
    table_frame = Frame(master=win, bg="peachpuff")
    table_frame.place(x=500, y=250)
    roots.widgets.append(table_frame)


    for i in range(len(names_up)):
        cell = Label(table_frame, text=f"{names_up[i]}", bg="peachpuff", font="15" )
        cell.grid(row=0, column=i, padx=20)

    for i in range(len(names_methods)):
        cell = Label(table_frame, text=f"{names_methods[i]}", bg="peachpuff", font="15" )
        cell.grid(row=i+1, column=0, padx=20, pady=20)
        cell = Label(table_frame, text=f"{values[i]}", bg="peachpuff", font="15" )
        cell.grid(row=i+1, column=1, padx=20)


def disp_matrix(mat, x1, y1=385) -> None:

    table_frame = Frame(master=win, bg="bisque2")
    table_frame.place(x=x1, y=y1)
    for i in range(len(mat)):
        if type(mat[i]) == list:
            for j in range(len(mat[i])):
                cell = Label(table_frame, text=f"{mat[i][j]}", bg="bisque2", font="15" )
                cell.grid(row=i, column=j, padx=10, pady=10)
        else:
            cell = Label(table_frame, text=f"{mat[i]}", bg="bisque2", font="15" )
            cell.grid(row=i, column=0, padx=10, pady=10)


def plot_graph(ent_left, ent_right) -> None:

    try:
        left_border = float(ent_left.get())
        right_border = float(ent_right.get())
    except ValueError:
        return error("Введите численные значениия\n в границах")
    roots.left_border = left_border
    roots.right_border = right_border


    x = np.linspace(left_border, right_border, 1000)
    y = np.linspace(left_border, right_border, 1000)
    X, Y = np.meshgrid(x, y)

    graph_1 = np.log(X + np.sqrt(X*X + 8))

    fig = Figure(figsize=(4, 4), facecolor='peachpuff')
    ax = fig.add_subplot(facecolor='bisque')

    ax.contour(X, Y, graph_1, levels=[-1], colors='r', linestyles='solid')

    ax.axhline(y=0, color='gray', linestyle='-', linewidth=1)
    fig.patch.set_edgecolor('whitesmoke')
    fig.patch.set_linewidth(2) 

    canvas1 = FigureCanvasTkAgg(fig, master = win)
    canvas1.draw()
    canvas1.get_tk_widget().place(x=0, y=300)
    # roots.widgets.append(canvas1)
    

def tkinter_fun() -> None:
    
    win.title("Лабораторная работа №4 Вершинин АТ-24-01")
    win.state('zoomed')
    win.resizable(0, 0)
    win.attributes("-alpha", 0.96)
    win.config(bg="bisque")
    Label(text="Вершинин Сергей АТ-24-01\nВариант №3", font="30", bg="bisque").place(x=70, y=740)

    Canvas(bg="peachpuff", width=395, height=300).place(x=1, y=1)
    Canvas(bg="bisque2", width=395, height=270).place(x=1, y=301)

    # Границы
    Label(text="Границы", font="15", bg="peachpuff").place(x=23, y=105)
    ent_left_border = Entry(win, textvariable=StringVar(value=-5), width=5, justify=CENTER)
    ent_left_border.place(x=25, y=135)
    ent_right_border = Entry(win, textvariable=StringVar(value=5), width=5, justify=CENTER)
    ent_right_border.place(x=65, y=135)


    # Уравнение
    # Label(text="Матрица A", font="15", bg="bisque2").place(x=60, y=335)
    # Label(text="Матрица B", font="15", bg="bisque2").place(x=255, y=335)
    # disp_matrix(roots.matrix_a, 20)
    # disp_matrix(roots.matrix_b, 280)

    
    # Точность
    Label(text="Точность", font="15", bg="peachpuff").place(x=140, y=125)
    ent_accuracy = Entry(win, textvariable=StringVar(value="1e-3"), width=9, justify=CENTER)
    ent_accuracy.place(x=150, y=155)

    # Расчет всех корней
    Button(win, text="Рассчитать корни", font="15", command= lambda x=ent_accuracy: disp_info(x)).place(x=100, y=50)
    
    plot_graph(ent_left_border, ent_right_border)

    all_wid = [ent_accuracy]
    roots.widgets.extend(all_wid)
    Button(win, text="RESET", bg="red", command=rst).place(x=5, y=5)


def rst() -> None:
    values = ["1e-3"]
    for i in range(len(roots.widgets)):
        if "matplotlib.backends.backend_tkagg.FigureCanvasTkAgg" in str(roots.widgets[i]):
            roots.widgets[i].get_tk_widget().destroy()
        elif ".!frame" in str(roots.widgets[i]):
            roots.widgets[i].destroy()
        else:
            roots.widgets[i].delete(0, END)
            roots.widgets[i].insert(0, values[i])
        


if __name__ == "__main__":
    win = Tk()
    tkinter_fun()
    win.mainloop()
