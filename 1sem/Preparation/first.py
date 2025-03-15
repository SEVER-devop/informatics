import random


def infill_matrix(n) -> list:
    mat = [[random.randint(-9, 9) for _ in range(n)] for _ in range(n)]

    return mat


def search_max_el(mat) -> list:
    max_el = [mat[0][0], [0, 0]]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] > max_el[0]:
                max_el = [mat[i][j], [i, j]]

    return max_el


def get_elements_below_diag(mat, indx_point, width) -> list:
    vec = []
    end_point_diag = [i for i in indx_point]

    # Нахождение верхней т. диагонали ч/з т. max
    while end_point_diag[0] != 0 and end_point_diag[1] != n - 1:
        end_point_diag = [end_point_diag[0] - 1, end_point_diag[1] + 1] 
    
    if end_point_diag != [0, 0]:
        for i in range(width):
            for j in range(width):
                if i <= end_point_diag[0]:
                    if i >= end_point_diag[0]:
                        end_point_diag[0] -= 1
                    continue
                elif j <= end_point_diag[1]:
                    if j >= end_point_diag[1]:
                        end_point_diag[1] -= 1
                    continue

                vec.append(mat[i][j])

    else:
        for i in range(width):
            for j in range(width):
                if i == 0 and j == 0:
                    continue
                vec.append(mat[i][j])

    return vec


n = 4
matrix = [
        [3, 6, 1, 4], 
        [1, 6, 4, 4], 
        [1, 9, 1, 4],
        [8, 0, 4, 1]]
matrix = infill_matrix(n)
max_element = search_max_el(matrix)
vector_below_diag = get_elements_below_diag(matrix, max_element[1], n)


print("\nМатрица")
for i in matrix:
    print(i)
print(f"\nМаксимальный элемент: {max_element[0]}"
    + f"\nЕго индекс {max_element[1][0] + 1} {max_element[1][1] + 1}")
print(f"вектор ниже диагонали: {vector_below_diag}\n")
