import sys


def solution():
    a, b, c = map(int, sys.stdin.readline().strip().split(' '))

    def divide(a, b, c):
        if b == 1:
            return a % c

        num = divide(a, b // 2, c)

        if b % 2 == 0:
            return num ** 2 % c
        else:
            return num ** 2 * a % c

    remain = divide(a, b, c)

    sys.stdout.write(str(remain))

    return


if __name__ == '__main__':
    solution()
