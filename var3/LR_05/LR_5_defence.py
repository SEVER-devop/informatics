import random


def len_checker(matrix_width, vectors) -> bool:
    l1 = matrix_width[0] * 4 - 4
    l2 = matrix_width[1] * 4 - 4
    if l1 <= len(vectors[0]) and l2 <= len(vectors[1]):
        return 1
    
    return 0


def disp_list(arr, arg="") -> None:
    print(arg)
    if len(arr) == 1:
        print(arr)
    elif len(arr) > 1:
        for i in arr:
            print(i)


def vectors_infill(len_values) -> list:
    x = [random.randint(0, 10) for _ in range(len_values[0])]
    y = [random.randint(0, 10) for _ in range(len_values[1])]
    disp_list([x, y], "Введенные векторы x; y;")
    
    return [x, y]


def matrix_infill(matrix_width, vectors):
    mat_x = [[0 for _ in range(matrix_width[0])] for _ in range(matrix_width[0])]
    mat_y = [[0 for _ in range(matrix_width[1])] for _ in range(matrix_width[1])]
    if not(len_checker(matrix_width, vectors)):
        print("Длины вектора не хватит для заполения матрицы")
    disp_list(mat_x)
    disp_list(mat_y)


def start() -> list:
    vectors_len = [int(i) for i in input("Введите длину вектора x и y через пробел ").split()]
    if len(vectors_len) != 2:
        print("Введено некорректное значение\n Введите все значения заново")
        return start()
    
    try:
        arr_len = [int(i) for i in input("Введите ширину первой и второй результирующей квадратной матрицы через пробел ").split()]
    except:
        print("Введено некорректное значение\n Введите все значения заново")
        return start()
    
    return [vectors_len, arr_len]


#values = start()
values = [[2, 2], [4, 5]]
print(values)
vectors = vectors_infill(values[0])
matrix = matrix_infill(values[1], vectors)