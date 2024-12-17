from tkinter import *
from tkinter import PhotoImage
import tkinter.ttk as ttk
from PIL import Image, ImageTk

win = Tk()
win.config(cursor='dot red')
win.geometry('790x850')
win.title("Лабораторная работа №4 Вершинин") 
win.minsize(550, 450)
win.attributes("-alpha", 0.96)


def start(ent_str) -> list:
    lim_val = [float(i) for i in ent_str.replace(',', '.').split()]
    if len(lim_val) != 2 or lim_val[0] >= lim_val[1]:
        er = "Значения интервала \nвведены некорректно"
        error(er)
    
    return lim_val

def finish() -> None:
    win.destroy()
    exit()

def matrix_fill() -> list:
    n = 4
    m = 5
    mat = []
    for i in range(1, n + 1):
        line = []
        for j in range(1, m + 1):
            if i >= 2:
                line.append(round((j**2 + 3.2 * i)**(3/2), 3))
            else:
                line.append(round(0.17 * i + (0.17 * i + j)**(1/2), 3))
        mat.append(line)


    return mat

def calc_matrix(lim_val, mat) -> list:
    ans_mat = []
    for i in mat:
        line = []
        for j in i:
            if j >= lim_val[0] and j <= lim_val[1]:
                line.append(round(j, 3))
        if line:
            ans_mat.append(line)

    return ans_mat

def show(ans, mat) -> None:
    global tree_ans, tree_orig, l1, l2
    rst()
    columns = ("str_num", "quantity", "str_values")
    tree_ans = ttk.Treeview(columns=columns, show="headings")
    tree_orig = ttk.Treeview(columns=columns, show="headings")
    l1 = Label(text="Значения исходной матрицы")
    l2 = Label(text="Значения результирующей матрицы")
    values = []

    for i, lines in enumerate(mat):
        values.append([i + 1, len(lines), lines])

    for i in range(2):
        tree = [tree_orig, tree_ans][i]
        if i == 1:
            l2.pack()
            values = []
            for i, lines in enumerate(ans):
                 for j in range(len(mat)):
                    if lines[0] in mat[j]:
                        values.append([j + 1, len(lines), lines])
        else:
            l1.pack()

        tree.pack(fill=BOTH)
        tree.heading("str_num", text="Номер строки")
        tree.heading("quantity", text="Количество элементов")
        tree.heading("str_values", text="Значения строки в заданном интервале")
        for val in values:
            tree.insert("", END, values=val)
        
def btn1() -> None:
    show(calc_matrix(start(entry.get()), matrix_fill()), matrix_fill())

def rst() -> None:
    btn1["state"] = ["normal"]
    entry.delete(0, END)
    try:
        tree_ans.destroy()
        tree_orig.destroy()
        l1.destroy()
        l2.destroy()
    except:
        pass

def error(er) -> None:
    err_win = Toplevel(win)
    err_win.title("Error Window")
    err_win.geometry("200x200")
    Label(err_win, text=er).pack()


ttk.Button(text='rest', command=rst).pack(anchor=NE, padx=10, pady=10)
Label(text="Лабораторная работа №4 \n Вершинин Сергей \n АТ-24-01", borderwidth=10, relief="ridge").pack()
# Для вывода картинки с заданием необходимо убрать комментарии и изменить путь к файлу
img2 = ImageTk.PhotoImage(Image.open("python/learning/infa/var3/LR_04/shot.png").resize((600, 175)))
Label(win, image = img2).pack()

Label(text="Введите интервал через пробел").pack()
btn1 = ttk.Button(text="Подтвердить", command=btn1)
btn1.pack(padx=10, pady=10)
entry = ttk.Entry()
entry.pack(padx=10, pady=10)

win.protocol("WM_DELETE_WINDOW", finish)
win.mainloop()
