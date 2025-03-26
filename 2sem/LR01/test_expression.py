import math as mt
import re

from sympy import symbols, Eq, solve, exp, sin, cos, tan, atan


def variable_expression(val) -> list:
    def __replacment_finder(val):
            reps = ""
            rev_reps = []
            for rep in replacement:
                for s in range(len(val)-1):
                    if val[s] == rep[0] and val[s + 1] == rep[1]:
                        
                        # Поиск функции c аргументом для замены
                        counter_brackets = 0
                        while len(val) >= s:
                            reps += val[s]

                            if val[s] == '(':
                                counter_brackets += 1
                            elif val[s] == ')':
                                counter_brackets -= 1

                            if val[s] == ')' and counter_brackets == 0:
                                reps += ';'                                      
                                break
                            s += 1
                        rev_reps.append(rep )
            
            return reps.split(";")[:-1], rev_reps


    def __expression_x(val) -> list:
            reps, rev_reps = __replacment_finder(val)
            for i in range(len(reps)):
                val = val.replace(reps[i], f"{rev_reps[i]}({i+10})")

            x = symbols('x')
            eq = Eq(eval(val), 0)
            solution = solve(eq, x)
            g_x = str(solution[0])
            for i in range(len(reps)):
                g_x = g_x.replace(f"{rev_reps[i]}({i+10})", reps[i])

            return g_x

    def __expression_func_x(val) -> list:
        try:
            x = symbols('x')
            eq = Eq(eval(val), 0)
            solution = solve(eq, x)
            g_x = str(solution[0])
        except NotImplementedError:
             return __expression_error()

        return g_x
    
    def __expression_error() -> str:
        return 'Нельзя выразить x в данном уравнении'

    
    res = []
    val_rep = val
    replacement = ["cos", "sin", "exp", "ln", "tan", "atan"]
    for i in replacement:
                pat = i+'\\([^)]*\\)'
                val_rep = re.sub(fr"{pat}", '', val_rep)


    if "x" in val_rep:
            res.append(__expression_x(val))
            print("1111", val, val_rep)
    elif 'x' not in val:
            res.append(__expression_error())
            print("ERRR")
    else:
            res.append(__expression_func_x(val))
            print("2222")

    return res

st = "exp(-2*x) + 1"
st = "atan(x) + 1/3 * x**3"
st = "atan(10) + 1/3 * x**3"

result = variable_expression(st)
print(result)



'''''''''
f = func

-x 
x 

+f - x
-f - x
x - f
x + f

f * x
f / x

x - f - x
x * f - x
x - f * x
x * f * x




    # Замена с знаками
    def __replacment_finder(val):
            reps = ""
            signs = []
            for rep in replacement:
                for s in range(len(val)-1):
                    if val[s] == rep[0] and val[s + 1] == rep[1]:

                        # Поиск знака перед функции
                        sign = []
                        if s == 0:
                              sign.append('+')
                        else:
                            counter = s
                            while True:
                                counter -= 1
                                if val[counter] in ['+', '-', '/', '*']:
                                    sign.append(val[counter])
                                    break

                        # Поиск функции для замены
                        counter_brackets = 0
                        while len(val) >= s:
                            reps += val[s]

                            if val[s] == '(':
                                counter_brackets += 1
                            elif val[s] == ')':
                                counter_brackets -= 1

                            if val[s] == ')' and counter_brackets == 0:
                                while s < len(val) - 1:
                                      s += 1
                                      if val[s] in ['+', '-', '/', '*']:
                                        sign.append(val[s])
                                        break
                                else:
                                     sign.append(None)

                                reps += ';'                                      
                                break
                            s += 1
                        signs.append(sign)
            
            return reps.split(";")[:-1], signs

'''''''''

