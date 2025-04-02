from tkinter import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


win = Tk()
win.title('Лабораторная работа 2, выполнил Чернышев АТ-24-01')
win.geometry('1600x1600')
win.config(bg='lightcyan1')

lev = StringVar(value=-15)
prav = StringVar(value=15)
lev1 = StringVar(value=-5)
lev2 = StringVar(value=-1)
prav1 = StringVar(value=1)
prav2 = StringVar(value=5)
e = StringVar(value=0.001)

Entry(win,textvariable=lev, bg='aliceblue', fg='black', width=5).place(x=35, y=25)
Entry(win,textvariable=prav, bg='aliceblue',fg='black', width=5).place(x=75, y=25)
Entry(win, textvariable=lev1, bg='aliceblue', fg='black', width=5).place(x=115, y=25)
Entry(win, textvariable=prav1, bg='aliceblue', fg='black', width=5).place(x=155, y=25)
Entry(win, textvariable=lev2, bg='aliceblue', fg='black', width=5).place(x=195, y=25)
Entry(win, textvariable=prav2, bg='aliceblue', fg='black', width=5).place(x=235, y=25)
Label(win, text='Интервал', font=('Arial Black', 8), bg='lightcyan1').place(x=38, y=0)
Label(win, text='Интервал1', font=('Arial Black', 8), bg='lightcyan1').place(x=118, y=0)
Label(win, text='Интервал2', font=('Arial Black', 8), bg='lightcyan1').place(x=195, y=0)



def graphic():
    a = float(lev.get())
    b = float(prav.get())
    x = np.linspace(a, b, 400)

    a = -1
    b = x - 2
    c = 2 * x ** 2 + 2 * x + 6
    #(-(x-2)+((x-2)**2 + 4(2 * x ** 2 + 2 * x + 6))**(1/2))/(-2)
    D = b ** 2 - 4 * a * c
    y1_positive = (-b + D ** (1 / 2)) / (2 * a)
    y1_negative = (-b - D ** (1 / 2)) / (2 * a)
    y2 = 0.5 * x ** 2 + 1

    plt.figure(figsize=(10, 6))
    plt.plot(x, y1_positive, label='2*x^2 - x*y - y^2 + 2*x - 2*y + 6 = 0', color='blue')
    plt.plot(x, y1_negative, color='blue')
    plt.plot(x, y2, label='y - 0.5*x^2 - 1 = 0', color='red')

    plt.title('Графики двух уравнений')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.ylim(-10, 10)
    plt.show()

def analit1():
    a1 = float(lev.get())
    b1 = float(prav.get())
    X = []
    frame1 = Frame()
    frame1.place(x=750, y=29)
    Label(frame1,text='x').pack()
    frame2 = Frame()
    frame2.place(x=770, y=29)
    Label(frame2, text='f(x)').pack()
    for i in range(int(a1), int(b1)):
        X.append(i)
        Label(frame1, text=i).pack()
    for j in X:
        y = 0.5 * j ** 2 + 1
        Label(frame2, text=y).pack()

def analit2():
    a1 = float(lev.get())
    b1 = float(prav.get())
    X = []
    frame1 = Frame()
    frame1.place(x=930, y=29)
    Label(frame1,text='x').pack()
    frame2 = Frame()
    frame2.place(x=950, y=29)
    Label(frame2, text='f(x)').pack()

    for j in range(int(a1), int(b1)):
        a = -1
        b = j - 2
        c = 2 * j ** 2 + 2 * j + 6

        D = b ** 2 - 4 * a * c

        if D >= 0:
            y = (-b + np.sqrt(D)) / (2 * a)

        Label(frame1, text=j).pack()
        Label(frame2, text=y).pack()

