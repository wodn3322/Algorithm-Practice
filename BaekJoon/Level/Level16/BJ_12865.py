import sys


def solution():
    thingNum, value = map(int, sys.stdin.readline().strip().split(' '))
    dataList = []

    for _ in range(thingNum):
        dataList.append(list(map(int, sys.stdin.readline().strip().split(' '))))
    dataList = sorted(dataList)

    dynamicList = [[0] * (value + 1) for _ in range(thingNum + 1)]
    for i in range(1, thingNum + 1):
        for j in range(1, value + 1):
            if j >= dataList[i - 1][0]:
                dynamicList[i][j] = max(dynamicList[i - 1][j - dataList[i - 1][0]] + dataList[i - 1][1], dynamicList[i - 1][j])
            else:
                dynamicList[i][j] = dynamicList[i - 1][j]

    sys.stdout.write(str(dynamicList[-1][-1]) + '\n')

    return


if __name__ == '__main__':
    solution()
