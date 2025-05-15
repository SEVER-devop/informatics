import math as mt

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk

import numpy as np


'''Классы для нахождения и отображения корней'''
class SolverCauchyFirstOrder:
    def __init__(self, win_frame) -> None:
        self.win_frame = win_frame
        self.fun = "(x + 1) * np.exp((- np.sin(x)))"
        self.name = 'First'
        self.values = []
        self.tk_val = ["-5", "5"]

        self.n = 10
        self.widgets = []
        self.left_border = -5
        self.right_border = 5
        self.x0 = 0
        self.y0 = 1
        self.x_end = 1
        self.h = 0.1
        self.n = int((self.x_end - self.x0) / self.h) + 1


        self.names_methods = ["Метод Адамса", "Метод Эйлера", "Метод Рунге-Кутта", "Точное значение"]
        self.names_up = ["Методы", "y(0.0)", "y(0.1)", "y(0.2)", "y(0.3)", "y(0.4)", "y(0.5)", "y(0.6)", "y(0.7)", "y(0.8)", "y(0.9)", "y(1.0)"]
        
        self.__tkinter_fun_scfo()
        plot_graph(self)
        

    def __tkinter_fun_scfo(self) -> None:
        
        Button(self.win_frame, text="RESET", bg="red", command= lambda: rst(self)).place(x=5, y=5)
        Label(self.win_frame, text="Задание 1: Задача Коши дифура первого порядка", font="14", bg='bisque').place(x=30, y=65)
        Label(self.win_frame, text="y'+ y * cos(x) = exp(-sin(x))", font="14", bg='bisque').place(x=100, y=100)
        Label(self.win_frame, text="Левая граница:", font= "14", bg='bisque').place(x=30, y=140)
        entry_a = Entry(self.win_frame, textvariable=StringVar(value=-5), justify=CENTER)
        entry_a.place(x=230, y=145, width=100)

        Label(self.win_frame, text="Правая граница:", font="14", bg='bisque').place(x=30, y=170)
        entry_b = Entry(self.win_frame, textvariable=StringVar(value=5), justify=CENTER)
        entry_b.place(x=230, y=175, width=100)

        Button(self.win_frame, text="Найти корни", font="14", bg='bisque2', command=lambda: disp_info(self, 0, 700)).place(x=30, y=220)
        Button(self.win_frame, text="Построить график", font="10", bg='bisque2', command=lambda: plot_graph(self)).place(x=180, y=220)


        self.widgets.append(entry_a)
        self.widgets.extend([entry_b])


    def __f(self, x, y) -> int:
        return -y * mt.cos(x) + mt.exp(-mt.sin(x))

    def __exact_solution(self, x) -> int:
        return (x + 1) * mt.exp(-mt.sin(x))


    # Метод Эйлера
    def __euler_method(self) -> list:
        x = [self.x0 + i * self.h for i in range(self.n)]
        y = [0.0] * self.n
        y[0] = self.y0
        
        for i in range(self.n-1):
            y[i+1] = y[i] + self.h * self.__f(x[i], y[i])
        
        return x, y

    # Метод Рунге-Кутта 4-го порядка
    def __runge_kutta(self) -> list:
        h = self.h
        x = [self.x0 + i * h for i in range(self.n)]
        y = [0.0] * self.n
        y[0] = self.y0
        
        for i in range(self.n-1):
            k1 = h * self.__f(x[i], y[i])
            k2 = h * self.__f(x[i] + h/2, y[i] + k1/2)
            k3 = h * self.__f(x[i] + h/2, y[i] + k2/2)
            k4 = h * self.__f(x[i] + h, y[i] + k3)
            
            y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        
        return x, y

    # Метод Адамса
    def __adams_method(self) -> list:
        x = [self.x0 + i * self.h for i in range(self.n)]
        y = [0.0] * self.n
        
        _ , y_rk = self.__runge_kutta()
        for i in range(4):
            y[i] = y_rk[i]
        
        for i in range(3, self.n-1):
            y[i+1] = y[i] + self.h * (55*self.__f(x[i], y[i]) - 59*self.__f(x[i-1], y[i-1]) + 
                                37*self.__f(x[i-2], y[i-2]) - 9*self.__f(x[i-3], y[i-3])) / 24
        
        return x, y
    
    def __exact_method(self) -> list:
        res = [self.__exact_solution(i) for i in self.__euler_method()[0]]

        return res


    def get_roots(self) -> None:
        try:
            self.left_border = float(self.widgets[0].get())
            self.right_border = float(self.widgets[1].get())
        except Exception as e:
            return error(e)
        
        self.values = [[round(i, 7) for i in self.__adams_method()[1]], 
                       [round(i, 7) for i in self.__euler_method()[1]], 
                       [round(i, 7) for i in self.__runge_kutta()[1]],
                       [round(i, 7) for i in self.__exact_method()]]

        
