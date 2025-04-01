import math as mt
import re

# import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

import sympy as sm
from sympy import symbols, Eq, solve, exp, sin, cos, tan, atan
from scipy.optimize import fsolve

import numpy as np

class RootFinder:
    def __init__(self):
        self.values = [None for _ in range(5)]
        self.widgets = []
        self.eps = 1e-6
        self.max_iter = 300
        self.left_border = 0
        self.right_border = 1
        self.initial_guess = 0.2
        self.function = "exp(-2*x) - 2*x + 1"
        # self.function = "tan(0.5 * x + 0.2) - x**2"
        # self.function = "x**2 + 4*sin(x)"
        # self.function = "atan(x) + 1/3 * x**3"
        # self.function = "1.8 * x**2 - sin(10*x)"
        # self.function = "x - log(x) - 5"
        # self.function = "3**(x-1) + 4 - x"
        # self.function = "tan(0.5 * x + 0.2) - x**2"
        # self.function = "tan(0.5 * x + 0.2) - x**2"
        # self.function = "tan(0.5 * x + 0.2) - x**2"

        self.x0 = (abs(self.left_border) + self.right_border) / 2
        self.replacement = ["cos", "sin", "exp", "log", "tan", "atan"]
    

    def func_x(self, x):
        fun = self.function
        for i in self.replacement:
            if i != 'tan' and i != 'atan':
                fun = fun.replace(i, "mt."+i)
        fun = re.sub(r'\batan\b|\btan\b', lambda match: 'mt.' + match.group(), fun)
        
        try:
            res = eval(fun)
        except ValueError:
            res = -1

        return res


    # Метод дихотомии
    def __dichotomy(self):
        a = self.left_border
        b = self.right_border
        counter = 0
        x = (a + b) / 2
        while abs(self.func_x(x)) > self.eps:
            counter += 1
            if self.func_x(x) * self.func_x(a) < 0:
                b = x
            else:
                a = x
            x = (a + b) / 2
            if counter >= self.max_iter:
                self.values[0] = f'Превышено максимальное кол-во итераций {self.max_iter}'
                return
    
        self.values[0] = (x, counter)


    # Метод хорд
    def __chord_method(self):
        a = self.left_border
        b = self.right_border
        counter = 0
        while True:
            counter += 1
            m = (self.func_x(b) * a 
                 - self.func_x(a) * b) / (self.func_x(b) - self.func_x(a))
            if abs(self.func_x(m)) < self.eps:
                break
            elif self.func_x(a) * self.func_x(m) < 0:
                b = m
            else:
                a = m
            if counter >= self.max_iter:
                self.values[1] = f'Превышено максимальное кол-во итераций {self.max_iter}'
                return
        
        self.values[1] = (m, counter)


    # Метод Ньютона (метод касательных)
    def __newton_raphson(self):
        def df(xx):
            fun = self.function
            for i in self.replacement:
                if i != 'tan' and i != 'atan':
                    fun = fun.replace(i, "sm."+i)
            fun = re.sub(r'\batan\b|\btan\b', lambda match: 'sm.' + match.group(), fun)

            x = sm.symbols('x')
            res = sm.diff(eval(fun))

            for i in self.replacement:
                if i != 'tan' and i != 'atan':
                    res = str(res).replace(i, "mt."+i)
            res = re.sub(r'\batan\b|\btan\b', lambda match: 'mt.' + match.group(), res)

            x = xx
            res = eval(res)

            return res
        
        x0 = self.initial_guess
        counter = 0
        while True:
            counter += 1
            x1 = x0 - self.func_x(x0) / df(x0)
            if abs(x1 - x0) < self.eps:
                break
            x0 = x1
            if counter >= self.max_iter:
                self.values[2] = f'Превышено максимальное кол-во итераций {self.max_iter}'
                return
            
        self.values[2] = (x1, counter)


    # Метод простых итераций
    def __simple_iteration(self):

        def __replacment_finder() -> list:
                    reps = ""
                    rev_reps = []
                    for rep in self.replacement:
                        for s in range(len(self.function)-1):
                            if self.function[s] == rep[0] and self.function[s + 1] == rep[1]:
                                if rep == "tan":
                                    cond1 = False
                                    if s == 0:
                                        cond1 = True
                                    elif self.function[s-1] != "a":
                                        cond1 = True
                                else:
                                    cond1 = True

                                if cond1:
                                    # Поиск функции c аргументом для замены
                                    counter_brackets = 0
                                    while len(self.function) >= s:
                                        reps += self.function[s]

                                        if self.function[s] == '(':
                                            counter_brackets += 1
                                        elif self.function[s] == ')':
                                            counter_brackets -= 1

                                        if self.function[s] == ')' and counter_brackets == 0:
                                            reps += ';'                                      
                                            break
                                        s += 1
                                    rev_reps.append(rep)
                    
                    return reps.split(";")[:-1], rev_reps   

        def equation(x):
            return eval(self.function_rep)

        # def g(xx):

            fun = self.function
            # for i in self.replacement:
            #     pat = i+'\\([^)]*\\)'
            #     fun = re.sub(fr"{pat}", '', fun)
            for i in self.replacement:
                fun = fun.replace(i, "sm."+i)
            fun = re.sub(r'\batan\b|\btan\b', lambda match: 'sm.' + match.group(), fun)

            x = sm.symbols('x') 
            eq = sm.Eq(eval(fun), 0)
            print(eq)
            solution = sm.solve(eq, x)
            print(solution)
            g_x = solution[0]
            x = xx
            reps = ['( ' + "mt." + i + ' )'for i in replacment_finder()]
            print(g_x, reps)
            equation = ''
            for i in reps:
                equation += i
            print(equation)
            g_x = eval(equation + '*' + str(g_x))
            print(g_x, xx)


            '''''''''
            fun = self.function
            for i in self.replacement:
                fun = fun.replace(i, "np."+i)
            fun = re.sub(r'\batan\b|\btan\b', lambda match: 'np.' + match.group(), fun)

            self.function_rep = fun
            solution = fsolve(equation, -1) # Второе значение - начало поиска корней
            print(solution)
            return solution
            '''

        def __variable_expression(xx) -> str:


            def __expression_error() -> str:
                return 'Нельзя выразить x в данном уравнении'
            

            def __expression_x() -> str:
                    val = self.function

                    reps, rev_reps = __replacment_finder()
                    for i in range(len(reps)):
                        val = val.replace(reps[i], f"{rev_reps[i]}(y + {i + 1})")

                    x = symbols('x')
                    y = symbols('y')

                    eq = Eq(eval(val), 0)
                    solution = solve(eq, x)
                    g_x = str(solution[0])

                    for i in range(len(reps)):
                        g_x = g_x.replace(f"{rev_reps[i]}(y + {i + 1})", reps[i])
                        g_x = g_x.replace(f"{rev_reps[i]}(y + {i + 1.0})", reps[i])

                    return g_x


            def __expression_func_x() -> str:
                try:
                    x = symbols('x')
                    eq = Eq(eval(self.function), 0)
                    solution = solve(eq, x)
                    g_x = str(solution[0])
                except NotImplementedError:
                    return __expression_error()

                return g_x

            
            val_rep = self.function
            for i in self.replacement:
                        pat = i+'\\([^)]*\\)'
                        val_rep = re.sub(fr"{pat}", '', val_rep)
            val_rep = re.sub(r'\batan\b|\btan\b', lambda match: match.group(), val_rep)
                
            if 'x' in val_rep:
                    res = __expression_x()
            elif 'x' not in self.function:
                    res = __expression_error()
            else:
                    res = __expression_func_x()


            x = xx
            reps = __replacment_finder()[0]
            reps_mt = ["mt." + i for i in reps]
            equation = res
            for i in range(len(reps)):
                equation = equation.replace(reps[i], reps_mt[i])
            equation = equation.replace("sqrt", "mt.sqrt")

            try:
                res = eval(equation)
            except ValueError:
                res = 0
            except TypeError:
                res = 0


            return res
            #   !!!
            #  !!!
            # !!!

        x0 = 1
        counter = 0
        while True:
            counter += 1
            x1 = __variable_expression(x0)
            if abs(x1 - x0) < self.eps:
                break
            x0 = x1
            if counter >= self.max_iter:
                self.values[3] = f'Превышено максимальное кол-во итераций {self.max_iter}'
                return
            
        self.values[3] = (x1, counter)


    # Scipy
    def __scipy_method(self):
        initial_guess = self.initial_guess
        root = fsolve(self.func_x, initial_guess)[0]
        fun_value = self.func_x(root)
        
        self.values[4] = (float(root), None)


    def get_roots(self):
        self.__dichotomy()
        self.__chord_method()
        self.__newton_raphson()
        self.__simple_iteration()
        self.__scipy_method()
        return self.values

