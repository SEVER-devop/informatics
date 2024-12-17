# Задана последовательность X = (x1, x2, …, x10).
# Сформировать из неё одномерный массив Y, состоящий из элементов,
# удовлетворяющих условию | xi | < G – x2, где G – среднее геометрическое
# значение элементов массива X. Если таковых не окажется, вывести фразу
# «Искомых элементов нет». Полученный массив напечатать в столбик.
# Исходный и искомый массивы представить в виде графиков.
# X = {5.31, -0.2, 1, -2.2, 3.25, -1.74, 4.9, -2.1, 0.9, 1.15}.

from tkinter import *
from math import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter.ttk as ttk
import matplotlib.pyplot as plt


win = Tk()
win.config(cursor='dot red')
win.geometry('700x700')
win.title("Лабораторная работа №3 Вершинин") 
win.minsize(400, 350)
win.attributes("-alpha", 0.96)


def finish() -> None:
    win.destroy()

def error() -> None:
    err_win = Toplevel(win)
    err_win.title("Error Window")
    err_win.geometry("200x200")
    Label(err_win, text ="Искомых элементов нет").pack()

def btn1() -> None: 
    x_arr = [5.31, -0.2, 1, -2.2, 3.25, -1.74, 4.9, -2.1, 0.9, 1.15]
    y_arr = new_array(x_arr)
    disp_graphs(x_arr, y_arr)

def btn2() -> None:
    e_text = ent1.get()
    cond1 = sum([1 for i in e_text.split(' ') if i.replace(',', '1').replace('.', '1').isnumeric()]) == 10
    if len(e_text.split()) == 10 and cond1:
        e_text = list(map(float, e_text.split(' ')))
    else:
        error()
        return 0

    graph_data = new_array(e_text)

    disp_graphs(e_text, graph_data)

def new_array(arr) -> list:
    geo_mean = 1
    y_arr = []

    for i in arr:
        geo_mean *= i
    geo_mean = round(geo_mean**(1/10), 4)

    for i in arr:
        if (geo_mean - arr[1]) > i:
            y_arr.append(i)
    
    if len(y_arr) == 0:
        return error()
    else:
        graph_data = [[arr.index(i), i] for i in y_arr] 
    print(*y_arr, sep="\n")

    return y_arr

def rst() -> None:
    btn1["state"] = ["normal"] 
    btn2["state"] = ["normal"] 
    ent1.delete(0, END)
    try:
        canvas.get_tk_widget().pack_forget()
    except:
        pass

def disp_graphs(x_arr, y_arr) -> None:
    rst()
    fig, ax = plt.subplots()
    ax.plot([i + 1 for i in range(len(y_arr))], y_arr)
    ax.plot([i + 1 for i in range(len(x_arr))], x_arr)
    ax.set_title("Графики функций, вариант №3")
    ax.set_xlabel('x')
    ax.set_ylabel("f(x)")
    global canvas
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)
    canvas.draw()


ttk.Button(text='rest', command=rst).pack(anchor=NE, padx=10, pady=10)
Label(text="Лабораторная работа №3 \n Вершинин Сергей \n АТ-24-01", borderwidth=10, relief="ridge").pack()
btn1 = ttk.Button(text="Ипользовать массив X", command=btn1)
btn1.pack(padx=10, pady=10)
Label(text = "X = {5.31, -0.2, 1, -2.2, 3.25, -1.74, 4.9, -2.1, 0.9, 1.15}").pack()
Label(text = "Введите собственные данные массива длиной 10 значений через пробел").pack()
ent1 = ttk.Entry()
ent1.pack(padx=10, pady=10)
btn2 = ttk.Button(text="Ипользовать введенный массив", command=btn2)
btn2.pack(padx=10, pady=10)

win.protocol("WM_DELETE_WINDOW", finish)
win.mainloop()
