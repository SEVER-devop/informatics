def matrix_infill(width=6) -> list:
    mat = [[None for _ in range(width)] for _ in range(width)]

    for i in range(width):
        for j in range(width):
            mat[i][j] = round(1.7 * (i + 1) * (0.3 * (i + 1) + (j - 4.5) * (j - 5.5)), 1)

    return mat


def max_elem(mat, width=6) -> list:
    max_el = mat[0][0]
    indx = [0, 0]
    for i in range(width):
        for j in range(width):
            if mat[j][i] > max_el:
                max_el = mat[j][i]
                indx = [i, j]

    return indx


def vector_infill(mat, indx, width=6) -> list:
    vec_f = []
    values_str = []
    values_col = []
    for i in range(width):
        values_col.append(mat[i][indx[0]]) # добавление столбца
        values_str.append(mat[indx[1]][i]) # добавление сроки
    
    for z in [values_col, values_str]:
        for i in z:
            counter = 0
            for j in z:
                if i == j:
                    counter += 1
            if counter == 1:
                vec_f.append(i)
    
    return vec_f


def bubble_sort(vec) -> list:
    vec = [i for i in vec] # создание копии объекта vec
    for i in range(len(vec) -  1):
        for j in range(len(vec) - i - 1):
            if vec[j] > vec[j + 1]:
                vec[j], vec[j + 1] = vec[j + 1], vec[j]

    return vec


def selective_sort(vec) -> list:
    vec = [i for i in vec] # создание копии объекта vec
    for i in range(len(vec)):
        min_el = vec[i]
        for j in range(i + 1, len(vec)):
            if min_el > vec[j]:
                min_el = vec[j]
                indx = j
        vec[i], vec[indx] = vec[indx], vec[i]

    return vec


matrix = matrix_infill()
index = max_elem(matrix)
vector_f = vector_infill(matrix, index)
bubble_sorted_vector_f = bubble_sort(vector_f)
selective_sorted_vector_f = selective_sort(vector_f)

print("Матрица")
for i in matrix:
    print(i)
print(f"Максимальный элемент: {matrix[index[1]][index[0]]}", 
    f"Вектор F:\n{vector_f}",
    f"Сортировка пузырьком:\n{bubble_sorted_vector_f}",
    f"Сортировка выбором:\n{selective_sorted_vector_f}", sep="\n")