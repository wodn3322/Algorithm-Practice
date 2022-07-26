def solution():
    a = int(input())

    def factorial(n):
        if n == 1 or n == 0:
            return 1
        elif n > 1:
            return n * factorial(n - 1)

    answer = factorial(a)
    print(answer)

    return


if __name__ == '__main__':
    solution()
