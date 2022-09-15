import sys


def solution():
    n, b = map(int, sys.stdin.readline().strip().split(' '))
    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    answerMatxrix = [[0] * n for _ in range(n)]

    def mul(b):
        if b==0:
            return
        mul(b//2)
        if b%2 ==0:



    return


if __name__ == '__main__':
    solution()
