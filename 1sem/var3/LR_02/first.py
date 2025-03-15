import matplotlib.pyplot as plt
import numpy as np
import math as mt


def zap(m, arr): # Фунцкия для 1-го задания
    for i in range(0,3):
        arr[i].append(m[i])


def yres(s, res = 1): # Функция для 2-го задания
    lst = list(s)
    for i in lst:
        res *= i
    return res


def first(): # Задане №1
    arr = [[],[],[]] # x y p
    arr_table = []
    for x in np.arange(-0.1, 1, 0.1):
        x = float(round(x, 1))
        if x <= 0:
            y = (abs(x) + 3.5)
        elif x >= 0.5:
            y = (1 + x**2)
        else:
            y = (mt.sin(x)**2)
        p = ((0.75 * mt.log(1 + y**2))/(y + 0.5))
        zap([x, y, p], arr)

    for i in range(0, len(arr[2])):
        arr_table.append([round(arr[0][i], 3), round(arr[1][i], 3), round(arr[2][i], 3)])
    plt.figure('Задание №1')
    table = plt.table(cellText=arr_table,
    colWidths=[0.09] * 3,
    colLabels = ['x', 'y', 'p'],
    colColours = ['yellow', 'green', 'red'],
    loc='upper center')
    plt.plot(arr[0], arr[1], c = 'cyan')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.title('График зависимости X и Y', fontsize=20, fontname='Times New Roman')
    plt.scatter(arr[0], arr[1], linestyle='-', c = 'red', marker='.')
    plt.show()


def second(): # Задание №2
    x = 2.43
    y_set = set()
    z_res = 1
    for z in range(3, 11):
        for y in range(1, 6):
            y_set.add((mt.log(abs(x + y), 3) + z)/(0.1 * y - y**2 - y**3))
        y_res = yres(y_set)
        z_work = (z * mt.cos(1/z))/(z**2 + (x**2 / (z + x)))
        z_res *= z_work
        s = z_res - y_res
        print(f'При z = {'{:.1f}'.format(z)}, s = {'{:.8f}'.format(s)}', end = '\n')

second()
first()
