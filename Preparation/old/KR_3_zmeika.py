from random import * 

def calc_width(c) -> int:
    for i in range(1, len(c) // 2 + 1):
        if len(c) == i**2:
            width = i
            break
    else:
        width = 0

    return (width)

def infil_mat(width, c) -> list:
    mat = [[0 for _ in range(width)] for _ in range(width)]
    k = -1
    col_quant = 1
    col_change = 0
    str_change = 0
    str_quant = 3
    str_pos = round(width / 2) - 1
    col_pos = round(width / 2) - 1
    direct = 0 # right = 0, left = 1, up = 2, down = 3;
    while k + 1 < len(c):
        k += 1
        if direct == 0:
            mat[str_pos][col_pos] = c[k]
            if col_change == col_quant:
                direct = 1
                str_pos += 1
                col_change = 1
                if k == 2:
                    col_quant += 1
                else:
                    col_quant += 1
                k += 1
            else:
                col_pos += 1
                col_change += 1

        if direct == 1:
            mat[str_pos][col_pos] = c[k]
            if col_change == col_quant:
                direct = 2
                col_change = 1
                col_pos -= 1
                col_quant += 2
                k += 1
            else:
                col_pos -= 1
                col_change += 1

        if direct == 2:
            mat[str_pos][col_pos] = c[k]
            if str_change == str_quant:
                str_quant += 2
                direct = 3
            else:
                str_pos -= 1
                str_change += 1


        if direct == 3:
            pass


    return mat


c = [randint(-8, 8) for _ in range(25)]
c = [i + 1 for i in range(36)]

#print(calc_width(c))

for i in infil_mat(calc_width(c), c):
    print(i)