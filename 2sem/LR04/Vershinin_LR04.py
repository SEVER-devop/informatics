from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

import math
import numpy as np


class RootFinder:
    def __init__(self) -> None:
        self.values = [None for _ in range(12)]
        self.widgets = []
        self.eps = 1e-3
        self.a = 0
        self.b = 1
        self.x_values = [0, 0.13, 0.26, 0.39,0.52,0.65, 0.79, 0.92, 1.05, 1.18, 1.31, 1.44, 1.57]
        self.y_values = [0, 0.004, 0.033, 0.104, 0.217, 0.358, 0.5, 0.608, 0.65, 0.604, 0.467, 0.254, 0]


    def __func(self, x) -> None:
        return math.log(x + math.sqrt(x*x + 8))


    def __left_rectangle_analit_integral(self) -> None:
        func = self.__func
        precision = self.eps
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

    def __mid_rectangle_analit_integral(self) -> None:
        func = self.__func
        precision = self.eps
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

    def __right_rectangle_analit_integral(self) -> None:
        func = self.__func
        precision = self.eps
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

    def __trapezoidal_analit_integral(self) -> None:
        func = self.__func
        precision = self.eps
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

    def __simpson_analit_integral(self) -> None:
        func = self.__func
        precision = self.eps
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

    def __analytical_integral(self) -> None:
        integral = (-3 +2*math.sqrt(2) + math.log(4))
        self.values[5] = integral


    def __left_rectangles_table_integral(self) -> None:
        integral = 0.0
        x = self.x_values
        y = self.y_values
        for i in range(len(x) - 1):
            integral += y[i] * (x[i+1] - x[i])
        self.values[6] = integral

    def __right_rectangles_table_integral(self) -> None:
        integral = 0.0
        x = self.x_values
        y = self.y_values
        for i in range(len(x) - 1):
            integral += y[i+1] * (x[i+1] - x[i])
        self.values[7] = integral

    def __mid_rectangles_table_integral(self) -> None:
        integral = 0.0
        x = self.x_values
        y = self.y_values
        for i in range(len(x) - 1):
            mid_y = (y[i] + y[i+1]) / 2
            integral += mid_y * (x[i+1] - x[i])
        self.values[8] = integral

    def __trapezoidal_table_integral(self) -> None:
        integral = 0.0
        x = self.x_values
        y = self.y_values
        for i in range(len(x) - 1):
            integral += (y[i] + y[i+1]) * (x[i+1] - x[i]) / 2
        self.values[9] = integral

    def __simpson_table_integral(self) -> None:
        x = self.x_values
        y = self.y_values

        if (len(x) - 1) % 2 != 0:
            raise ValueError("Для метода Симпсона необходимо четное число интервалов")
        
        integral = y[0] + y[-1]
        h = x[1] - x[0]
        
        for i in range(1, len(x)-1):
            if i % 2 == 1:
                integral += 4 * y[i]
            else:
                integral += 2 * y[i]
        
        integral *= h / 3
        self.values[10] = integral

    def __technical_spec_table_integral(self) -> None:
        self.values[11] = 0.5


    def get_roots(self) -> list:
        self.__left_rectangle_analit_integral()
        self.__mid_rectangle_analit_integral()
        self.__right_rectangle_analit_integral()
        self.__trapezoidal_analit_integral()
        self.__simpson_analit_integral()
        self.__analytical_integral()
        
        self.__left_rectangles_table_integral()
        self.__right_rectangles_table_integral()
        self.__mid_rectangles_table_integral()
        self.__trapezoidal_table_integral()
        self.__simpson_table_integral()
        self.__technical_spec_table_integral()

        return self.values




roots = RootFinder()


def error(er='Ошибка'):
    er_win = Toplevel(win)
    er_win.title("Ошибка")
    er_win.geometry("350x150")
    Label(er_win, text=er, font="30", bg="red").pack()

 
def disp_info(ent_accur, left, right) -> None:
    try:
        accuracity = float(ent_accur.get())
        left_ent = int(left.get())
        right_ent = int(right.get())
    except ValueError:
        return error("Введите численные значениия\n в границах")
    roots.eps = accuracity
    roots.a = left_ent
    roots.b = right_ent
    plot_graph(left_ent, right_ent)
    

    values = roots.get_roots()
    names_methods = ["Лев. треуг.", "Средн. треуг.", "Прав. треуг.", "Трапец.", "Симпсон", "Аналитика"]
    names_up = ["Методы вычисления", "RES"]
    table_frame_first = Frame(master=win, bg="peachpuff")
    table_frame_first.place(x=700, y=70)
    table_frame_second = Frame(master=win, bg="peachpuff")
    table_frame_second.place(x=1100, y=70)
    names_frame = [table_frame_first, table_frame_second]
    roots.widgets.extend(names_frame)
    names_integral = ["Интеграл, заданный функцией","Таблично заданный интеграл"]

    for j in range(len(names_frame)):
        Label(names_frame[j], text=names_integral[j], bg="peachpuff", font="15").grid(row=0, column=0, columnspan=2, padx=20)
        for i in range(len(names_up)):
            cell = Label(names_frame[j], text= f"{names_up[i]}", bg="peachpuff", font="15" )
            cell.grid(row=1, column=i, padx=20, pady=20)

        for i in range(len(names_methods)):
            cell = Label(names_frame[j], text=f"{names_methods[i]}", bg="peachpuff", font="15" )
            cell.grid(row=i+2, column=0, padx=20, pady=20)
            cell = Label(names_frame[j], text=f"{float(values[i + j*6]):.4f}", bg="peachpuff", font="15" )
            cell.grid(row=i+2, column=1, padx=20)


