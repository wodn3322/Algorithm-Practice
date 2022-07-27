import sys


def solution():
    n, k = map(int, sys.stdin.readline().strip().split())

    target = 1
    divideNum = 1

    for i in range(k):
        target *= (n - i)
        divideNum *= (i + 1)
    sys.stdout.write(str(target // divideNum % 10007) + '\n')

    return


def solution2():
    n, k = map(int, sys.stdin.readline().strip().split())

    pascalTri = [[1]]
    if n >= 1:
        for i in range(1, n + 1):
            pascalTri.append([0] * (i + 1))
        pascalTri[1] = [1, 1]
        for i in range(1, n + 1):
            pascalTri[i][0] = 1
            for j in range(1, i):
                pascalTri[i][j] = pascalTri[i - 1][j - 1] + pascalTri[i - 1][j]
            pascalTri[i][-1] = 1

    # print(pascalTri)
    sys.stdout.write(str(pascalTri[n][k] % 10007) + '\n')

    return


if __name__ == '__main__':
    # solution()
    solution2()
