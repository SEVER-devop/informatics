import random

def bubble_sort(arr) -> list:  # Сортировка пузыриком
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


orig_arr = [random.randint(-18,-10) for _ in range(10)]
#orig_arr = [1, 2, 3, -4, 2, 1, 5, 8, -3, -2, 2, 4, 3, 1]
duplic_arr = [i for i in orig_arr]
negative = [i for i in range(len(duplic_arr)) if duplic_arr[i] < 0]
n_max = max(duplic_arr)
i_max = duplic_arr.index(n_max)

print(f"Исходный массив {duplic_arr} \n Максимальный элемент {n_max} и его индекс {i_max + 1} \n Первый отрицательный элемент {duplic_arr[negative[0]]} и его индекс {negative[0] + 1}")

if i_max == negative[0] or abs(i_max - negative[0]) == 1:
    print("Error")
else:
    if i_max > negative[0]:
        print("Сортировка от отрицательного до максимального")
        ans = duplic_arr[:negative[0] + 1] + bubble_sort(duplic_arr[negative[0] + 1:i_max]) + duplic_arr[i_max:]
    elif negative[0] > i_max:
        print("Сортировка от максимального до отрицательного")
        ans = duplic_arr[:i_max + 1] + bubble_sort(duplic_arr[i_max + 1 :negative[0]]) + duplic_arr[negative[0]:]
    print(f"Полученный {ans}")
        