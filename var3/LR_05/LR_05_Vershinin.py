from tkinter import *
import tkinter.ttk as ttk
from math import *
import random

from PIL import Image, ImageTk

def window() -> None:
    win.config(cursor="dot red")
    win.geometry("900x950")
    win.title("Лабораторная работа №5 Вершинин")
    win.minsize(900, 950)
    win.maxsize(900, 950)
    win.attributes("-alpha", 0.96)
    win.configure(background="gray12")
    Frame(background="gray5", height="1000", width="300").pack(anchor="nw")
    Label(
        text="Вершинин Сергей \n Лабораторная работа №5",
        fg="lightsalmon1",
        font="Arial 20 bold",
        background="gray12",
    ).place(x=440, y=15)
    
    Button(text="reset", background="red", command=cmd_rst).place(x=15, y=15)
    Button(text="Первое задание", command=cmd_first_var).place(x=80, y=70)
    Button(text="Второе задание", command=cmd_second_var).place(x=80, y=110)
    Button(text="Использовать рандомно\n сгенерированные значения",
            command=lambda: infill_matrix(1)).place(x=40, y=150)
    Button(text="Использовать pначения\n из задания",
            command=lambda: infill_matrix(0)).place(x=55, y=205)
    Button(text="Вычислить", command=cmd_btn_calc).place(x=95, y=260)


def cmd_rst() -> None:
    try:
        if var_status == 1:
            try:
                photo1.destroy()
                frame1.destroy()
                frame2.destroy()
                photo2.destroy()
            except:
                try:
                    photo2.destroy()
                    frame2.destroy()
                except:
                    pass
        else:
            try:
                photo2.destroy()
                frame1.destroy()
                frame2.destroy()
                photo1.destroy()
            except:
                try:
                    photo1.destroy()
                    frame1.destroy()
                except:
                    pass
    except:
        pass


def error(err) -> None:
    err_win = Toplevel(win)
    err_win.title("Error Window")
    err_win.geometry("400x200")
    Label(err_win, text=err).pack()


def cmd_btn_calc() -> None:
    try:
        var_status == array
    except NameError:
        return error("Выберите номер задания,\nспособ ввода данных")
    except:
        return error("Произошла непредвиденная ошибка\n"
                    + "перезапустите приложение")
    
    if var_status == 1:
        first_prod = dot_product([array[0],array[1]])
        second_prod = dot_product([array[2],array[3]])
        ans = [first_prod, second_prod, 
                check_dot_product([first_prod, second_prod])]
        
    else:
        first_matrix = [transposition(array[0]),
                        symmetry_checker(transposition(array[0]))]
        second_matrix = [transposition(array[1]),
                        symmetry_checker(transposition(array[1]))]
        third_matrix = [transposition(array[2]),
                        symmetry_checker(transposition(array[2]))]
        ans = [first_matrix, second_matrix, third_matrix]
    
    show_answer(ans)


def infill_matrix(gen_type) -> None:
    if gen_type:
        x = [random.randint(-18,10) for _ in range(3)]
        y = [random.randint(-18,10) for _ in range(3)]
        z = [random.randint(-18,10) for _ in range(4)]
        p = [random.randint(-18,10) for _ in range(4)]
        i = random.randint(2, 3)
        a = [[random.randint(-9, 9) for _ in range(i)] for _ in range(i)]
        b = [[random.randint(-9, 9) for _ in range(i)] for _ in range(i)]
        c = [[random.randint(-9, 9) for _ in range(i)] for _ in range(i)]
        
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
    else:
        show_values(array)


def show_answer(answer) -> None:
    global frame2
    try:
        frame2.destroy()
    except:
        pass

    if var_status == 1:
        names = ['X*Y', 'Z*P', 'A']
        frame2 = Frame()
        frame2.place(x=500, y=420)
        Label(frame2, text="Результирующие данные").grid(row=1, column=1, columnspan=2)
        for i in range(len(answer)):
            Label(frame2, text=names[i]).grid(row=i+2, column=1, padx=10, pady=10)
            Label(frame2, text=answer[i]).grid(row=i+2, column=2, pady=10)
    else:
        names = ["A'", "B'", "C'"]
        frame2 = Frame()
        frame2.place(x=330, y=420)
        Label(frame2, text="Результирующие данные").grid(row=1, column=0, columnspan=3)
        for i in range(3):
            Label(frame2, text=names[i]).grid(row=2, column=i, padx=10, pady=0)
            if answer[i][1]:
                txt = "симметричная"
            else:
                txt = "асимметричная"
            Label(frame2, text=txt).grid(row=3, column=i, padx=10, pady=10)
        
        for i in range(3):
            for j in range(len(answer[i][0])):
                Label(frame2, text=answer[i][0][j]).grid(row=j+4, column=i, padx=12)
        


def show_values(values) -> None:
    global frame1
    cmd_rst()
    if var_status == 1:
        cmd_first_var()
        names = ['X', 'Y', 'Z', 'P']
        frame1 = Frame()
        frame1.place(x=85, y=300)
        Label(frame1, text="Исходные данные").grid(row=1, column=1, columnspan=2)
        for i in range(len(values)):
            Label(frame1, text=names[i]).grid(row=i+2, column=1, padx=10, pady=10)
            Label(frame1, text=values[i]).grid(row=i+2, column=2, pady=10)
    else:
        cmd_second_var()
        names = ['A', 'B', 'C']
        frame1 = Frame()
        frame1.place(x=22, y=300)
        Label(frame1, text="Исходные данные").grid(row=1, column=0, columnspan=3)
        for i in range(3):
            Label(frame1, text=names[i]).grid(row=2, column=i, padx=10, pady=10)
        for i in range(len(values)):
            for j in range(len(values[i])):
                Label(frame1, text=values[i][j]).grid(row=j+3, column=i, padx=12)


# Функции для первого задания
def cmd_first_var() -> None:
    global var_status
    global img1
    global photo1
    var_status = 1

    cmd_rst()
    try:
        img1 = ImageTk.PhotoImage(
            Image.open("python/learning/informatics/"
                    + "var3/LR_05/number_1.png").resize((400, 300)))
        
        photo1 = Label(win, image = img1)
        photo1.place(x=370, y=100)
    except:
        error("Для вывода картинки укажите путь в программе")


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


# Функции для второго задания 
def cmd_second_var() -> None:
    global var_status
    global img2
    global photo2
    var_status = 2

    cmd_rst()
    try:
        img2 = ImageTk.PhotoImage(
            Image.open("python/learning/informatics/"
                    + "var3/LR_05/number_2.png").resize((400, 300)))
        photo2 = Label(win, image = img2)
        photo2.place(x=370, y=100)
    except:
        error("Для вывода картинки укажите путь в программе")


def transposition(arr) -> list:
    new_arr = []
    for i in range(len(arr) - 1):
        if len(arr[i]) != len(arr[i + 1]):
            error("Введенная мартица не удовлетворяет условиям\n"
                    + "для траспонирования")
            return "Ошибка транспонирования"

    for i in range(len(arr[0])):
        line = []
        for j in range(len(arr)):
            line.append(arr[j][i])
        new_arr.append(line)
    return new_arr


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


win = Tk()
window()
win.mainloop()
