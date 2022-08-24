import sys


def solution():
    listLength = int(sys.stdin.readline().strip())
    numList = list(map(int, sys.stdin.readline().strip().split(' ')))
    numListBack = numList[::-1]

    dynamicFrontList = [1] * listLength
    dynamicBackList = [1] * listLength

    for i in range(1, listLength):
        for j in range(i):
            if numList[i] > numList[j]:
                dynamicFrontList[i] = max(dynamicFrontList[i], dynamicFrontList[j] + 1)
            if numListBack[i] > numListBack[j]:
                dynamicBackList[i] = max(dynamicBackList[i], dynamicBackList[j] + 1)

    dynamicBackList = dynamicBackList[::-1]
    dynamicList = [0] * listLength
    for i in range(listLength):
        dynamicList[i] = dynamicFrontList[i] + dynamicBackList[i] - 1

    sys.stdout.write(str(max(dynamicList)) + '\n')

    return


if __name__ == '__main__':
    solution()
