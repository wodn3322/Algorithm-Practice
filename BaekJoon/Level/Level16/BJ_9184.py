import sys


def solution():
    inputList = []
    while True:
        inputabc = list(map(int, sys.stdin.readline().strip().split(' ')))
        if inputabc[0] == -1 and inputabc[1] == -1 and inputabc[2] == -1:
            break
        else:
            inputList.append(inputabc)

    # dataList = [0] * 50
    # dataList = [dataList] * 50
    # dataList = [dataList] * 50

    dataList = [[[0 for _ in range(20)] for _ in range(20)] for _ in range(20)]

    def w(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        if a > 20 or b > 20 or c > 20:
            # dataList[a - 1][b - 1][c - 1] = w(20, 20, 20)
            # return dataList[a - 1][b - 1][c - 1]
            return w(20, 20, 20)
        if a < b < c:
            if dataList[a - 1][b - 1][c - 1] == 0:
                dataList[a - 1][b - 1][c - 1] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return dataList[a - 1][b - 1][c - 1]
        else:
            if dataList[a - 1][b - 1][c - 1] == 0:
                dataList[a - 1][b - 1][c - 1] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
            return dataList[a - 1][b - 1][c - 1]

    for i in inputList:
        answer = w(i[0], i[1], i[2])
        sys.stdout.write('w(' + str(i[0]) + ', ' + str(i[1]) + ', ' + str(i[2]) + ') = ' + str(answer) + '\n')
    return


if __name__ == '__main__':
    solution()
