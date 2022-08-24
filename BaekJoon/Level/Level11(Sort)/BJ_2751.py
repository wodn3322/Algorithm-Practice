import sys


def solution():
    count = int(input())
    numList = []
    for _ in range(count):
        numList.append(int(sys.stdin.readline()))

    numList = sorted(numList)

    for i in numList:
        sys.stdout.write(str(i) + '\n')
    return


if __name__ == '__main__':
    solution()
