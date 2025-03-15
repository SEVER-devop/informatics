import math as mt
from tkinter import *


class Name():
    pass


def start() -> None:
    global GLOBAL_NAMES

    win.title("Лабораторная работа №1 Вершинин АТ-24-01")
    win.geometry("1350x750")
    win.resizable(0, 0)
    win.attributes("-alpha", 0.96)
    Label(text="Вершинин Сергей АТ-24-01\nВариант №3").pack()
    ent1 = Entry(win, textvariable=StringVar(value=0), width=5)
    ent1.place(x=100, y=100)
    ent2 = Entry(win, textvariable=StringVar(value=1), width=5)
    ent2.place(x=120, y=100)


    GLOBAL_NAMES = [ent1, ent2, ent3, ent4]
    btn1 = Button(win, text="RESET", command=lambda x=GLOBA_NAMES: rst(x))
    btn1.place(x=10, y=10)




def rst(x) -> None:
    for i in x:
        pass



if __name__ == "__main__":
    win = Tk()
    start()
    win.mainloop()
