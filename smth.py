import sys


def main():
    n, m = [int(i) for i in input().split()]
    arr = [[ "" for j in range(m)] for i in range(n)]
    for i in range(n):
        val = [int(s) for s in input().split()]
        for j in range(m):
            arr[i][j] = val[j]
    print(arr)
    pass


if __name__ == '__main__':
    main()