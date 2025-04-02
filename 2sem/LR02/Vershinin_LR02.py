import math as mt
import re

# import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

from sympy import symbols, sin, cos, Eq, nsolve, solve, sqrt
from scipy.optimize import fsolve

import numpy as np

class RootFinder:
    def __init__(self):
        self.values = [(None, None, None) for _ in range(5)]
        self.widgets = []
        self.eps = 1e-3
        self.max_iter = 1000
        self.initial_guess = -1.0
        self.left_border = -5
        self.right_border = 5


    def __f1(self, x, y):
        return np.sin(x - y) - x*y + 1

    def __f2(self, x, y):
        return x**2 - y**2 - 0.75

    def __jacobian(self, x, y):
        f1_dx = np.cos(x - y) - y
        f1_dy = -np.cos(x - y) - x
        f2_dx = 2*x
        f2_dy = -2*y
        return np.array([[f1_dx, f1_dy], [f2_dx, f2_dy]])

    def __jacobi_method(self):
        x, y = self.initial_guess, 0.0

        for iter_counter in range(self.max_iter):
            x_old, y_old = x, y
            
            if x_old >= 0:
                x = np.sqrt(y_old**2 + 0.75)
            else:
                x = -np.sqrt(y_old**2 + 0.75)
                
            y = (np.sin(x_old - y_old) + 1)/x_old if x_old != 0 else y_old
            
            if abs(x - x_old) < self.eps and abs(y - y_old) < self.eps:
                break
                
        self.values[0] = (x, y, iter_counter)


    def __gauss_seidel_method(self):
        x, y = self.initial_guess, 0
        
        for iter_couter in range(self.max_iter):
            x_old, y_old = x, y
            
            if x >= 0:
                x = np.sqrt(y**2 + 0.75)
            else:
                x = -np.sqrt(y**2 + 0.75)
                
            y = (np.sin(x - y_old) + 1)/x if x != 0 else y_old
            
            if abs(x - x_old) < self.eps and abs(y - y_old) < self.eps:
                break
        
        self.values[1] = (x, y, iter_couter)


    def __newton_method(self):
        x, y = self.initial_guess, 0
        
        for iter_counter in range(self.max_iter):
            F = np.array([self.__f1(x, y), self.__f2(x, y)])
            J = self.__jacobian(x, y)
            
            try:
                delta = np.linalg.solve(J, -F)
            except np.linalg.LinAlgError:
                break
                
            x += delta[0]
            y += delta[1]
            
            if np.linalg.norm(delta) < self.eps:
                break
        
        self.values[2] = (x, y, iter_counter)


    def __sympy_method(self):
        x, y = symbols('x y')

        eq1 = Eq(sin(x - y) - x*y, -1)
        eq2 = Eq(x**2 - y**2, 0.75)


        res = nsolve([eq1, eq2], [x, y], [self.initial_guess, 0])
        
        self.values[3] = (res[0], res[1], None)



    def get_roots(self):
        self.__jacobi_method()
        self.__gauss_seidel_method()
        self.__newton_method()
        self.__sympy_method()
        return self.values




roots = RootFinder()


def error(er='Ошибка'):
    er_win = Toplevel(win)
    er_win.title("Ошибка")
    er_win.geometry("350x150")
    Label(er_win, text=er, font="30", bg="red").pack()


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

    graph_1 = np.sin(X - Y) - X*Y
    graph_2 = X**2 - Y**2 - 0.75

    fig = Figure(figsize=(4, 4), facecolor='peachpuff')
    ax = fig.add_subplot(facecolor='bisque')

    ax.contour(X, Y, graph_1, levels=[-1], colors='r', linestyles='solid')
    ax.contour(X, Y, graph_2, levels=[0], colors='b', linestyles='solid')

    ax.axhline(y=0, color='gray', linestyle='-', linewidth=1)
    fig.patch.set_edgecolor('whitesmoke')
    fig.patch.set_linewidth(2) 

    canvas1 = FigureCanvasTkAgg(fig, master = win)
    canvas1.draw()
    canvas1.get_tk_widget().place(x=0, y=300)
    roots.widgets.append(canvas1)

    
