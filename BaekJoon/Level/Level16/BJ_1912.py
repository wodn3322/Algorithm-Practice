import sys


def solution():
    numberNum = int(sys.stdin.readline().strip())
    numberList = list(map(int, sys.stdin.readline().strip().split(' ')))
    dynamicList = []

    for i in range(numberNum):
        if i == 0:
            dynamicList.append(numberList[i])
            continue
        dynamicList.append(max(dynamicList[i - 1] + numberList[i], numberList[i]))

    sys.stdout.write(str(max(dynamicList)) + '\n')

    return


if __name__ == '__main__':
    solution()
