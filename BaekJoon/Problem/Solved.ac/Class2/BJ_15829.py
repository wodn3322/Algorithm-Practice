import sys


def solution():
    n = int(sys.stdin.readline().strip())
    inputString = list(sys.stdin.readline().strip())

    num = 0
    for i in range(len(inputString)):
        num += (ord(inputString[i]) - ord('a') + 1) * (31 ** i)
    num %= 1234567891
    print(num)

    return


if __name__ == '__main__':
    solution()
