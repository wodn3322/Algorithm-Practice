import sys


def solution():
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    matrixA = []

    def mul(i, j, m):
        sum = 0
        for n in range(m):
            sum += matrixA[i][n] * matrixB[n][j]
        return sum

    for i in range(n):
        matrixA.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    m, k = map(int, sys.stdin.readline().strip().split(' '))
    matrixB = []
    answerMatrix = [[0] * k for _ in range(n)]

    for i in range(m):
        matrixB.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    for i in range(n):
        for j in range(k):
            answerMatrix[i][j] = mul(i,j,m)

    for answer in answerMatrix:
        for num in answer:
            sys.stdout.write(str(num)+' ')
        sys.stdout.write('\n')

    return


if __name__ == '__main__':
    solution()