class SolverCauchySysFirstOrder:
    def __init__(self, win_frame) -> None:
        self.win_frame = win_frame
        self.fun = "0"
        self.name = 'Second'
        self.values = []
        self.values_dop = []
        self.tk_val = ["-5", "5"]

        self.n = 10
        self.widgets = []
        self.left_border = -5
        self.right_border = 5
        self.x0 = 0
        self.y10 = self.__exact_y1(self.x0)
        self.y20 = self.__exact_y2(self.x0)
        self.x_end = 1
        self.h = 0.1
        self.n = int((self.x_end - self.x0)/self.h) + 1


        self.names_methods = ["Метод Адамса", "Метод Эйлера", "Метод Рунге-Кутта", "Точное значение"]
        self.names_up = ["Методы", "y1(0.0)", "y1(0.1)", "y1(0.2)", "y1(0.3)", "y1(0.4)", "y1(0.5)", "y1(0.6)", "y1(0.7)", "y1(0.8)", "y1(0.9)", "y1(1.0)"]
        self.names_up_dop = ["Методы", "y2(0.0)", "y2(0.1)", "y2(0.2)", "y2(0.3)", "y2(0.4)", "y2(0.5)", "y2(0.6)", "y2(0.7)", "y2(0.8)", "y2(0.9)", "y2(1.0)"]
        
        self.__tkinter_fun_scsfo()
        

    def __tkinter_fun_scsfo(self) -> None:
        Button(self.win_frame, text="RESET", bg="red", command= lambda: rst(self)).place(x=5, y=5)
        
        Label(self.win_frame, text="y'1 = -y1 + 8*y2", font="15", bg="bisque").place(x=50, y=80)
        Label(self.win_frame, text="y'2 = y1 + y2", font="15", bg="bisque").place(x=50, y=110)
        Label(self.win_frame, text="\u007B", font=("calibri light", 40), bg="bisque").place(x=25, y=70)
        Label(self.win_frame, text="Задание 2: Задача Коши сист диф. ур-ий первого порядка", font="14", bg='bisque').place(x=30, y=50)

        Label(self.win_frame, text="Левая граница:", font= "14", bg='bisque').place(x=30, y=140)
        entry_a = Entry(self.win_frame, textvariable=StringVar(value=2), justify=CENTER)
        entry_a.place(x=230, y=145, width=100)

        Label(self.win_frame, text="Правая граница:", font="14", bg='bisque').place(x=30, y=170)
        entry_b = Entry(self.win_frame, textvariable=StringVar(value=3), justify=CENTER)
        entry_b.place(x=230, y=175, width=100)

        Button(self.win_frame, text="Найти корни", font="14", bg='bisque2', command=lambda: disp_info(self, 450, 200)).place(x=30, y=220)
        Button(self.win_frame, text="Построить график", font="10", bg='bisque2', command=lambda: self.__plot_graph_scsfo()).place(x=180, y=220)


        self.widgets.append(entry_a)
        self.widgets.extend([entry_b])
      
    def __plot_graph_scsfo(self) -> None:
        try:
            x_euler, y1_euler, y2_euler = self.__euler_method()
            x_rk, y1_rk, y2_rk = self.__runge_kutta()
            
            fig1 = Figure(figsize=(4, 4), facecolor='peachpuff')
            ax1 = fig1.add_subplot(facecolor='bisque')
            
            fig2 = Figure(figsize=(4, 4), facecolor='peachpuff')
            ax2 = fig2.add_subplot(facecolor='bisque')

            # Точные решения для отрисовки
            x_exact = np.linspace(self.x0, self.x_end, 100)
            y1_exact = [self.__exact_y1(x) for x in x_exact]
            y2_exact = [self.__exact_y2(x) for x in x_exact]

            ax1.plot(x_exact, y1_exact, 'k-', linewidth=2, label='Точное')
            ax1.plot(x_euler, y1_euler, 'b--o', markersize=4, linewidth=1, label='Эйлер')
            ax1.plot(x_rk, y1_rk, 'g--s', markersize=4, linewidth=1, label='Рунге-Кутта')
            
            ax2.plot(x_exact, y2_exact, 'k-', linewidth=2, label='Точное')
            ax2.plot(x_euler, y2_euler, 'b--o', markersize=4, linewidth=1, label='Эйлер')
            ax2.plot(x_rk, y2_rk, 'g--s', markersize=4, linewidth=1, label='Рунге-Кутта')

            for ax in [ax1, ax2]:
                ax.axhline(y=0, color='gray', linestyle='-', linewidth=1)
                ax.axvline(x=0, color='gray', linestyle='-', linewidth=1)
                ax.legend()
                ax.grid(True)

            for fig in [fig1, fig2]:
                fig.patch.set_edgecolor('whitesmoke')
                fig.patch.set_linewidth(2)

            for widget in self.widgets[2:]:
                if isinstance(widget, FigureCanvasTkAgg):
                    widget.get_tk_widget().destroy()


            canvas2 = FigureCanvasTkAgg(fig2, master=self.win_frame)
            canvas2.draw()
            canvas2.get_tk_widget().place(x=-1, y=630)

            canvas1 = FigureCanvasTkAgg(fig1, master=self.win_frame)
            canvas1.draw()
            canvas1.get_tk_widget().place(x=-1, y=265)

            self.widgets = [*self.widgets[:2], canvas1, canvas2]

        except Exception as e:
            return error(e)
        

    # Определение системы уравнений
    def __f1(self, x, y1, y2):
        return -y1 + 8*y2

    def __f2(self, x, y1, y2):
        return y1 + y2

    # Точные решения
    def __exact_y1(self, x):
        return 2*mt.exp(3*x) - 4*mt.exp(-3*x)

    def __exact_y2(self, x):
        return mt.exp(3*x) + mt.exp(-3*x)


    # Метод Эйлера
    def __euler_method(self):
        x = [self.x0 + i*self.h for i in range(self.n)]
        y1 = [0.0]*self.n
        y2 = [0.0]*self.n
        y1[0] = self.y10
        y2[0] = self.y20
        
        for i in range(self.n-1):
            y1[i+1] = y1[i] + self.h * self.__f1(x[i], y1[i], y2[i])
            y2[i+1] = y2[i] + self.h * self.__f2(x[i], y1[i], y2[i])
        
        return x, y1, y2
    
    # Метод Рунге-Кутта 4-го порядка
    def __runge_kutta(self):
        h = self.h
        x = [self.x0 + i*h for i in range(self.n)]
        y1 = [0.0]*self.n
        y2 = [0.0]*self.n
        y1[0] = self.y10
        y2[0] = self.y20
        
        for i in range(self.n-1):
            k1_y1 = h * self.__f1(x[i], y1[i], y2[i])
            k1_y2 = h * self.__f2(x[i], y1[i], y2[i])
            
            k2_y1 = h * self.__f1(x[i] + h/2, y1[i] + k1_y1/2, y2[i] + k1_y2/2)
            k2_y2 = h * self.__f2(x[i] + h/2, y1[i] + k1_y1/2, y2[i] + k1_y2/2)
            
            k3_y1 = h * self.__f1(x[i] + h/2, y1[i] + k2_y1/2, y2[i] + k2_y2/2)
            k3_y2 = h * self.__f2(x[i] + h/2, y1[i] + k2_y1/2, y2[i] + k2_y2/2)
            
            k4_y1 = h * self.__f1(x[i] + h, y1[i] + k3_y1, y2[i] + k3_y2)
            k4_y2 = h * self.__f2(x[i] + h, y1[i] + k3_y1, y2[i] + k3_y2)
            
            y1[i+1] = y1[i] + (k1_y1 + 2*k2_y1 + 2*k3_y1 + k4_y1)/6
            y2[i+1] = y2[i] + (k1_y2 + 2*k2_y2 + 2*k3_y2 + k4_y2)/6
        
        return x, y1, y2


    def get_roots(self) -> None:
        try:
            self.left_border = float(self.widgets[0].get())
            self.right_border = float(self.widgets[1].get())
        except Exception as e:
            return error(e)
        
        y1_exact = []
        y2_exact = []
        for i in range(self.n):
            y1_exact.append(self.__exact_y1((self.__euler_method()[0])[i]))
            y2_exact.append(self.__exact_y2((self.__euler_method()[0])[i]))

        res_y1 = [[round(i, 4) for i in self.__euler_method()[1]],
                  [round(i, 4) for i in self.__runge_kutta()[1]],
                  [round(i, 4) for i in y1_exact]]
        
        res_y2 = [[round(i, 4) for i in self.__euler_method()[2]],
                  [round(i, 4) for i in self.__runge_kutta()[2]],
                  [round(i, 4) for i in y2_exact]]
        
        self.values = res_y1
        self.values_dop = res_y2
        disp_info(self, 450, 450, res_y2)


