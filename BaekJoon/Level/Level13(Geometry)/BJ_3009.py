import sys


def solution():
    xList = []
    yList = []
    for _ in range(3):
        x, y = map(int, sys.stdin.readline().strip().split())
        xList.append(x)
        yList.append(y)
    answerX = 0
    answerY = 0
    for i in range(3):
        if xList.count(xList[i]) == 1:
            answerX = xList[i]
        if yList.count(yList[i]) == 1:
            answerY = yList[i]
    sys.stdout.write(str(answerX) + ' ' + str(answerY))

    return


if __name__ == '__main__':
    solution()
