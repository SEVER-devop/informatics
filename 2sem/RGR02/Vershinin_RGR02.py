import math as mt

# import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk

import numpy as np

class SolverNonlinearEquations:
    def __init__(self, win_frame):
        self.values = [(None, None, None) for _ in range(5)]
        self.widgets = []
        self.eps = 1e-3
        self.max_iter = 1000
        self.left_border = -2
        self.right_border = 3



    def get_roots(self):

        return self.values


class NumericalIntegration:
    def __init__(self, win_frame):
        pass

class SolverDifferentialEquations:
    def __init__(self, win_frame):
        pass


class Application:
    def __init__(self, win):
        self.win = win
        self.win.title("Домашнее задание 02 (Вариант 3)")
        
        # Создаем меню-бар
        self.create_menu_bar()
        
        # Фреймы для задач (изначально скрыты)
        self.frame_eq = ttk.Frame(win)
        self.frame_int = ttk.Frame(win)
        self.frame_diff = ttk.Frame(win)
        
        # Инициализация решателей задач
        self.eq_solver = SolverNonlinearEquations(self.frame_eq)
        self.int_calculator = NumericalIntegration(self.frame_int)
        self.diff_solver = SolverDifferentialEquations(self.frame_diff)
        
        # Показываем первую задачу по умолчанию
        self.show_frame(self.frame_eq)

    def create_menu_bar(self):
        """Создает меню-бар с кнопками выбора задачи"""
        menubar = Menu(self.win)
        
        # Добавляем выпадающее меню "Задачи"
        task_menu = Menu(menubar, tearoff=0)
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


def plot_graph(ent_left, ent_right) -> None:

    try:
        left_border = float(ent_left.get())
        right_border = float(ent_right.get())
    except ValueError:
        return error("Введите численные значениия\n в границах")
    roots.left_border = left_border
    roots.right_border = right_border


    x = np.linspace(left_border, right_border, 1000)
    y = x**3 - 3*x**2 + 3

    fig = Figure(figsize=(4, 4), facecolor='peachpuff')
    ax = fig.add_subplot(facecolor='bisque')
    
    ax.plot(x, y, color='r', linestyle='solid', linewidth=2)

    ax.axhline(y=0, color='gray', linestyle='-', linewidth=1)
    fig.patch.set_edgecolor('whitesmoke')
    fig.patch.set_linewidth(2) 

    canvas1 = FigureCanvasTkAgg(fig, master = win)
    canvas1.draw()
    canvas1.get_tk_widget().place(x=-1, y=300)
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
    ent_left_border = Entry(win, textvariable=StringVar(value=-2), width=5, justify=CENTER)
    ent_left_border.place(x=25, y=135)
    ent_right_border = Entry(win, textvariable=StringVar(value=3), width=5, justify=CENTER)
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
    # roots.widgets.extend(all_wid)
    Button(win, text="RESET", bg="red", command=rst).place(x=5, y=5)


def rst() -> None:
    values = ['-2', '3', "1e-3", "1000", "1"]
    for i in range(len(roots.widgets)):
        if "matplotlib.backends.backend_tkagg.FigureCanvasTkAgg" in str(roots.widgets[i]):
            roots.widgets[i].get_tk_widget().destroy()
        elif ".!frame" in str(roots.widgets[i]):
            roots.widgets[i].destroy()
        else:
            roots.widgets[i].delete(0, END)
            roots.widgets[i].insert(0, values[i])
        



win = Tk()
app = Application(win)
# win.geometry("900x700")
tkinter_fun()
win.mainloop()
