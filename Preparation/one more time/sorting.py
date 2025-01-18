import random


def bubble_sorting(vec) -> list:
    vec = [i for i in vec]

    for i in range(len(vec) - 1):
        for j in range(len(vec) - i - 1):
            if vec[j] > vec[j + 1]:
                vec[j], vec[j + 1] = vec[j + 1], vec[j]

    return vec


def selective_sorting(vec) -> list:
    vec = [i for i in vec]

    for i in range(len(vec) - 1):
        m = i
        for j in range(i + 1, len(vec)):
            if vec[m] > vec[j]:
                m = j
                
        vec[m], vec[i] = vec[i], vec[m]
        
    return vec


vector = [random.randint(-10, 10) for _ in range(6)]
vector = [6, -3, -4, 2, -3, 9, 6, -10, 7, -7]


bubble_sorted_vector = bubble_sorting(vector)
selective_sorted_vector = selective_sorting(vector)

print(f"Пузырек:\n  {bubble_sorted_vector}\nВыборка:\n  {selective_sorted_vector}")
