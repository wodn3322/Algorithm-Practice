import sys


def solution():
    num = int(sys.stdin.readline().strip())
    total = 1

    for i in range(1, num + 1):
        total *= i

    stringList = list(str(total))
    stringList = stringList[::-1]
    notZeroCount = 0
    for i in stringList:
        if i == '0':
            notZeroCount += 1
        else:
            break
    sys.stdout.write(str(notZeroCount) + '\n')

    return


if __name__ == '__main__':
    solution()