def disp_info(ent_accur, ent_iter, ent_init_guess) -> None:
    try:
        iter = int(ent_iter.get())
        accuracity = float(ent_accur.get())
        init_guess = float(ent_init_guess.get())
    except ValueError:
        return error("Введите численные значениия\n в границах")
    roots.eps = accuracity
    roots.max_iter = iter
    roots.initial_guess = init_guess

    values = roots.get_roots()
    names_methods = ["Якоби", "Гаусс", "Ньютон", "Sympy"]
    names_up = ["Методы вычисления", "Значение x", "Значение y", "Кол-во итераций"]
    table_frame = Frame(master=win, bg="peachpuff")
    table_frame.place(x=500, y=250)
    roots.widgets.append(table_frame)

    for i in range(len(names_up)):
        cell = Label(table_frame, text=f"{names_up[i]}", bg="peachpuff", font="15" )
        cell.grid(row=0, column=i, padx=20)

    for i in range(len(names_methods)):
        cell = Label(table_frame, text=f"{names_methods[i]}", bg="peachpuff", font="15" )
        cell.grid(row=i+1, column=0, padx=20, pady=20)
        for j in range(len(values[i])):
            cell = Label(table_frame, text=f"{values[i][j]}", bg="peachpuff", font="15" )
            cell.grid(row=i+1, column=j+1, padx=20)


def tkinter_fun() -> None:
    
    win.title("Лабораторная работа №2 Вершинин АТ-24-01")
    win.state('zoomed')
    win.resizable(0, 0)
    win.attributes("-alpha", 0.96)
    win.config(bg="bisque")
    Label(text="Вершинин Сергей АТ-24-01\nВариант №3", font="30", bg="bisque").place(x=70, y=740)

    Canvas(bg="peachpuff", width=395, height=300).place(x=1, y=1)
    # Canvas(bg="bisque2", width=275, height=170).place(x=398, y=1)
    Canvas(bg="bisque2", width=226, height=100).place(x=170, y=1)


    # Границы
    Label(text="Границы", font="15", bg="peachpuff").place(x=23, y=105)
    ent_left_border = Entry(win, textvariable=StringVar(value=-5), width=5, justify=CENTER)
    ent_left_border.place(x=25, y=135)
    ent_right_border = Entry(win, textvariable=StringVar(value=5), width=5, justify=CENTER)
    ent_right_border.place(x=65, y=135)

    # Уравнение
    Label(text="Уравнения", font="15", bg="bisque2").place(x=235, y=5)
    Label(text="x^2 - y^2 = 0.75", font="15", bg="bisque2").place(x=225, y=35)
    Label(text="sin(x-y) - x*y = -1", font="15", bg="bisque2").place(x=225, y=65)
    Label(text="\u007B", font=("calibri light", 40), bg="bisque2").place(x=200, y=23)

    Button(win, text="Построить\nграфик", font="15", bg="bisque2", command=lambda y=ent_left_border,
                                                         z=ent_right_border: plot_graph(y, z)).place(x=50, y=30)
    
    # Точность, итерации, scipy
    Label(text="Точность", font="15", bg="peachpuff").place(x=115, y=105)
    ent_accuracy = Entry(win, textvariable=StringVar(value="1e-3"), width=9, justify=CENTER)
    ent_accuracy.place(x=130, y=135)
    Label(text="Кол-во итераций", font="15", bg="peachpuff").place(x=220, y=105)
    ent_iter = Entry(win, textvariable=StringVar(value="1000"), width=15, justify=CENTER)
    ent_iter.place(x=250, y=135)
    Label(text="Приближение\n по x", font="15", bg="peachpuff").place(x=25, y=180)
    ent_accuracy_scipy = Entry(win, textvariable=StringVar(value="1"), width=9, justify=CENTER)
    ent_accuracy_scipy.place(x=60, y=235)

    # Расчет всех корней
    Button(win, text="Рассчитать корни", font="15", command= lambda x=ent_accuracy,
                                                                    y=ent_iter,
                                                                    z=ent_accuracy_scipy: disp_info(x, y, z)).place(x=185, y=220)
    
    all_wid = [ent_left_border, ent_right_border, ent_accuracy, ent_iter, ent_accuracy_scipy]
    roots.widgets.extend(all_wid)
    Button(win, text="RESET", bg="red", command=rst).place(x=5, y=5)


def rst() -> None:
    values = ['-5', '5', "1e-3", "1000", "1"]
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
