from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

import csv


class RootFinder:
    def __init__(self):
        self.values = [(None, None, None) for _ in range(3)]
        self.widgets = []
        self.eps = 1e-3
        self.matrix_a = [
                            [3.6, 2.7, 1.5],
                            [1.8, -3.6, 4.5],
                            [-4.7, 1.9, 3.3]
                        ]
        self.matrix_b = [3.8, 0.4, -1.6]


    def __gauss_method(self):
        matrix_a = [i for i in self.matrix_a]
        matrix_b = [i for i in self.matrix_b]

        n = len(matrix_b)
        for i in range(n):
            max_row = i
            for k in range(i+1, n):
                if abs(matrix_a[k][i]) > abs(matrix_a[max_row][i]):
                    max_row = k
            
            matrix_a[i], matrix_a[max_row] = matrix_a[max_row], matrix_a[i]
            matrix_b[i], matrix_b[max_row] = matrix_b[max_row], matrix_b[i]
            
            
            prev_el = matrix_a[i][i]
            matrix_a[i] = [a/prev_el for a in matrix_a[i]]
            matrix_b[i] /= prev_el
            
            for k in range(i+1, n):
                m = matrix_a[k][i]
                matrix_a[k] = [a - m*b for a,b in zip(matrix_a[k], matrix_a[i])]
                matrix_b[k] -= m * matrix_b[i]
        
        solution = [0]*n
        for i in range(n-1, -1, -1):
            solution[i] = matrix_b[i] - sum(a*x for a,x in zip(matrix_a[i][i+1:], solution[i+1:]))
        
        self.values[0] = solution

    
    def __gauss_jordan_method(self):
        matrix_a = [i for i in self.matrix_a]
        matrix_b = [i for i in self.matrix_b]
    
        n = len(matrix_b)
        for i in range(n):
            # Частичный выбор ведущего элемента
            max_row = i
            for k in range(i+1, n):
                if abs(matrix_a[k][i]) > abs(matrix_a[max_row][i]):
                    max_row = k
            
            # Перестановка строк
            matrix_a[i], matrix_a[max_row] = matrix_a[max_row], matrix_a[i]
            matrix_b[i], matrix_b[max_row] = matrix_b[max_row], matrix_b[i]
            
            # Проверка на вырожденность
            if abs(matrix_a[i][i]) < self.eps:
                raise ValueError("Матрица вырождена - система не имеет решения")
            
            # Нормализация текущей строки
            prev_el = matrix_a[i][i]
            matrix_a[i] = [a/prev_el for a in matrix_a[i]]
            matrix_b[i] /= prev_el
            
            # Обнуление всех элементов в столбце
            for k in range(n):
                if k != i:
                    m = matrix_a[k][i]
                    matrix_a[k] = [a - m*b for a,b in zip(matrix_a[k], matrix_a[i])]
                    matrix_b[k] -= m * matrix_b[i]
        
        self.values[1] = matrix_b


    def get_roots(self):
        self.__gauss_method()
        self.__gauss_jordan_method()
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
    names_methods = ["Гаусс", "Гаусс-Жордан"]
    names_up = ["Методы вычисления", "X1", "X2", "X3"]
    table_frame = Frame(master=win, bg="peachpuff")
    table_frame.place(x=500, y=250)
    roots.widgets.append(table_frame)

    field = names_up
    data = [
                ["Гаусс", values[0][0], values[0][1], values[0][2]],
                ["Гаусс-Жордан", values[1][0], values[1][1], values[1][2]],
            ]

    with open("Vershinin_LR03.csv", "w") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\n")
        writer.writerow(field)
        writer.writerows(data)



    for i in range(len(names_up)):
        cell = Label(table_frame, text=f"{names_up[i]}", bg="peachpuff", font="15" )
        cell.grid(row=0, column=i, padx=20)

    for i in range(len(names_methods)):
        cell = Label(table_frame, text=f"{names_methods[i]}", bg="peachpuff", font="15" )
        cell.grid(row=i+1, column=0, padx=20, pady=20)
        for j in range(len(values[i])):
            cell = Label(table_frame, text=f"{values[i][j]}", bg="peachpuff", font="15" )
            cell.grid(row=i+1, column=j+1, padx=20)


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


def tkinter_fun() -> None:
    
    win.title("Лабораторная работа №3 Вершинин АТ-24-01")
    win.state('zoomed')
    win.resizable(0, 0)
    win.attributes("-alpha", 0.96)
    win.config(bg="bisque")
    Label(text="Вершинин Сергей АТ-24-01\nВариант №3", font="30", bg="bisque").place(x=70, y=740)

    Canvas(bg="peachpuff", width=395, height=300).place(x=1, y=1)
    Canvas(bg="bisque2", width=395, height=270).place(x=1, y=301)


    # Уравнение
    Label(text="Матрица A", font="15", bg="bisque2").place(x=60, y=335)
    Label(text="Матрица B", font="15", bg="bisque2").place(x=255, y=335)
    disp_matrix(roots.matrix_a, 20)
    disp_matrix(roots.matrix_b, 280)

    
    # Точность
    Label(text="Точность", font="15", bg="peachpuff").place(x=140, y=125)
    ent_accuracy = Entry(win, textvariable=StringVar(value="1e-3"), width=9, justify=CENTER)
    ent_accuracy.place(x=150, y=155)

    # Расчет всех корней
    Button(win, text="Рассчитать корни", font="15", command= lambda x=ent_accuracy: disp_info(x)).place(x=100, y=50)
    
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
