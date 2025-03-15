def snake(width) -> list:
    mat = [[None for _ in range(width)] for _ in range(width)]

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = width // 2, width // 2
    if width % 2 == 0:
        x, y = x - 1, y - 1

    cur_dir = 0
    step = 1
    step_done = 0

    for i in range(width * width):
        mat[x][y] = i + 1

        x += direction[cur_dir][0]
        y += direction[cur_dir][1]
        step_done += 1

        if step == step_done:
            cur_dir = (cur_dir + 1) % 4
            step_done = 0

            if cur_dir % 2 == 0:
                step += 1

    return mat


snake_matrix = snake(width=4)

for i in snake_matrix:
    print(i)