roots = RootFinder()


def error(er='Ошибка'):
    er_win = Toplevel(win)
    er_win.title("Ошибка")
    er_win.geometry("350x150")
    Label(er_win, text=er, font="30", bg="red").pack()

# Добавить поля для ввода границ построения графика,  поле для шага
# Универсальность для разных графиков
def plot_graph(ent_eq, ent_left, ent_right) -> None:

    equation = ent_eq.get()
    try:
        left_border = float(ent_left.get())
        right_border = float(ent_right.get())
    except ValueError:
        return error("Введите численные значениия\n в границах")
    roots.function = equation
    roots.left_border = left_border
    roots.right_border = right_border
    
    step = 0.001
    x = [i * step for i in range(int(left_border/step), int(right_border/step+1))]
    y = [roots.func_x(i) for i in x]
    # plt.plot(x, y)
    # plt.show()


    fig = Figure(figsize=(4, 4), facecolor='peachpuff')
    ax = fig.add_subplot(facecolor='bisque')   
    ax.scatter(x, y, s=1)
    ax.axis('on')
    ax.axhline(y=0, color='r', linestyle='-', linewidth=1)
    fig.patch.set_edgecolor('whitesmoke')
    fig.patch.set_linewidth(2) 

    canvas1 = FigureCanvasTkAgg(fig, master = win)
    canvas1.draw()
    canvas1.get_tk_widget().place(x=0, y=300)
    roots.widgets.append(canvas1)

    