class SolverCauchySecondOrder:
    def __init__(self, win_frame) -> None:
        self.win_frame = win_frame
        self.fun = "np.log(np.tan(x/np.sqrt(10)))"
        self.name = 'Third_ss'

        self.values = []
        self.tk_val = ["2", "3"]
        self.widgets = []

        self.n = 10
        self.left_border = 2
        self.right_border = 3
        self.h = 0.1
        self.x0 = 0.0
        self.xn = 1.0
        self.y0 = 4.0
        self.y_prime0 = 1.0

        self.names_methods = ["Метод Эйлера", "Метод Рунге-Кутта", "Точное значение"]
        self.names_up = ["Методы", "y1(0.0)", "y1(0.1)", "y1(0.2)", "y1(0.3)", "y1(0.4)", "y1(0.5)", "y1(0.6)", "y1(0.7)", "y1(0.8)", "y1(0.9)", "y1(1.0)"]
        
        self.__tkinter_fun_se()
        plot_graph(self)
        

    def __tkinter_fun_se(self) -> None:
        Button(self.win_frame, text="RESET", bg="red", command= lambda: rst(self)).place(x=5, y=5)
        Label(self.win_frame, text="Задание 3: диференциальное уравнение второго порядка", font="14", bg='bisque').place(x=30, y=60)
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



    def __f(self, x, y, y_prime):
        return y + 2*np.exp(x) - x**2

    def __exact_solution(self, x):
        return (1 + x)*np.exp(x) + np.exp(-x) + x**2 + 2

    # Метод Эйлера для ОДУ второго порядка
    def __euler_method(self):
        x = np.arange(self.x0, self.xn + self.h, self.h)
        y = np.zeros_like(x)
        y_prime = np.zeros_like(x)
        
        y[0] = self.y0
        y_prime[0] = self.y_prime0
        
        for i in range(1, len(x)):
            y_prime[i] = y_prime[i-1] + self.h * self.__f(x[i-1], y[i-1], y_prime[i-1])
            y[i] = y[i-1] + self.h * y_prime[i-1]
        
        return x, y

    # Метод Рунге-Кутты 4-го порядка для ОДУ второго порядка
    def __runge_kutta_4(self):
        x = np.arange(self.x0, self.xn + self.h, self.h)
        y = np.zeros_like(x)
        y_prime = np.zeros_like(x)
        
        y[0] = self.y0
        y_prime[0] = self.y_prime0
        
        for i in range(1, len(x)):
            # Преобразуем ОДУ второго порядка в систему двух ОДУ первого порядка
            def system(Y, x_val):
                return np.array([Y[1], self.__f(x_val, Y[0], Y[1])])
            
            Y = np.array([y[i-1], y_prime[i-1]])
            
            k1 = self.h * system(Y, x[i-1])
            k2 = self.h * system(Y + 0.5*k1, x[i-1] + 0.5*self.h)
            k3 = self.h * system(Y + 0.5*k2, x[i-1] + 0.5*self.h)
            k4 = self.h * system(Y + k3, x[i-1] + self.h)
            
            Y_new = Y + (k1 + 2*k2 + 2*k3 + k4) / 6
            
            y[i] = Y_new[0]
            y_prime[i] = Y_new[1]
        
        return x, y


    def get_roots(self) -> None:
        try:
            self.left_border = float(self.widgets[0].get())
            self.right_border = float(self.widgets[1].get())
        except Exception as e:
            return error(e)


            # Вычисление решений
        x_euler, y_euler = self.__euler_method()
        x_rk, y_rk = self.__runge_kutta_4()

        exact_val = []
        for i in range(len(x_euler)):
            exact_val.append(self.__exact_solution(x_euler[i]))
            
        self.values = [[round(i,4) for i in y_euler],
                       [round(i,4) for i in y_rk],
                       [round(i,4) for i in exact_val]]



