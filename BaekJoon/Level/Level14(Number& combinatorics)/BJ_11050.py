import sys


def solution():
    n, k = map(int, sys.stdin.readline().strip().split())

    target = 1
    divideNum = 1

    for i in range(k):
        target *= (n - i)
        divideNum *= (i + 1)
    sys.stdout.write(str(target // divideNum) + '\n')

    return


if __name__ == '__main__':
    solution()