def disp_info(ent_accur, ent_iter, ent_scipy) -> None:
    try:
        accuracity = float(ent_accur.get())
        itterations = int(ent_iter.get())
        scipy_accur = float(ent_scipy.get())
    except ValueError:
        return error("Введите численные значениия\n в границах")
    roots.eps = accuracity
    roots.initial_guess = scipy_accur
    roots.max_iter = itterations

    values = roots.get_roots()
    names_methods = ["Дихотомии", "Хорд", "Касательных", "Итераций", "Scipy"]
    names_up = ["Методы вычисления", "Значение корна", "Кол-во итераций"]
    table_frame = Frame(master=win, bg="peachpuff")
    table_frame.place(x=700, y=250)
    roots.widgets.append(table_frame)

    for i in range(len(names_up)):
        cell = Label(table_frame, text=f"{names_up[i]}", bg="peachpuff", font="15" )
        cell.grid(row=0, column=i, padx=20)

    for i in range(len(names_methods)):
        cell = Label(table_frame, text=f"{names_methods[i]}", bg="peachpuff", font="15" )
        cell.grid(row=i+1, column=0, padx=20, pady=20)
        for j in range(len(values[i])):
            if "П" in str(values[i][0]):
                text = f"Превышено максимальное\nкол-во итераций {roots.max_iter}\nв " + names_methods[i]
                error(text)
                cell = Label(table_frame, text=f"Ошибка", bg="peachpuff", font="15" )
                cell.grid(row=i+1, column=j+1, padx=20)
                break
            elif names_methods[i] == "Scipy" and j == 1:
                cell = Label(table_frame, text=f"{values[2][1]}", bg="peachpuff", font="15" )
                cell.grid(row=i+1, column=j+1, padx=20)
            else:
                cell = Label(table_frame, text=f"{values[i][j]}", bg="peachpuff", font="15" )
                cell.grid(row=i+1, column=j+1, padx=20)


