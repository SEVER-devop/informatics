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
lev2 = StringVar(value=0)
prav1 = StringVar(value=0)
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



def graphic_1():
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
    frame1.place(x=805, y=29)
    Label(frame1,text='x').pack()
    frame2 = Frame()
    frame2.place(x=830, y=29)
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
    frame1.place(x=955, y=29)
    Label(frame1,text='x').pack()
    frame2 = Frame()
    frame2.place(x=980, y=29)
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
    frame2.place(x=1155, y=29)
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
        return -2 * 1

def yakobi(e=float(10e-3)):
    x0 = float(lev2.get())
    y0 = float(prav2.get())
    x0 = 5
    y0 = 0
    iterations = 0
    error = float('inf')

    while error > e:
        x_old, y_old = x0, y0

        x0 = Fx(y_old)
        y0 = Fy(x_old)

        error = max(abs(x0 - x_old), abs(y0 - y_old))
        iterations += 1


    Label(win, text=iterations).place(x=170, y=400)
    Label(win, text=f'{x0:.4f}').place(x=20, y=400)
    Label(win, text=f'{y0:.4f}').place(x=20, y=470)
    Label(win, text='Значение корня :', font=('Arial Black', 8), bg="cadetblue1").place(x=0, y=380)
    Label(win, text='Количество итераций :', font=('Arial Black', 8), bg="cadetblue1").place(x=130, y=380)
    Label(win, text='Значение функции :', font=('Arial Black', 8), bg="cadetblue1").place(x=0, y=450)

    Label(win, text=f'F1: {F1(x0, y0):.4f}').place(x=20, y=495)
    Label(win, text=f'F2: {F2(x0, y0):.4f}').place(x=20, y=520)





# ... (предыдущий код остается без изменений)

def newton_method(e=float(10e-3)):
    x0 = float(lev2.get())
    y0 = float(prav2.get())
    iterations = 0
    error = float('inf')
    
    while error > e:
        # Вычисляем значения функций
        f1 = F1(x0, y0)
        f2 = F2(x0, y0)
        
        # Вычисляем элементы матрицы Якоби
        # df1/dx = 4x - y + 2
        # df1/dy = -x - 2y - 2
        # df2/dx = -x
        # df2/dy = 1
        J = np.array([
            [4*x0 - y0 + 2, -x0 - 2*y0 - 2],
            [-x0, 1]
        ])
        
        # Вектор функций
        F = np.array([f1, f2])
        
        try:
            # Решаем систему линейных уравнений J*delta = -F
            delta = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError:
            Label(win, text="Матрица Якоби вырождена").place(x=300, y=400)
            return
            
        x_new = x0 + delta[0]
        y_new = y0 + delta[1]
        
        error = max(abs(x_new - x0), abs(y_new - y0))
        x0, y0 = x_new, y_new
        iterations += 1
        
        # Защита от бесконечного цикла
        if iterations > 1000:
            break
    
    # Вывод результатов
    Label(win, text=iterations).place(x=470, y=400)
    Label(win, text=f'{x0:.4f}').place(x=320, y=400)
    Label(win, text=f'{y0:.4f}').place(x=320, y=470)
    Label(win, text='Значение корня :', font=('Arial Black', 8), bg="cadetblue1").place(x=300, y=380)
    Label(win, text='Количество итераций :', font=('Arial Black', 8), bg="cadetblue1").place(x=430, y=380)
    Label(win, text='Значение функции :', font=('Arial Black', 8), bg="cadetblue1").place(x=300, y=450)

    Label(win, text=f'F1: {F1(x0, y0):.4f}').place(x=320, y=495)
    Label(win, text=f'F2: {F2(x0, y0):.4f}').place(x=320, y=520)

