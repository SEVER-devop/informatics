import math as mt
import re
from tkinter import *
import sympy as sm

class RootFinder:
    def __init__(self):
        self.values = [None for _ in range(4)]
        self.eps = 1e-6
        self.max_iter = 30000
        self.left_border = -5
        self.right_border = 1
        self.function = "exp(-2*x) - 2*x + 1"
        self.replacement = ["cos", "sin", "exp", "tg", "arctg", "ln"]
        # result = re.sub(r'cos$([^)]+)$', '1', s)
        self.x0 = -2
    

    def f(self, x):
        fun = self.function
        for i in self.replacement:
            fun = fun.replace(i, "mt."+i)
        return eval(fun)


    # Метод дихотомии
    def __dichotomy(self):
        a = self.left_border
        b = self.right_border
        counter = 0
        x = (a + b) / 2
        while abs(self.f(x)) > self.eps:
            counter += 1
            if self.f(x) * self.f(a) < 0:
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
            m = (self.f(b) * a 
                 - self.f(a) * b) / (self.f(b) - self.f(a))
            if abs(self.f(m)) < self.eps:
                break
            elif self.f(a) * self.f(m) < 0:
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
                fun = fun.replace(i, "sm."+i)
            x = sm.symbols('x')
            res = sm.diff(eval(fun))
            x = xx
            res = eval(str(res).replace("exp", "mt.exp"))
            return res
        
        x0 = self.x0
        counter = 0
        while True:
            counter += 1
            x1 = x0 - self.f(x0) / df(x0)
            if abs(x1 - x0) < self.eps:
                break
            x0 = x1
            if counter >= self.max_iter:
                self.values[2] = f'Превышено максимальное кол-во итераций {self.max_iter}'
                return
            
        self.values[2] = (x1, counter)


    # Метод простых итераций
    def __simple_iteration(self):
        def g(xx):
            fun = self.function
            for i in self.replacement:
                pat = i+'\\([^)]*\\)'
                fun = re.sub(fr"{pat}", '', fun)
            x = sm.symbols('x')
            eq = sm.Eq(eval(fun), 0)
            solution = sm.solve(eq, x)
            g_x = solution[0]
            x = xx
            g_x = eval('(mt.exp(-2*x) + 1) * ' + str(g_x))
            return g_x


        x0 = 1
        counter = 0
        while True:
            counter += 1
            x1 = g(x0)
            if abs(x1 - x0) < self.eps:
                break
            x0 = x1
            if counter >= self.max_iter:
                self.values[3] = f'Превышено максимальное кол-во итераций {self.max_iter}'
                return
            
        self.values[3] = (x1, counter)


    def get_roots(self):
        self.__dichotomy()
        self.__chord_method()
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
