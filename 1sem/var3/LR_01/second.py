# Пример №2
import math as mt

x = float(input('Введите значения переменной x '))
y = float(input('Введите значения переменной y '))

if y != 2 and mt.sin(x) != 1:
    a = (2 * mt.cos(x - mt.pi/6)) / (1 - mt.sin(x))
    b = 1 - (x ** 2 * mt.sin(x - 3) ** 2) / 2 - y
    if a > b:
        print(f'Задание 3.2 максимальное число из a и b -> a = {'{:.2f}'.format(a)}')
    else:
        print(f'Задание 3.2 максимальное число из a и b -> b = {'{:.2f}'.format(b)}')
else:
    if y == 2 and mt.sin(x) != 1:
        print('Заданное значение y в задании 3.2 не удовлетворяет ОДЗ')
    elif y != 2 and mt.sin(x) == 1:
        print('Заданное значение x в задании 3.2 не удовлетворяет ОДЗ')
    else:
        print('Заданноые значения x и y в задании 3.2 не удовлетворяют ОДЗ')

