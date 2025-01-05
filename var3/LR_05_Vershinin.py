from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from math import *
from pprint import *
import random

global win, rst_btn, var_status, array


def window() -> None:
    win.config(cursor="dot red")
    win.geometry("900x950")
    win.title("Лабораторная работа №5 Вершинин")
    win.minsize(850, 850)
    win.maxsize(850, 850)
    win.attributes("-alpha", 0.96)
    win.configure(background="gray12")
    Frame(background="gray5", height="1000", width="300").pack(anchor="nw")
    Label(
        text="Вершинин Сергей \n Лабораторная работа №5",
        fg="lightsalmon1",
        font="Arial 20 bold",
        background="gray12",
    ).place(x=440, y=15)
    
    Button(text="Вычислить", command=cmd_btn_calc).place(x=95, y=300)
    Button(text="reset", background="red", command=cmd_rst).place(x=15, y=15)
    Button(text="Первое задание", command=cmd_first_var).place(x=80, y=70)
    Button(text="Второе задание", command=cmd_second_var).place(x=80, y=110)
    Button(text="Использовать рандомно\n сгенерированные значения", command=lambda: infill_matrix(1)).place(x=40, y=180)
    Button(text="Использовать pначения\n из задания", command=lambda: infill_matrix(0)).place(x=55, y=230)

def infill_matrix(gen_type) -> None:
    if gen_type:
        x = [random.randint(-18,10) for _ in range(3)]
        y = [random.randint(-18,10) for _ in range(3)]
        z = [random.randint(-18,10) for _ in range(4)]
        p = [random.randint(-18,10) for _ in range(4)]
        i = random.randint(2, 5)
        a = [[random.randint(-18, 10) for _ in range(i)] for _ in range(i)]
        b = [[random.randint(-18, 10) for _ in range(i)] for _ in range(i)]
        c = [[random.randint(-18, 10) for _ in range(i)] for _ in range(i)]
        
    else:
        x = [1.5, 2.1, 3.0]
        y = [2.1, 1.1, 3.2]
        z = [3.7, 1.2, 6.4, -5.3]
        p = [1.8, -1.8, 2.5, -2.2]

        a = [[1.5, 0.3], [1.8, 2.1]]
        b = [[1.1, 2.2, 0.1], [3.3, -1, 2.5], [1.5, 2.1, 0.8]]
        c = [[1.5, 0.1, 2.1], [0.1, -2.8, -1], [2.1, -1, 0.5]]

    try:
        global array
        if var_status == 1:
            array = [x, y, z, p]
        else:
            array = [a, b, c]
    except:
        error("сначала выберите вариант задания")
    
    
def cmd_btn_calc() -> None:
    print("1111")

def cmd_first_var() -> None:
    global var_status
    var_status = 1


def cmd_second_var() -> None:
    global var_status
    var_stattus = 2


def cmd_rst() -> None:
    pass


def error(err) -> None:
    err_win = Toplevel(win)
    err_win.title("Error Window")
    err_win.geometry("400x200")
    Label(err_win, text=err).pack()


def dot_product(vectors) -> float:
    dot_product = 0
    if (len(vectors[0]) != len(vectors[1])) or len(vectors) != 2:

        return error("Значение векторов введены не корректно")

    for i in range(len(vectors[0])):
        dot_product += vectors[0][i] * vectors[1][i]

    return dot_product


def check_dot_product(dot_products) -> int:
    if dot_products[0] > dot_products[1]:
        return 1
    return 0


def transposition(arr) -> list:
    new_arr = []
    for i in range(len(arr) - 1):
        if len(arr[i]) != len(arr[i + 1]):
            error("Введенная мартица не удовлетворяет условиям\n для траспонирования")
            return [[arr], ["Ошибка транспонирования"]]

    for i in range(len(arr[0])):
        line = []
        for j in range(len(arr)):
            line.append(arr[j][i])
        new_arr.append(line)
    return [arr, new_arr]


def symmetry_checker(arr) -> bool:
    try:
        for i in range(len(arr[0])):
            for j in range(len(arr[0][i])):
                if arr[0][i][j] != arr[1][i][j]:
                    return False
                
        for i in range(len(arr[1])):
            for j in range(len(arr[1][i])):
                if arr[0][i][j] != arr[1][i][j]:
                    return False
    except:
        return False
    
    return True


#answer = check_dot_product([dot_product([x, y]), dot_product([z, p])])

a = "{:.2f}".format(123.456)
b = isclose(15.060000000000002, 15.060)
print(b)

try:
    print(array)
except:
    pass

win = Tk()
window()
win.mainloop()
