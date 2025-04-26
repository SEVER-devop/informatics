letters = ['a', 'b', 'c', 'd']
valid_matrices = []

# Генерируем все возможные строки без повторений
unique_rows = []
for i in letters:
    for j in letters:
        if j == i: continue
        for k in letters:
            if k == i or k == j: continue
            for m in letters:
                if m == i or m == j or m == k: continue
                unique_rows.append([i, j, k, m])

print(len(unique_rows))