import sys


def solution():
    n, k = map(int, sys.stdin.readline().strip().split())
    top = 1
    bot = 1
    divideNum = 1000000007

    def factorial(n):
        num = 1
        for i in range(2, n + 1):
            num = num * i % divideNum
        return num

    def divide(n, k):
        if k == 0:
            return 1
        elif k == 1:
            return n

        num = divide(n, k // 2)

        if k % 2 == 1:
            return num ** 2 * n % divideNum
        else:
            return num ** 2 % divideNum

    top = factorial(n)
    bot = factorial(k) * factorial(n - k)

    answer = top * divide(bot, divideNum - 2) % divideNum

    sys.stdout.write(str(int(answer)))

    return


if __name__ == '__main__':
    solution()
