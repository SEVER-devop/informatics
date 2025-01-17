import random


def infill_matrix(n=6) -> list:
    mat = [[random.randint(0, 9) for _ in range(6)] for _ in range(6)]

    return mat


def get_max_el(mat) -> list:
    max_el = [mat[0][0], [0, 0]]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] > max_el[0]:
                max_el = [mat[i][j], [i, j]]
    
    return max_el


def get_diags(mat, max_el) -> list:
    cur_pos = [i for i in max_el[1]]
    # Cписок с эл-ми гл диагонали и побочной ч/з т. max
    values = [[mat[cur_pos[0]][cur_pos[1]]], [mat[cur_pos[0]][cur_pos[1]]]]

    # Нахождение эл-ов главной диагонали
    while cur_pos[0] != 0 and cur_pos[1] != len(mat) - 1:
        cur_pos = [cur_pos[0] - 1, cur_pos[1] + 1]
        values[0].append(mat[cur_pos[0]][cur_pos[1]])
    cur_pos = [i for i in max_el[1]]

    while cur_pos[0] != len(mat) - 1 and cur_pos[1] != 0:
        cur_pos = [cur_pos[0] + 1, cur_pos[1] - 1]
        values[0].append(mat[cur_pos[0]][cur_pos[1]])
    cur_pos = [i for i in max_el[1]]
    
    # Нахождение элементов побочной диагонали
    while cur_pos[0] != 0 and cur_pos[1] != 0:
        cur_pos = [cur_pos[0] - 1, cur_pos[1] - 1]
        values[1].append(mat[cur_pos[0]][cur_pos[1]])
    cur_pos = [i for i in max_el[1]]

    while cur_pos[0] != len(mat) - 1 and cur_pos[1] != len(mat) - 1:
        cur_pos = [cur_pos[0] + 1, cur_pos[1] + 1]
        values[1].append(mat[cur_pos[0]][cur_pos[1]])
    cur_pos = [i for i in max_el[1]]

    return values


def bubble_sort(vec) -> list:
    vec = [i for i in vec] # создание копии объекта vec
    for i in range(len(vec) - 1):
        for j in range(len(vec) - i - 1):
            if vec[j] > vec[j + 1]:
                vec[j], vec[j + 1] = vec[j + 1], vec[j]

    return vec


words = ["Главная", "Побочная"]
matrix = [
    [6, 8, 3, 1, 5, 6], 
    [5, 9, 0, 1, 6, 8], 
    [5, 6, 4, 9, 7, 6], 
    [0, 3, 6, 1, 2, 3], 
    [9, 3, 1, 7, 0, 1], 
    [1, 6, 7, 7, 7, 7]]
# matrix = infill_matrix()
max_element = get_max_el(matrix)

diags = get_diags(matrix, max_element)
vector_f = []
for i in diags:
    for j in i:
        vector_f.append(j)
sorted_vector_f = bubble_sort(vector_f)


print("Матрица")
for i in matrix:
    print(" ", i)
print(f"Максимальный эл-т и его коорд: {max_element[0]} [{max_element[1][0] + 1}; {max_element[1][1] + 1}]")
print("Диагонали и их суммы")
for i in range(len(diags)):
    summ = 0
    for j in diags[i]:
        summ += j
    print(f"    {words[i]} диагональ: {diags[i]}, ее сумма {summ}")
print(f"Вектор F: {vector_f}")
print(f"Отсортированный вектор F: {sorted_vector_f}")