def analit3():
    a1 = float(lev.get())
    b1 = float(prav.get())
    X = []
    frame1 = Frame()
    frame1.place(x=1130, y=29)
    Label(frame1,text='x').pack()
    frame2 = Frame()
    frame2.place(x=1150, y=29)
    Label(frame2, text='f(x)').pack()

    for j in range(int(a1), int(b1)):
        a = -1
        b = j - 2
        c = 2 * j ** 2 + 2 * j + 6

        D = b ** 2 - 4 * a * c

        if D >= 0:
            y = (-b - np.sqrt(D)) / (2 * a)

        Label(frame1, text=j).pack()
        Label(frame2, text=y).pack()


def F1(x, y):
    return 2 * x ** 2 - x * y - y ** 2 + 2 * x - 2 * y + 6


def F2(x, y):
    return y - 0.5 * x ** 2 - 1


# Rearranging to fit the Jacobi method form:
def Fy(x):
    return (x - 2 + sqrt((x - 2) ** 2 + 4 * (2 * x ** 2 + 2 * x + 6))) / (2)


def Fx(y):
    if y-1 >= 0:
        return -2 * sqrt(y - 1)
    else:
        return 0


def yakobi(e=float(10e-1)):
    # Извлекаем начальные значения из текстовых полей
    x0 = float(lev1.get())
    y0 = float(lev2.get())

#     iterations = 0
#     error = float('inf')

# # Начальная итерируемая переменная
#     while error > e:
#         # Сохраняем предыдущее значение
#         x_old, y_old = x0, y0

#         # Обновляем значения для следующей итерации
#         x0 = Fx(y_old)
#         y0 = Fy(x_old)

#         # Обновляем ошибку
#         error = max(abs(x0 - x_old), abs(y0 - y_old))
#         iterations += 1

    x, y = x0, y0
    x, y = 1.6, 1
    for iterations in range(100000):
        x_old, y_old = x, y

        # Обновляем y из второго уравнения
        y = 0.5 * x_old**2 + 1

        # Обновляем x из первого уравнения (квадратное)
        a = 2
        b = 2 - y_old
        c = -(y_old**2 + 2 * y_old - 6)
        discriminant = b**2 - 4 * a * c

        if discriminant >= 0:
            x = (-b + np.sqrt(discriminant)) / (2 * a)
        else:
            # Если дискриминант отрицательный, оставляем старое значение
            x = x_old

        # Проверка на сходимость
        if np.abs(x - x_old) < e and np.abs(y - y_old) < e:
            print(f"Решение найдено за {iterations + 1} итераций")
            print(f"x = {x:.6f}, y = {y:.6f}")
            x0 = x
            y0 = y
            break

    # Вывод результатов
    Label(win, text=iterations).place(x=590, y=325)
    Label(win, text=f'{x0:.4f}').place(x=370, y=325)
    Label(win, text=f'{y0:.4f}').place(x=370, y=370)
    Label(win, text='Значение корня :', font=('Arial Black', 8), bg="cadetblue1").place(x=370, y=300)
    Label(win, text='Количество итераций :', font=('Arial Black', 8), bg="cadetblue1").place(x=520, y=300)
    Label(win, text='Значение функции :', font=('Arial Black', 8), bg="cadetblue1").place(x=370, y=350)

    # Вывод значений функций F1 и F2 в найденной точке
    Label(win, text=f'F1: {F1(x0, y0):.4f}').place(x=370, y=400)
    Label(win, text=f'F2: {F2(x0, y0):.4f}').place(x=370, y=430)

# Обратите внимание на объявления функций и переменные в вашем основном коде так же.


press1=Button(win,command=graphic,text='Построение графика ', font=('Arial Black', 8),bg="coral").place(x=0, y=50)
press2=Button(win,command=analit1,text='Аналитический(красный)', font=('Arial Black', 8),bg="coral").place(x=700, y=0)
press3=Button(win,command=analit2,text='Аналитический(синий +)', font=('Arial Black', 8),bg="coral").place(x=900, y=0)
press4=Button(win,command=analit3,text='Аналитический(синий -)', font=('Arial Black', 8),bg="coral").place(x=1100, y=0)
press5=Button(win,command=yakobi,text='Метод якоби', font=('Arial Black', 8),bg="coral").place(x=0, y=350)



win.mainloop()