import scipy.optimize
import math as mt
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image
import tkinter as tk

file = open('1.txt', 'w', encoding='utf-8')

# функция
def f(x):
    y = 2 * mt.sin(x + mt.pi / 3)-0.5*x**2+1
    return (y)

file.write(f'2 *sin(x + П / 3)-0.5*x^2+1\n')
file.write(f'\n')

# фотка графика
def graf():
    global k
    global kol
    global nameax
    global namebx
    global a
    global b
    global h
    global e
    global Nn
    global name_mass

    a = float(namex.get())
    b = float(namey.get())
    h = float(nameh.get())
    e = float(namee.get())

    file.write(f'Значение левой границы:{a}\n')
    file.write(f'Значение правой границы:{b}\n')
    file.write(f'Значение изменения Х:{h}\n')
    file.write(f'Значение точности:{e}\n')
    file.write(f'\n')
    x = []
    y = []
    Nn = int((b - a) // h + 1)
    for i in range(Nn):
        x.append(a + i * h)
        y.append(f(x[i]))

    plt.figure('График')
    plt.title('График функции y(x)', fontsize=16, fontname='Times New Roman')
    plt.grid('on')
    plt.plot(x, y, c='m')
    plt.savefig('saved_figure.PNG')
    gr = "saved_figure.PNG"
    image = tk.PhotoImage(file="saved_figure.PNG")
    imageLabel = tk.Label(win, image=image)
    imageLabel.image = image
    imageLabel.place(x=750, y=30)

    # таблица
    lbl = tk.Label(win, text='x')
    lbl.place(x=600, y=30)
    lbl = tk.Label(win, text='y')
    lbl.place(x=650, y=30)
    for i in range(len(x)):
        lbl = tk.Label(win, text=round(x[i], 2))
        lbl.place(x=600, y=i * 15 + 50)
    for i in range(len(y)):
        lbl = tk.Label(win, text=round(y[i], 2))
        lbl.place(x=650, y=i * 15 + 50)

    file.write(f'X:{x}\n')
    file.write(f'Y:{y}\n')
    file.write(f'\n')

    # Кол-во корней
    kol = []
    x0 = []
    y0 = []
    k = 0
    for i in range(1, len(y)):
        if (y[i - 1] * y[i]) <= 0:
            k += 1
            kol.append(k)
            x0.append(0.5 * (x[i - 1] + x[i]))
            y0.append(0)

    file.write(f'Кол-во корней:{k}\n')
    file.write(f'\n')

    lbl5 = tk.Label(win, text='Кол-во корней: ')
    lbl5.place(x=60, y=190)
    lbl6 = tk.Label(win, text=k)
    lbl6.place(x=160, y=190)
    name_mass = []
    for i in range(k):
        lbl7 = tk.Label(win, text='Введите границу интервала левую: ')
        lbl7.place(x=60, y=i * 180 + 220)
        nameax = tk.Entry(win)
        nameax.place(x=280, y=i * 180 + 220)

        lbl8 = tk.Label(win, text='Введите границу интервала правую: ')
        lbl8.place(x=60, y=i * 180 + 250)
        namebx = tk.Entry(win)
        namebx.place(x=280, y=i * 180 + 250)

        lbl9 = tk.Label(win, text='Корень методом половинного деления: ')
        lbl9.place(x=60, y=i * 180 + 280)

        lbl10 = tk.Label(win, text='Корень методом хорд:')
        lbl10.place(x=60, y=i * 180 + 310)

        lbl11 = tk.Label(win, text='Корень методом касательных (Ньютона):')
        lbl11.place(x=60, y=i * 180 + 340)

        lbl12 = tk.Label(win, text='Корень методом Итераций:')
        lbl12.place(x=60, y=i * 180 + 370)

        btn2 = tk.Button(win, text='Считать корни:', command=korni)
        btn2.place(x=440, y=i * 180 + 230)

        name_mass.append([nameax, namebx])

def korni():


    # метод половинного деления
    def metod1(a, b, e):
        global m
        m = 0
        while abs(b - a) / 2 > e and m < Nn:
            midp = (a + b) / 2
            if f(midp) == 0:
                return midp
            elif f(a) * f(midp) < 0:
                b = midp
            else:
                a = midp
            m += 1
        return (a + b) / 2


    # метод хорд
    def metod2(a, b, e):
        global k
        x_prev = a
        x = b - f(b) * (b - a) / (f(b) - f(a))
        k = 0
        while abs(x - x_prev) > e or abs(f(x)) > e and k < Nn:
            if f(x) == 0:
                return x
            if f(x) * f(a) < 0:
                b = x
            else:
                a = x
            k += 1

            x_prev = x
            x = b - f(b) * (b - a) / (f(b) - f(a))
        return x


    # производная
    def f_prime(x):
        return 2 * mt.cos(x + mt.pi / 3) - x

    # метод касательных
    def metod3(a, b, e):
        global l
        l = 0
        while abs(f(b)) > e and l < Nn:
            x = b - f(b) / f_prime(b)
            l += 1
        return x


    # метод итераций
    def metod4(a, b, e):
        global p
        p = 0
        while p < Nn:
            pol = (a + b) / 2
            if f(pol) == 0 or (b - a) / 2 < e:
                x = pol
                break
            p += 1
            if f(pol) * f(a) < 0:
                b = pol
            else:
                a = pol
        return x


    for i in range(k):
        ax = float(name_mass[i][0].get())
        bx = float(name_mass[i][1].get())

        file.write(f'Значение левой границы корня:{ax}\n')
        file.write(f'Значение правой границы корня:{bx}\n')
        file.write(f'\n')

        SCI=[]

        k1 = round(metod1(ax, bx, e),4)
        if k1 != 0:
            lbl13 = tk.Label(win, text=k1)
            lbl13.place(x=350, y=i * 180 + 280)
        y1 = scipy.optimize.fsolve(f, 0.5 * (ax + bx))

        k2 = round(metod2(ax, bx, e),4)
        if k2 != 0:
            lbl14 = tk.Label(win, text=k2)
            lbl14.place(x=280, y=i * 180 + 310)
        y2 = scipy.optimize.bisect(f, ax, bx)

        k3 = round(metod3(ax, bx, e),4)
        if k3 != 0:
            lbl15 = tk.Label(win, text=k3)
            lbl15.place(x=350, y=i * 180 + 340)
        y3 = scipy.optimize.newton(f, 0.5 * (ax + bx))

        k4 = round(metod4(ax, bx, e),4)
        if k4 != 0:
            lbl16 = tk.Label(win, text=k4)
            lbl16.place(x=280, y=i * 180 + 370)
        y4 = scipy.optimize.root_scalar(f, method='secant', x0=ax, x1=bx, xtol=1e-2)

        SCI=[y1,y2,y3,y4]
        names = ["Метод 1", "Метод 2", "Метод 3", "Метод 4"]
        values = [k1, k2, k3, k4]
        iteration = [m, k, l, p]

        file.write(f'Корень методом SCIPY:\n')
        file.write(f'Методы:{names}\n')
        file.write(f'Корень:{SCI}\n')
        file.write(f'\n')

        file.write(f'Методы:{names}\n')
        file.write(f'Корень:{values}\n')
        file.write(f'Итерации:{iteration}\n')
        file.write(f'\n')
        if i == 0:
            tk.Label(win, text="Таблица").place(x=800, y=600)
            tk.Label(win, text="Корень 1").place(x=900, y=600)
            tk.Label(win, text="Кол-во итераций").place(x=1000, y=600)
            for j in range(len(names)):
                tk.Label(win, text=names[j]).place(x=800, y=630 + j * 30)
                tk.Label(win, text="SCIPY").place(x=800, y=750)

                tk.Label(win, text=y2).place(x=900, y=750)

                tk.Label(win, text=values[j]).place(x=900, y=630 + j * 30)
                tk.Label(win, text=iteration[j]).place(x=1000, y=630 + j * 30)

        if i != 0:
            tk.Label(win, text=f"Корень {i + 1}").place(x=900 + i * 250, y=600)
            tk.Label(win, text="Кол-во итераций").place(x=1000 + i * 300, y=600)
            for j in range(len(names)):
                tk.Label(win, text=values[j]).place(x=900 + i * 250, y=630 + j * 30)
                tk.Label(win, text=y2).place(x=1150, y=750)
                tk.Label(win, text=iteration[j]).place(x=1000 + i * 350, y=630 + j * 30)
            file.close()



win = tk.Tk()
win.geometry('1500x1000')
win.title("Гринько АТ-24-01 ЛР1, Вариант 5")

lbl1 = tk.Label(win, text='Введите Левую границу: ')
lbl1.place(x=60, y=40)
namex = tk.Entry(win)
namex.place(x=220, y=40)

lbl2 = tk.Label(win, text='Введите Правую границу: ')
lbl2.place(x=60, y=70)
namey = tk.Entry(win)
namey.place(x=220, y=70)

lbl3 = tk.Label(win, text='Введите изменение Х: ')
lbl3.place(x=60, y=100)
nameh = tk.Entry(win)
nameh.place(x=220, y=100)

lbl4 = tk.Label(win, text='Введите точность: ')
lbl4.place(x=60, y=130)
namee = tk.Entry(win)
namee.place(x=220, y=130)

btn1 = tk.Button(win, text='Сформировать Y и посторить график', command=graf)
btn1.place(x=60, y=160)


win.mainloop()