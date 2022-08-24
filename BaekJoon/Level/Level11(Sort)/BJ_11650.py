import sys


def solution():
    count = int(sys.stdin.readline())
    dotList = [[]] * count

    for i in range(count):
        dotList[i] = list(map(int, sys.stdin.readline().split(" ")))

    dotList.sort()

    for dot in dotList:
        sys.stdout.write(str(dot[0]) + ' ' + str(dot[1]) + '\n')

    return


if __name__ == '__main__':
    solution()
