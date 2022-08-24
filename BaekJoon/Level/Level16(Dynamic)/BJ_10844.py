import sys


def solution():
    num = int(sys.stdin.readline().strip())

    dynamicList = [[0] * 10 for _ in range(num)]
    for i in range(1, 10):
        dynamicList[0][i] = 1

    for i in range(1, num):
        for j in range(10):
            if j == 0:
                dynamicList[i][j] = dynamicList[i - 1][1]
                continue
            if j == 9:
                dynamicList[i][j] = dynamicList[i - 1][8]
                continue
            dynamicList[i][j] = dynamicList[i - 1][j - 1] + dynamicList[i - 1][j + 1]

    sys.stdout.write(str(sum(dynamicList[num - 1]) % 1000000000) + '\n')
    return


if __name__ == '__main__':
    solution()