def tkinter_fun() -> None:
    
    win.title("Лабораторная работа №1 Вершинин АТ-24-01")
    win.state('zoomed')
    win.resizable(0, 0)
    win.attributes("-alpha", 0.96)
    win.config(bg="bisque")
    Label(text="Вершинин Сергей АТ-24-01\nВариант №3", font="30", bg="bisque").place(x=70, y=740)

    Canvas(bg="peachpuff", width=395, height=300).place(x=1, y=1)
    Canvas(bg="bisque2", width=275, height=170).place(x=398, y=1)
    Canvas(bg="bisque2", width=226, height=70).place(x=170, y=1)


    # Границы
    Label(text="Границы", font="15", bg="peachpuff").place(x=23, y=105)
    ent_left_border = Entry(win, textvariable=StringVar(value=0), width=5, justify=CENTER)
    ent_left_border.place(x=25, y=135)
    ent_right_border = Entry(win, textvariable=StringVar(value=1), width=5, justify=CENTER)
    ent_right_border.place(x=65, y=135)

    # Уравнение
    Label(text="Уравнение", font="15", bg="bisque2").place(x=230, y=5)
    ent_equation = Entry(win, textvariable=StringVar(value="exp(-2*x) - 2*x + 1"), width=30, justify=CENTER)
    ent_equation.place(x=190, y=40)

    Radiobutton(win, textvariable=StringVar(value="tan(0.5 * x + 0.2) - x**2"), bg="bisque2", font="15",
                command=lambda: [ent_equation.delete(0, END), ent_equation.insert(0, "tan(0.5 * x + 0.2) - x**2")]).place(x=420, y=10)
    Radiobutton(win, textvariable=StringVar(value="x**2 + 4*sin(x)"), bg="bisque2", font="15",
                command=lambda: [ent_equation.delete(0, END), ent_equation.insert(0, "x**2 + 4*sin(x)")]).place(x=420, y=10)
    Radiobutton(win, textvariable=StringVar(value="atan(x) + 1/3 * x**3"), bg="bisque2", font="15",
                command=lambda: [ent_equation.delete(0, END), ent_equation.insert(0, "atan(x) + 1/3 * x**3")]).place(x=420, y=50)
    Radiobutton(win, textvariable=StringVar(value="1.8 * x**2 - sin(10*x)"), bg="bisque2", font="15",
                command=lambda: [ent_equation.delete(0, END), ent_equation.insert(0, "1.8 * x**2 - sin(10*x)")]).place(x=420, y=90)
    Radiobutton(win, textvariable=StringVar(value="exp(-2*x) - 2*x + 1"), bg="bisque2", font="15",
                command=lambda: [ent_equation.delete(0, END), ent_equation.insert(0, "exp(-2*x) - 2*x + 1")]).place(x=420, y=130)
    
    Button(win, text="Построить\nграфик", command=lambda x=ent_equation,
                                                         y=ent_left_border,
                                                         z=ent_right_border: plot_graph(x, y, z)).place(x=70, y=13)
    
    # Точность, итерации, scipy
    Label(text="Точность", font="15", bg="peachpuff").place(x=115, y=105)
    ent_accuracy = Entry(win, textvariable=StringVar(value="1e-6"), width=9, justify=CENTER)
    ent_accuracy.place(x=130, y=135)
    Label(text="Кол-во итераций", font="15", bg="peachpuff").place(x=220, y=105)
    ent_iter = Entry(win, textvariable=StringVar(value="300"), width=15, justify=CENTER)
    ent_iter.place(x=250, y=135)
    Label(text="Приближение\nscipy", font="15", bg="peachpuff").place(x=25, y=180)
    ent_accuracy_scipy = Entry(win, textvariable=StringVar(value="0.2"), width=9, justify=CENTER)
    ent_accuracy_scipy.place(x=60, y=235)

    # Расчет всех корней
    Button(win, text="Рассчитать корни", font="15", command= lambda x=ent_accuracy,
                                                                    y=ent_iter,
                                                                    z=ent_accuracy_scipy: disp_info(x, y, z)).place(x=185, y=220)
    
    all_wid = [ent_left_border, ent_right_border, ent_equation, ent_accuracy, ent_iter, ent_accuracy_scipy]
    roots.widgets.extend(all_wid)
    Button(win, text="RESET", bg="red", command=rst).place(x=5, y=5)


def rst() -> None:
    values = ['0', '1', "exp(-2*x) - 2*x + 1", "1e-6", "300", "0.2"]
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
