import sys


def solution():
    listLength = int(sys.stdin.readline().strip())
    numList = list(map(int, sys.stdin.readline().strip().split(' ')))

    dynamicList = [1] * listLength

    for i in range(1, listLength):
        for j in range(i):
            if numList[i] > numList[j]:
                dynamicList[i] = max(dynamicList[i], dynamicList[j] + 1)

    print(dynamicList)
    sys.stdout.write(str(max(dynamicList))+'\n')

    return


if __name__ == '__main__':
    solution()