def disp_matrix(mat, x1, y1=385) -> None:

    table_frame = Frame(master=win, bg="peachpuff")
    table_frame.place(x=x1, y=y1)
    for i in range(len(mat)):
        if type(mat[i]) == list:
            for j in range(len(mat[i])):
                cell = Label(table_frame, text=f"{mat[i][j]}", bg="peachpuff", font="15" )
                cell.grid(row=i, column=j, padx=10, pady=10)
        else:
            cell = Label(table_frame, text=f"{mat[i]}", bg="peachpuff", font="15" )
            cell.grid(row=i, column=0, padx=10, pady=10)


def plot_graph(ent_left, ent_right) -> None:

    if ent_left is not(type(10)):
        try:
            left_border = float(ent_left.get())
            right_border = float(ent_right.get())
        except ValueError:
            return error("Введите численные значениия\n в границах")
        except:
            pass
        left_border = roots.a
        right_border = roots.b 
    else:
        left_border = ent_left
        right_border = ent_right

    x = np.linspace(left_border, right_border, 1000)
    y = np.log(x + np.sqrt(x**2 + 8))

    fig = Figure(figsize=(4, 4), facecolor='peachpuff')
    ax = fig.add_subplot(facecolor='bisque')
    
    ax.plot(x, y, color='r', linestyle='solid', linewidth=2)


    ax.axhline(y=0, color='gray', linestyle='-', linewidth=1)
    fig.patch.set_edgecolor('whitesmoke')
    fig.patch.set_linewidth(2) 

    canvas1 = FigureCanvasTkAgg(fig, master = win)
    canvas1.draw()
    canvas1.get_tk_widget().place(x=-1, y=300)
    # roots.widgets.append(canvas1)
    

def tkinter_fun() -> None:
    
    win.title("Лабораторная работа №4 Вершинин АТ-24-01")
    win.state('zoomed')
    win.resizable(0, 0)
    win.attributes("-alpha", 0.96)
    win.config(bg="bisque")
    Label(text="Вершинин Сергей АТ-24-01\nВариант №3", font="30", bg="bisque").place(x=70, y=740)


    Canvas(bg="peachpuff", width=395, height=300).place(x=1, y=1)
    Canvas(bg="peachpuff", width=280, height=670).place(x=397, y=1)


    # Интеграл
    fig = Figure(figsize=(4, 3), facecolor='peachpuff')
    ax = fig.add_subplot(111)
    ax.axis('off')
    integral_text = r"$\int_{0}^{1} \log \left( x + \sqrt{x^2 + 8} \right) \, dx$"
    ax.text(0.5, 0.5, integral_text, fontsize=20, 
            ha='center', va='center', color='black')
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().place(x=-10, y=50)


    # Границы
    Label(text="Границы", font="15", bg="peachpuff").place(x=105, y=65)
    ent_left_border = Entry(win, textvariable=StringVar(value=0), width=5, justify=CENTER)
    ent_left_border.place(x=105, y=95)
    ent_right_border = Entry(win, textvariable=StringVar(value=1), width=5, justify=CENTER)
    ent_right_border.place(x=145, y=95)


    # Уравнение
    Label(text="Вектор X", font="15", bg="peachpuff").place(x=435, y=5)
    Label(text="Вектор F(X)", font="15", bg="peachpuff").place(x=560, y=5)
    disp_matrix(roots.x_values, 440, 30)
    disp_matrix(roots.y_values, 570, 30)

    
    # Точность
    Label(text="Точность", font="15", bg="peachpuff").place(x=220, y=65)
    ent_accuracy = Entry(win, textvariable=StringVar(value="1e-3"), width=9, justify=CENTER)
    ent_accuracy.place(x=230, y=95)

    # Расчет всех корней
    Button(win, text="Рассчитать корни", font="15", command= lambda x=ent_accuracy,
                                                                    y=ent_left_border,
                                                                    z=ent_right_border: disp_info(x, y, z)).place(x=130, y=20)
    
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