'''Основной класс'''
class Application:
    def __init__(self, win) -> None:
        self.win = win
        self.tk_widgets = []
        
        # Создаем меню-бар
        self.create_menu_bar()
        style = ttk.Style()
        style.configure("Custom.TFrame", background="bisque") 
        self.frame_first_order = ttk.Frame(win, style="Custom.TFrame")
        self.frame_sys_first_order = ttk.Frame(win, style="Custom.TFrame")
        self.frame_second_order = ttk.Frame(win, style="Custom.TFrame")
        self.solver_first_order= SolverCauchyFirstOrder(self.frame_first_order)
        self.solver_sys_first_order = SolverCauchySysFirstOrder(self.frame_sys_first_order)
        self.solver_second_order = SolverCauchySecondOrder(self.frame_second_order)

        self.show_frame(self.frame_first_order)

    def create_menu_bar(self) -> None:
        """Создает меню-бар с кнопками выбора задачи"""
        menubar = Menu(self.win)
        
        # Добавляем выпадающее меню "Задачи"
        task_menu = Menu(menubar, tearoff=0, font="15")
        task_menu.add_command(label="Задание 1 Дифур Первого рода", command=lambda: self.show_frame(self.frame_first_order))
        task_menu.add_command(label="Задание 2 Система дифуров первого рода", command=lambda: self.show_frame(self.frame_sys_first_order))
        task_menu.add_command(label="Задание 3 Дифур второго рода", command=lambda: self.show_frame(self.frame_second_order))
        
        menubar.add_cascade(label="Выбор задания", menu=task_menu)
        self.win.config(menu=menubar)

    def show_frame(self, frame) -> None:
        """Показывает выбранный фрейм и скрывает остальные"""
        self.frame_first_order.pack_forget()
        self.frame_sys_first_order.pack_forget()
        self.frame_second_order.pack_forget()
        
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
        values = obj.values_dop
        names_methods = obj.names_methods
        names_up = obj.names_up_dop

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
        if len(values) == 0:
            cell = Label(table_frame, text=f"Корней нет", bg="peachpuff", font="15" )
            cell.grid(row=1, column=1, padx=20)
            cell = Label(table_frame, text=f"Ошибка", bg="peachpuff", font="15" )
            cell.grid(row=1, column=0, padx=20)

def tkinter_fun() -> None: 
    win.title("Лабораторная работа №6 Вершинин АТ-24-01")
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
