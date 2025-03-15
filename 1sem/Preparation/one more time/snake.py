def snake(n) -> list:
    mat = [[None for _ in range(n)] for _ in range(n)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cur_dir = 0
    x, y = n // 2, n//2
    if n % 2 == 0:
        x, y = x - 1, y - 1

    steps = 1
    cur_step = 0

    for i in range(n * n):
        mat[x][y] = i + 1

        x += directions[cur_dir][0]
        y += directions[cur_dir][1]
        cur_step += 1

        if cur_step == steps:
            cur_dir = (cur_dir + 1) % 4
            cur_step = 0

            if cur_dir % 2 == 0:
                steps += 1


    return mat



matrix = snake(4)

for i in matrix:
    print(i)