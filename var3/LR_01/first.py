# Пример №1
import math as mt

x = 3.251
y = 0.325
z = 0.466
a = 2**(y**x) + (3**x)**y
b = (abs(x - y) * (1 + (mt.sin(z)**2)) / mt.e**abs(x - y) + x/2 )
print(f'Задание 3.1 a = {'{:.2f}'.format(a)}, b = {'{:.2f}'.format(b)}')
