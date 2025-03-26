import math as mt
import re

from tkinter import *

import sympy as sm
from sympy import symbols, Eq, solve, exp, sin, cos, tan, atan
from scipy.optimize import fsolve

import numpy as np

class RootFinder:
    def __init__(self):
        self.values = [None for _ in range(4)]
        self.eps = 1e-6
        self.max_iter = 300
        self.left_border = -5
        self.right_border = 1
        self.function = "exp(-2*x) - 2*x + 1"
        # self.function = "tan(0.5 * x + 0.2) - x**2"
        # self.function = "x**2 + 4*sin(x)"
        # self.function = "atan(x) + 1/3 * x**3"
        # self.function = "1.8 * x**2 - sin(10*x)"
        # self.function = "x - log(x) - 5"
        self.function = "3**(x-1) + 4 - x"
        # self.function = "tan(0.5 * x + 0.2) - x**2"
        # self.function = "tan(0.5 * x + 0.2) - x**2"
        # self.function = "tan(0.5 * x + 0.2) - x**2"

        self.x0 = -2
        self.replacement = ["cos", "sin", "exp", "log", "tan", "atan"]
    

    def __f(self, x):
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
        while abs(self.__f(x)) > self.eps:
            counter += 1
            if self.__f(x) * self.__f(a) < 0:
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
            m = (self.__f(b) * a 
                 - self.__f(a) * b) / (self.__f(b) - self.__f(a))
            if abs(self.__f(m)) < self.eps:
                break
            elif self.__f(a) * self.__f(m) < 0:
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
        
        x0 = self.x0
        counter = 0
        while True:
            counter += 1
            x1 = x0 - self.__f(x0) / df(x0)
            if abs(x1 - x0) < self.eps:
                break
            x0 = x1
            if counter >= self.max_iter:
                self.values[2] = f'Превышено максимальное кол-во итераций {self.max_iter}'
                return
            
        self.values[2] = (x1, counter)


    # Метод простых итераций
    def __simple_iteration(self):

        def __replacment_finder():
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
        pass
        

    def get_roots(self):
        self.__dichotomy()
        # self.__chord_method()
        self.__newton_raphson()
        self.__simple_iteration()
        return self.values

a = RootFinder()
print(a.get_roots())


def start() -> None:
    global GLOBAL_NAMES

    win.title("Лабораторная работа №1 Вершинин АТ-24-01")
    win.geometry("1350x750")
    win.resizable(0, 0)
    win.attributes("-alpha", 0.96)
    Label(text="Вершинин Сергей АТ-24-01\nВариант №3").pack()
    ent1 = Entry(win, textvariable=StringVar(value=0), width=5)
    ent1.place(x=100, y=100)
    ent2 = Entry(win, textvariable=StringVar(value=1), width=5)
    ent2.place(x=120, y=100)


    GLOBAL_NAMES = [ent1, ent2, ent3, ent4]
    btn1 = Button(win, text="RESET", command=lambda x=GLOBA_NAMES: rst(x))
    btn1.place(x=10, y=10)




def rst(x) -> None:
    for i in x:
        pass



# if __name__ == "__main__":
#     win = Tk()
#     start()
#     win.mainloop()
