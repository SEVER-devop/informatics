from tkinter import *
import tkinter.ttk as ttk
from math import *

from PIL import Image, ImageTk


# Блок кода для Tkinter
def window() -> None:
    global img1
    win.config(cursor="dot red")
    win.geometry("900x950")
    win.title("Лабораторная работа №6 Вершинин")
    win.minsize(900, 950)
    win.maxsize(900, 950)
    win.attributes("-alpha", 0.96)
    win.configure(background="gray12")
    Frame(background="gray5", height="1000", width="400").pack(anchor="nw")
    Label(
        text="Вершинин Сергей \n Лабораторная работа №6",
        fg="lightsalmon1",
        font="Arial 20 bold",
        background="gray12",
    ).place(x=510, y=15)

    Button(text="reset", background="red", command=cmd_rst).place(x=15, y=15)
    Button(text="Вычислить", command=cmd_btn_calc).place(x=110, y=30)
    try:
        img1 = ImageTk.PhotoImage(Image.open("python/learning/informatics/var3"
                                + "/LR_06/number_6.png").resize((400, 100)))

        Label(win, image=img1).place(x=440, y=100)
    except:
        error("Для вывода картинки укажите путь в программе")


def disp_info(values) -> None:
    global frame1, frame2, frame3, frame4, frame5
    accuracy = 1

    frame1 = Frame()
    frame1.place(x=25, y=70)
    Label(frame1, text="Исходная матрица").grid(row=1, column=1, columnspan=2)
    for i in range(len(values[0])):
        val = []
        for j in values[0][i]:
            val.append(round(j, accuracy))
        Label(frame1, text=val).grid(row=i + 2, column=2, pady=10)

    frame2 = Frame()
    frame2.place(x=25, y=480)
    Label(frame2, text="Результирующая матрица").grid(row=1, column=1, columnspan=2)
    for i in range(len(values[1][0])):
        val = []
        for j in values[1][0][i]:
            val.append(round(j, accuracy))
        Label(frame2, text=val).grid(row=i + 2, column=2, pady=10)

    frame3 = Frame()
    frame3.place(x=480, y=250)
    Label(frame3, text="Среднее значение строк исходной матрицы").grid(
        row=1, column=2, columnspan=9
    )
    for i in range(len(values[1][1])):
        Label(frame3, text=round(values[1][1][i], accuracy)).grid(
            row=2, column=i + 2, pady=15
        )

    frame4 = Frame()
    frame4.place(x=535, y=350)
    Label(frame4, text="Вектор X").grid(row=1, column=2, columnspan=9)
    for i in range(len(values[2])):
        Label(frame4, text=round(values[2][i], accuracy)).grid(
            row=2, column=i + 2, pady=15
        )

    frame5 = Frame()
    frame5.place(x=535, y=450)
    Label(frame5, text="Отсортированный вектор X").grid(row=1, column=2, columnspan=9)
    for i in range(len(values[3])):
        Label(frame5, text=round(values[3][i], accuracy)).grid(
            row=2, column=i + 2, pady=15
        )


def list_to_str_convert(val, name) -> list:
    res = f"{name}\n"
    if isinstance(val[0], list):
        for i in range(len(val)):
            for j in val[i]:
                res += str(j) + " "
            res += "\n"
    else:
        for i in val:
            res += str(i) + ' '
        res += "\n"
    res += "\n"

    return res


def save_info(values) -> None:
    names = ["Matrix",
                [
                "Resulting matrix",
                "Average value of the row elements of the matrix"
                ],
            "Vector X",
            "Sorted Vector X"
            ]
    data = []
    for i in range(len(values)):
        if i == 1:
            for j in range(2):
                data.append(list_to_str_convert(values[i][j], names[i][j]))
        else:
            data.append(list_to_str_convert(values[i], names[i]))

    with open('LR_06_Vershinin.txt', 'w+') as f:
        f.writelines(data)


def cmd_btn_calc():
    matrix = matrix_infill()
    second_answer = second_number(matrix)
    vector_x = third_number(second_answer[0])
    vector_x_sort = fourth_number(vector_x)
    disp_info([matrix, second_answer, vector_x, vector_x_sort])
    save_info([matrix, second_answer, vector_x, vector_x_sort])


def cmd_rst():
    try:
        frame1.destroy()
        frame2.destroy()
        frame3.destroy()
        frame4.destroy()
        frame5.destroy()
    except:
        pass



def error(err) -> None:
    err_win = Toplevel(win)
    err_win.title("Error Window")
    err_win.geometry("400x200")
    Label(err_win, text=err).pack()


# Блок функций для решения задач
def matrix_infill() -> list:
    mat = [[None for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if i < 2:
                mat[i][j] = 0.17 * i + sqrt(0.17 * i + j)
            else:
                mat[i][j] = (j**2 + 3.2 * i) ** (3 / 2)

    return mat


def second_number(mat) -> list:
    # Среднее значение элементов строк
    average_mat = []
    for i in mat:
        average_str = 0
        for j in i:
            average_str += j
        average_mat.append(average_str / 9)

    # Перестановка 3го и 7го столбца
    for i in range(9):
        mat[i][2], mat[i][6] = mat[i][6], mat[i][2]

    return mat, average_mat


def third_number(mat) -> list:
    vec = []
    for i in mat[1]:
        vec.append(i)
    return vec


def fourth_number(vector) -> list:
    vec = []
    for i in vector:
        vec.append(i)
    for i in range(len(vec) - 1):
        for j in range(len(vec) - 1 - i):
            if vec[j] > vec[j + 1]:
                vec[j], vec[j + 1] = vec[j + 1], vec[j]

    return vec


win = Tk()
window()
win.mainloop()
