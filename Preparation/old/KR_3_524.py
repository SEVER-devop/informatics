import numpy as np
from random import * 

def calc_cond(a_b, mat) -> bool:
    flag = False
    for i in [0, len(mat) - 1]:
        sum = 0
        for j in range(len(mat)):
            sum += abs(mat[j][i])
        if sum >= a_b[0] and sum <= a_b[1]:
            flag = True
            
    return flag


mat = [[randint(-10, 10) for _ in range(4)] for x in range(4)]
a_b = sorted([float(i) for i in input('Ведите a и b через пробел ').split()])

for i in mat:
    print(i)
print()

cond1 = calc_cond(a_b, mat)

if cond1:
    for i in range(len(mat) // 2):
        mat[i][len(mat) - 1 - i], mat[len(mat) - 1 - i][i] = mat[len(mat) - 1- i][i], mat[i][len(mat) - 1 - i]

else:
    for i in range(len(mat) - 1):
        mat[i][i] = abs(mat[i][i])

for i in mat:
    print(i)
print()

a = np.array(mat).transpose()
for i in a:
    print(i)