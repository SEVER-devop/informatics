def infil_matrix() -> list:
    diction = ['a', 'b', 'c', 'd']
    mat = []
    string_of_matrix = []
    for i in diction:
        for j in diction:
            for k in diction:
                string_of_matrix = []
                for m in diction:
                    string_of_matrix.append([i, j, k, m])
                mat.append(list(string_of_matrix))

    return mat

def valid_checker(mat) -> list:

    res_mat = []
    for vectors in mat:
        counter = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0
        }
        for vector in vectors:
            print("!!!")
            for key in counter.keys():
                counter[key] += vector.count(key)
                print(vector)
                print(counter)
                

        condition = sum([1 for i in counter.values() if (int(i) == 4)])
        # print(vectors)
        # print(counter)
        # print(condition)
        if condition == 4:
            print(vector)
            print(condition)


    return mat


matrix = infil_matrix()
valid_checker(matrix)
# print(matrix[0] + matrix[1])
# print(matrix)

