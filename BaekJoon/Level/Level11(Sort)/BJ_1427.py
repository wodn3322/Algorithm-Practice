import sys


def solution():
    numSplitList = list(sys.stdin.readline())

    numSplitList.sort()
    numSplitList = numSplitList[::-1]
    for i in numSplitList:
        sys.stdout.write(str(i))

    return


if __name__ == '__main__':
    solution()
