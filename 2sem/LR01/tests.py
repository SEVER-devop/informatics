import math as mt

replacement = ["cos", "sin", "exp", "atan", "tan", "ln"]
fun = "cos(x + sin(y)) *  sin(x-y) * y - 3*x - 1/(x-12)"

# for rep in replacement:
#     for j in range(len(rep)):
#         for s in range(len(fun)):
#             pass

# reps = ""
# for rep in replacement:
#     for s in range(len(fun)-1):
#         if fun[s] == rep[0] and fun[s + 1] == rep[1]:
#             counter_brackets = 0
#             while True:
#                 reps += fun[s]

#                 if fun[s] == '(':
#                     counter_brackets += 1
#                 elif fun[s] == ')':
#                     counter_brackets -= 1

#                 if fun[s] == ')' and counter_brackets == 0:
#                     reps += ";"
#                     break
#                 s += 1
            
# print(reps.split(";")[:-1])


# x = 1
# y = 2
# fun = fun.replace("cos", "mt.cos").replace("sin", "mt.sin")
# print(eval(fun))


# from scipy.optimize import fsolve
# import numpy as np

# def equation(x):
#     return np.atan(x) + 1/3 * x**3
#     return np.exp(-2*x) - 2*x + 1
#     return np.tan(0.5 * x + 0.2) - x**2

# # Начальная точка
# initial_guess = 0.0

# # Решение уравнения
# solution = fsolve(equation, 10000)

# print(solution)

# import re

# eq_str = "tan(x) - atan(x)"
# new_eq_str = re.sub(r'\batan\b|\btan\b', lambda match: 'mt.' + match.group(), eq_str)

# print(new_eq_str)


import sympy as sp

def express_through_x(equation_string):
    # Определение переменной x
    x = sp.Symbol('x')
    
    # Парсинг уравнения из строки
    lhs, rhs = equation_string.split('=')
    equation = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
    
    # Решение уравнения относительно x
    solution = sp.solve(equation, x)
    
    # Возврат первого решения
    return solution[0]

# Пример использования
equation_string = "atan(10) + 1/3 * x**3"
g_x = express_through_x(equation_string)
print(g_x)