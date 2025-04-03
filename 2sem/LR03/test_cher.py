from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import csv

# Глобальные переменные вместо полей класса
values = [(None, None, None) for _ in range(3)]
widgets = []
eps = 1e-3
matrix_a = [
    [3.6, 2.7, 1.5],
    [1.8, -3.6, 4.5],
    [-4.7, 1.9, 3.3]
]
matrix_b = [3.8, 0.4, -1.6]

def gauss_method():
    global values, eps, matrix_a, matrix_b
    
    # Создаем копии матриц для работы
    a = [row[:] for row in matrix_a]
    b = matrix_b[:]
    
    n = len(b)
    for i in range(n):
        # Частичный выбор ведущего элемента
        max_row = i
        for k in range(i+1, n):
            if abs(a[k][i]) > abs(a[max_row][i]):
                max_row = k
        
        # Перестановка строк
        a[i], a[max_row] = a[max_row], a[i]
        b[i], b[max_row] = b[max_row], b[i]
        
        # Нормализация текущей строки
        pivot = a[i][i]
        a[i] = [x/pivot for x in a[i]]
        b[i] /= pivot
        
        # Исключение переменной из других уравнений
        for k in range(i+1, n):
            factor = a[k][i]
            a[k] = [a_ki - factor * a_ij for a_ki, a_ij in zip(a[k], a[i])]
            b[k] -= factor * b[i]
    
    # Обратный ход
    solution = [0]*n
    for i in range(n-1, -1, -1):
        solution[i] = b[i] - sum(a_ij * x_j for a_ij, x_j in zip(a[i][i+1:], solution[i+1:]))
    
    values[0] = solution

def gauss_jordan_method():
    global values, eps, matrix_a, matrix_b
    
    # Создаем копии матриц для работы
    a = [row[:] for row in matrix_a]
    b = matrix_b[:]
    
    n = len(b)
    for i in range(n):
        # Частичный выбор ведущего элемента
        max_row = i
        for k in range(i+1, n):
            if abs(a[k][i]) > abs(a[max_row][i]):
                max_row = k
        
        # Перестановка строк
        a[i], a[max_row] = a[max_row], a[i]
        b[i], b[max_row] = b[max_row], b[i]
        
        # Проверка на вырожденность
        if abs(a[i][i]) < eps:
            raise ValueError("Матрица вырождена - система не имеет решения")
        
        # Нормализация текущей строки
        pivot = a[i][i]
        a[i] = [x/pivot for x in a[i]]
        b[i] /= pivot
        
        # Обнуление столбца во всех строках
        for k in range(n):
            if k != i:
                factor = a[k][i]
                a[k] = [a_kj - factor * a_ij for a_kj, a_ij in zip(a[k], a[i])]
                b[k] -= factor * b[i]
    
    values[1] = b

def get_roots():
    gauss_method()
    gauss_jordan_method()
    return values

def error(er='Ошибка'):
    er_win = Toplevel(win)
    er_win.title("Ошибка")
    er_win.geometry("350x150")
    Label(er_win, text=er, font="30", bg="red").pack()

def disp_info(ent_accur):
    global eps, values
    
    try:
        eps = float(ent_accur.get())
    except ValueError:
        return error("Введите численные значениия\n в границах")
    
    values = get_roots()
    names_methods = ["Гаусс", "Гаусс-Жордан"]
    names_up = ["Методы вычисления", "X1", "X2", "X3"]
    
    table_frame = Frame(master=win, bg="peachpuff")
    table_frame.place(x=500, y=250)
    widgets.append(table_frame)

    # Запись в CSV файл
    with open("Vershinin_LR03.csv", "w") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\n")
        writer.writerow(names_up)
        writer.writerow([names_methods[0], values[0][0], values[0][1], values[0][2]])
        writer.writerow([names_methods[1], values[1][0], values[1][1], values[1][2]])

    # Создание заголовков таблицы
    for i in range(len(names_up)):
        Label(table_frame, text=names_up[i], bg="peachpuff", font="15").grid(row=0, column=i, padx=20)

    # Заполнение данными
    for i in range(len(names_methods)):
        Label(table_frame, text=names_methods[i], bg="peachpuff", font="15").grid(row=i+1, column=0, padx=20, pady=20)
        for j in range(len(values[i])):
            Label(table_frame, text=f"{values[i][j]}", bg="peachpuff", font="15").grid(row=i+1, column=j+1, padx=20)

def disp_matrix(mat, x1, y1=385):
    table_frame = Frame(master=win, bg="bisque2")
    table_frame.place(x=x1, y=y1)
    for i in range(len(mat)):
        if isinstance(mat[i], list):
            for j in range(len(mat[i])):
                Label(table_frame, text=f"{mat[i][j]}", bg="bisque2", font="15").grid(row=i, column=j, padx=10, pady=10)
        else:
            Label(table_frame, text=f"{mat[i]}", bg="bisque2", font="15").grid(row=i, column=0, padx=10, pady=10)

def tkinter_fun():
    global widgets
    
    win.title("Лабораторная работа №3 Вершинин АТ-24-01")
    win.state('zoomed')
    win.resizable(0, 0)
    win.attributes("-alpha", 0.96)
    win.config(bg="bisque")
    Label(text="Вершинин Сергей АТ-24-01\nВариант №3", font="30", bg="bisque").place(x=70, y=740)

    Canvas(bg="peachpuff", width=395, height=300).place(x=1, y=1)
    Canvas(bg="bisque2", width=395, height=270).place(x=1, y=301)

    # Отображение матриц
    Label(text="Матрица A", font="15", bg="bisque2").place(x=60, y=335)
    Label(text="Матрица B", font="15", bg="bisque2").place(x=255, y=335)
    disp_matrix(matrix_a, 20)
    disp_matrix(matrix_b, 280)

    # Поле точности
    Label(text="Точность", font="15", bg="peachpuff").place(x=140, y=125)
    ent_accuracy = Entry(win, textvariable=StringVar(value="1e-3"), width=9, justify=CENTER)
    ent_accuracy.place(x=150, y=155)

    # Кнопка расчета
    Button(win, text="Рассчитать корни", font="15", command=lambda: disp_info(ent_accuracy)).place(x=100, y=50)
    
    widgets.append(ent_accuracy)
    Button(win, text="RESET", bg="red", command=rst).place(x=5, y=5)

def rst():
    global widgets, eps
    
    for widget in widgets:
        if isinstance(widget, Frame):
            widget.destroy()
        elif isinstance(widget, Entry):
            widget.delete(0, END)
            widget.insert(0, "1e-3")
    
    eps = 1e-3
    widgets = [widget for widget in widgets if isinstance(widget, Entry)]  # Оставляем только Entry

if __name__ == "__main__":
    win = Tk()
    tkinter_fun()
    win.mainloop()