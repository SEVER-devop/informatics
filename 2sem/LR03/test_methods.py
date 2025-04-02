# def solve_gauss(A, B):
#     n = len(B)
#     for i in range(n):
#         # Нормализация строки
#         pivot = A[i][i]
#         A[i] = [a/pivot for a in A[i][i:]] + A[i][:i]
#         B[i] /= pivot
        
#         # Обнуление элементов ниже
#         for k in range(i+1, n):
#             m = A[k][i]
#             A[k] = [a - m*b for a,b in zip(A[k][i:], A[i][i:])] + A[k][:i]
#             B[k] -= m * B[i]
    
#     # Обратная подстановка
#     X = [0]*n
#     for i in range(n-1, -1, -1):
#         X[i] = B[i] - sum(a*x for a,x in zip(A[i][i+1:], X[i+1:]))
#     return X

# def solve_gauss_jordan(A, B):
#     n = len(B)
#     for i in range(n):
#         # Нормализация строки
#         pivot = A[i][i]
#         A[i] = [a/pivot for a in A[i]]
#         B[i] /= pivot
        
#         # Обнуление всех элементов в столбце
#         for k in range(n):
#             if k != i:
#                 m = A[k][i]
#                 A[k] = [a - m*b for a,b in zip(A[k], A[i])]
#                 B[k] -= m * B[i]
#     return B

# # Исходные данные
# matrix_a = [
#     [3.6, 2.7, 1.5],
#     [1.8, -3.6, 4.5],
#     [-4.7, 1.9, 3.3]
# ]
# matrix_b = [3.8, 0.4, -1.6]

# # Решение
# X_gauss = solve_gauss([row.copy() for row in matrix_a], matrix_b.copy())
# X_gj = solve_gauss_jordan([row.copy() for row in matrix_a], matrix_b.copy())

# print("Гаусс:", [round(x, 6) for x in X_gauss])
# print("Гаусс-Жордан:", [round(x, 6) for x in X_gj])










def solve_gauss(matrix_a, matrix_b):
    n = len(matrix_b)
    for i in range(n):
        # Частичный выбор ведущего элемента
        max_row = i
        for k in range(i+1, n):
            if abs(matrix_a[k][i]) > abs(matrix_a[max_row][i]):
                max_row = k
        
        # Перестановка строк
        matrix_a[i], matrix_a[max_row] = matrix_a[max_row], matrix_a[i]
        matrix_b[i], matrix_b[max_row] = matrix_b[max_row], matrix_b[i]
        
        # Проверка на вырожденность
        if abs(matrix_a[i][i]) < 1e-10:
            raise ValueError("Матрица вырождена - система не имеет решения")
        
        # Нормализация текущей строки
        pivot = matrix_a[i][i]
        matrix_a[i] = [a/pivot for a in matrix_a[i]]
        matrix_b[i] /= pivot
        
        # Обнуление элементов ниже
        for k in range(i+1, n):
            m = matrix_a[k][i]
            matrix_a[k] = [a - m*b for a,b in zip(matrix_a[k], matrix_a[i])]
            matrix_b[k] -= m * matrix_b[i]
    
    # Обратная подстановка
    solution = [0]*n
    for i in range(n-1, -1, -1):
        solution[i] = matrix_b[i] - sum(a*x for a,x in zip(matrix_a[i][i+1:], solution[i+1:]))
    return solution

def solve_gauss_jordan(matrix_a, matrix_b):
    n = len(matrix_b)
    for i in range(n):
        # Частичный выбор ведущего элемента
        max_row = i
        for k in range(i+1, n):
            if abs(matrix_a[k][i]) > abs(matrix_a[max_row][i]):
                max_row = k
        
        # Перестановка строк
        matrix_a[i], matrix_a[max_row] = matrix_a[max_row], matrix_a[i]
        matrix_b[i], matrix_b[max_row] = matrix_b[max_row], matrix_b[i]
        
        # Проверка на вырожденность
        if abs(matrix_a[i][i]) < 1e-10:
            raise ValueError("Матрица вырождена - система не имеет решения")
        
        # Нормализация текущей строки
        pivot = matrix_a[i][i]
        matrix_a[i] = [a/pivot for a in matrix_a[i]]
        matrix_b[i] /= pivot
        
        # Обнуление всех элементов в столбце
        for k in range(n):
            if k != i:
                m = matrix_a[k][i]
                matrix_a[k] = [a - m*b for a,b in zip(matrix_a[k], matrix_a[i])]
                matrix_b[k] -= m * matrix_b[i]
    return matrix_b

# Исходные данные
# matrix_a = [
# [3.6, 2.7, 1.5],
# [1.8, -3.6, 4.5],
# [-4.7, 1.9, 3.3]
# ]
# matrix_b = [3.8, 0.4, -1.6]


#     # Создаем копии для каждого метода
# a_gauss = [row.copy() for row in matrix_a]
# b_gauss = matrix_b.copy()
# solution_gauss = solve_gauss(a_gauss, b_gauss)
    
# a_gj = [row.copy() for row in matrix_a]
# b_gj = matrix_b.copy()
# solution_gj = solve_gauss_jordan(a_gj, b_gj)

# print("Метод Гаусса:", [round(x, 6) for x in solution_gauss])
# print("Метод Гаусса-Жордана:", [round(x, 6) for x in solution_gj])
