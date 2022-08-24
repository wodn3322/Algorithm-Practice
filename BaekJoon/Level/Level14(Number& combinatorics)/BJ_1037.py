import sys


def solution():
    divideNum = int(sys.stdin.readline().strip())
    numList = list(map(int, sys.stdin.readline().strip().split(' ')))
    numList.sort()

    if divideNum % 2 == 1:
        sys.stdout.write(str(numList[divideNum // 2] ** 2))
    else:
        sys.stdout.write(str(numList[0] * numList[-1]))

    return


if __name__ == '__main__':
    solution()