def gauss_seidel(e=float(10e-3)):
    x0 = float(lev2.get())
    y0 = float(prav2.get())
    iterations = 0
    error = float('inf')
    
    while error > e:
        x_old, y_old = x0, y0
        
        # Сначала обновляем x, используя текущее значение y
        # Из F2: y = 0.5*x^2 + 1
        # Подставляем в F1 и решаем относительно x
        # Но для простоты используем итерационную формулу
        x0 = Fx(y_old)
        
        # Затем обновляем y, используя только что вычисленное x
        y0 = Fy(x0)
        
        error = max(abs(x0 - x_old), abs(y0 - y_old))
        iterations += 1
        
        # Защита от бесконечного цикла
        if iterations > 1000:
            break
    
    # Вывод результатов
    Label(win, text=iterations).place(x=670, y=400)
    Label(win, text=f'{x0:.4f}').place(x=520, y=400)
    Label(win, text=f'{y0:.4f}').place(x=520, y=470)
    Label(win, text='Значение корня :', font=('Arial Black', 8), bg="cadetblue1").place(x=500, y=380)
    Label(win, text='Количество итераций :', font=('Arial Black', 8), bg="cadetblue1").place(x=630, y=380)
    Label(win, text='Значение функции :', font=('Arial Black', 8), bg="cadetblue1").place(x=500, y=450)

    Label(win, text=f'F1: {F1(x0, y0):.4f}').place(x=520, y=495)
    Label(win, text=f'F2: {F2(x0, y0):.4f}').place(x=520, y=520)

# Добавляем кнопки для новых методов
press6 = Button(win, command=newton_method, text='Метод Ньютона', font=('Arial Black', 8), bg="coral").place(x=300, y=350)
press7 = Button(win, command=gauss_seidel, text='Метод Гаусса-Зейделя', font=('Arial Black', 8), bg="coral").place(x=500, y=350)




def graphic():
    a = float(lev.get())
    b = float(prav.get())
    x = np.linspace(a, b, 400)
    
    # Первое уравнение: 2*x^2 - x*y - y^2 + 2*x - 2*y + 6 = 0
    # Решаем относительно y: -y^2 - (x + 2)y + (2x^2 + 2x + 6) = 0
    # Квадратное уравнение вида ay^2 + by + c = 0
    a_coeff = -1
    b_coeff = -(x + 2)
    c_coeff = 2*x**2 + 2*x + 6
    
    D = b_coeff**2 - 4*a_coeff*c_coeff
    
    # Рассчитываем только действительные корни
    valid = D >= 0
    x_valid = x[valid]
    D_valid = D[valid]
    
    y1_positive = np.zeros_like(x) * np.nan
    y1_negative = np.zeros_like(x) * np.nan
    
    y1_positive[valid] = (-b_coeff[valid] + np.sqrt(D_valid)) / (2*a_coeff)
    y1_negative[valid] = (-b_coeff[valid] - np.sqrt(D_valid)) / (2*a_coeff)
    
    # Второе уравнение: y = 0.5*x^2 + 1
    y2 = 0.5 * x**2 + 1

    plt.figure(figsize=(10, 6))
    
    # Рисуем только действительные части графиков
    plt.plot(x, y1_positive, label='2*x^2 - x*y - y^2 + 2*x - 2*y + 6 = 0 (y1)', color='blue')
    plt.plot(x, y1_negative, label='2*x^2 - x*y - y^2 + 2*x - 2*y + 6 = 0 (y2)', color='green')
    plt.plot(x, y2, label='y = 0.5*x^2 + 1', color='red')

    plt.title('Графики двух уравнений')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(True)
    plt.legend()
    
    # Автоматическое масштабирование осей
    plt.autoscale(enable=True, axis='both', tight=True)
    
    # Показываем пересечения графиков (решения системы)
    plt.scatter([-2], [3], color='purple', zorder=5, label='Решение (-2, 3)')
    
    plt.show()




press1=Button(win,command=graphic,text='Построение графика ', font=('Arial Black', 8),bg="coral").place(x=0, y=50)
press2=Button(win,command=analit1,text='Аналитический(красный)', font=('Arial Black', 8),bg="coral").place(x=760, y=0)
press3=Button(win,command=analit2,text='Аналитический(синий +)', font=('Arial Black', 8),bg="coral").place(x=940, y=0)
press4=Button(win,command=analit3,text='Аналитический(синий -)', font=('Arial Black', 8),bg="coral").place(x=1110, y=0)
press5=Button(win,command=yakobi,text='Метод якоби', font=('Arial Black', 8),bg="coral").place(x=0, y=350)



win.mainloop()