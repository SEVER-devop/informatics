import math

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Определение вашей функции, которую нужно решить.
    return x**3 - 2*x + 1

# Метод дихотомии
def dichotomy(a, b, eps=1e-6):

    if f(a) * f(b) >= 0:
        print('Ошибка: f(a) и f(b) должны иметь разные знаки.')
        return
    
    count = 0
    x = (a + b) / 2
    while abs(f(x)) > eps:
        count += 1
        if f(x) * f(a) < 0:
            b = x
        else:
            a = x
        x = (a + b) / 2
    return x

# Метод хорд
def chord_method(a, b, eps=1e-6):
    while True:
        m = (f(b) * a - f(a) * b) / (f(b) - f(a))
        if abs(f(m)) < eps:
            break
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return m

# Метод Ньютона (метод касательных)
def newton_raphson(x0, eps=1e-6):
    def df(x):
        # Производная функции f(x)
        return 3*x**2 - 2
    
    while True:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < eps:
            break
        x0 = x1
    return x1

# Метод простых итераций
def simple_iteration(phi, x0, eps=1e-6):
    while True:
        x1 = phi(x0)
        if abs(x1 - x0) < eps:
            break
        x0 = x1
    return x1

# Функция для построения графика
def plot_function(a, b, step=0.01):
    x = np.arange(a, b+step, step)
    y = f(x)
    plt.plot(x, y, label='Function')
    plt.axhline(y=0, color='k', linestyle='--')  # линия y=0
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of the function')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print("Enter interval limits:")
    a = float(input("Left limit: "))
    b = float(input("Right limit: "))
    print("Enter precision (epsilon):")
    eps = float(input("Precision: "))
    
    print("\nMethod of Dichotomy:")
    root_dichotomy = dichotomy(a, b, eps)
    print(f"Root by Dichotomy method: {root_dichotomy}")
    
    print("\nChord Method:")
    root_chord = chord_method(a, b, eps)
    print(f"Root by Chord method: {root_chord}")
    
    print("\nNewton-Raphson Method:")
    root_newton = newton_raphson((a+b)/2, eps)
    print(f"Root by Newton-Raphson method: {root_newton}")
    
    print("\nSimple Iteration Method:")
    # Предположим, что функция преобразования уже известна
    def phi(x):
        return x - f(x)
    root_simple_iter = simple_iteration(phi, (a+b)/2, eps)
    print(f"Root by Simple Iteration method: {root_simple_iter}")
    
    # Построение графика функции
    plot_function(a, b)






# def f(x):
#     a2 = float(a.get())
#     return sqrt(pi/2) * exp(a2*x) + x/(a22+x2)
# def fi(x):
#     a2 = float(a.get())
#     return -sqrt(pi/2) * exp(a2*x) * (a22+x2)
# def fp(x):
#     a2 = float(a.get())
#     return sqrt(pi/2) * a2 * exp(a2*x) + (a22 + x2)/((a22+x2)**2)


# def dyhotomy():
#     a = float(lev1.get())
#     b = float(prav1.get())
#     eps = float(e.get())

#     if f(a) * f(b) >= 0:
#         Label(win, text='Ошибка: f(a) и f(b) должны иметь разные знаки.', bg="red").place(x=0, y=490)
#         return

#     count = 0
#     x = (a + b) / 2
#     while abs(f(x)) > eps:
#         count += 1
#         if f(x) * f(a) < 0:
#             b = x
#         else:
#             a = x
#         x = (a + b) / 2

#     Label(win, text='Значение корня:', font=('Arial Black', 8), bg="aquamarine1").place(x=0, y=490)
#     Label(win, text='Количество итераций:', font=('Arial Black', 8), bg="aquamarine1").place(x=120, y=490)
#     Label(win, text='Значение функции:', font=('Arial Black', 8), bg="aquamarine1").place(x=0, y=540)
#     Label(win, text=count).place(x=190, y=515)
#     Label(win, text=x).place(x=0, y=515)
#     Label(win, text=f(x)).place(x=0, y=565)

#     with open('text.txt', 'a') as file:  # Используйте режим 'a' для добавления
#         file.write('Дихотомия:\n')
#         file.write(f'Кол-во итераций: {count}\n')
#         file.write(f'x: {x}\n')
#         file.write(f'f(x): {f(x)}\n\n')

# def Newtons():
#     eps = float(e.get())
#     a = float(lev1.get())
#     b = float(prav1.get())
#     count=0
#     x=b-f(b)/fp(b)
#     while abs(f(x)) > eps:
#         x = b - f(b) / fp(b)
#         b=x
#         count+=1
#     Label(win, text=count).place(x=215, y=325)
#     Label(win,text=x).place(x=0, y=325)
#     Label(win, text='Значение корня :', font=('Arial Black', 8), bg="aqua").place(x=0, y=300)
#     Label(win, text='Количество итераций :', font=('Arial Black', 8), bg="aqua").place(x=150, y=300)
#     Label(win, text='Значение функции :', font=('Arial Black', 8), bg="aqua").place(x=0, y=350)
#     Label(win, text=f(x)).place(x=0, y=370)
#     with open('text.txt', 'a') as file:
#         file.write('Ньютон:\n')
#         file.write(f'Кол-во итераций: {count}\n')
#         file.write(f'x: {x}\n')
#         file.write(f'f(x): {f(x)}\n\n')

# def Hord():
#     eps = float(e.get())
#     a = float(lev1.get())
#     b = float(prav1.get())
#     count=0
#     x=(a*f(b)-f(a)*b)/(f(b)-f(a))
#     while abs(f(x)) > eps:
#         x = (a * f(b) - f(a) * b) / (f(b) - f(a))
#         if f(x) * f(b) < 0:
#             a = x
#         else:
#             b = x
#         count += 1
#     Label(win, text=count).place(x=590, y=325)
#     Label(win, text=x).place(x=370, y=325)
#     Label(win, text=f(x)).place(x=370, y=370)
#     Label(win, text='Значение корня :', font=('Arial Black', 8), bg="cadetblue1").place(x=370, y=300)
#     Label(win, text='Количество итераций :', font=('Arial Black', 8), bg="cadetblue1").place(x=520, y=300)
#     Label(win, text='Значение функции :', font=('Arial Black', 8), bg="cadetblue1").place(x=370, y=350)
#     with open('text.txt', 'a') as file:
#         file.write('Хорды:\n')
#         file.write(f'Кол-во итераций: {count}\n')
#         file.write(f'x: {x}\n')
#         file.write(f'f(x): {f(x)}\n\n')

# def Iter():
#     eps = float(e.get())
#     z=float(prim.get())
#     count=0
#     x=fi(z)
#     while abs(f(x)) > eps:
#         x=fi(z)
#         z=x
#         count+=1
#     Label(win, text=count).place(x=590, y=510)
#     Label(win, text=x).place(x=370, y=510)
#     Label(win, text=f(x)).place(x=370, y=560)
#     Label(win, text='Значение корня :', font=('Arial Black', 8), bg="chartreuse1").place(x=370, y=490)
#     Label(win, text='Количество итераций :', font=('Arial Black', 8), bg="chartreuse1").place(x=520, y=490)
#     Label(win, text='Значение функции :', font=('Arial Black', 8), bg="chartreuse1").place(x=370, y=540)
#     with open('text.txt', 'a') as file:
#         file.write('Итерации:\n')
#         file.write(f'Кол-во итераций: {count}\n')
#         file.write(f'x: {x}\n')
#         file.write(f'f(x): {f(x)}\n\n')
