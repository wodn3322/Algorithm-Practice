import sys


def solution():
    num = int(sys.stdin.readline().strip())

    dynamicList = [0] * (num + 1)

    for i in range(2, num + 1):
        dynamicList[i] = dynamicList[i - 1] + 1

        if i % 2 == 0:
            dynamicList[i] = min(dynamicList[i], dynamicList[i // 2] + 1)
        if i % 3 == 0:
            dynamicList[i] = min(dynamicList[i], dynamicList[i // 3] + 1)
    sys.stdout.write(str(dynamicList[num]) + '\n')
    return


if __name__ == '__main__':
    solution()
