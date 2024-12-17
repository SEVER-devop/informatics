from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from math import *
from pprint import *


def error(err) -> None:
    print(f"Произошла ошибка: {err}")

def dot_product(vectors) -> float:
    dot_product = 0
    if (len(vectors[0]) != len(vectors[1])) or len(vectors) != 2 :
        
        return error("Значение векторов введены не корректно")
    
    for i in range(len(vectors[0])):
        dot_product += vectors[0][i] * vectors[1][i]
        
    return dot_product

def check_dot_product(dot_products) -> int:
    if dot_products[0] > dot_products[1]:
        return 1
    return 0


x = [1.5, 2.1, 3.0]
y = [2.1, 1.1, 3.2]
z = [3.7, 1.2, 6.4, -5.3]
p = [1.8, -1.8, 2.5, -2.2]

answer = check_dot_product([dot_product([x, y]), dot_product([z, p])])
dot_prod = [dot_product([x, y]), dot_product([z, p])]
pprint(dot_prod)
print(answer)
a = "{:.2f}".format(123.456)
b = isclose(15.060000000000002, 15.060)
print(b)