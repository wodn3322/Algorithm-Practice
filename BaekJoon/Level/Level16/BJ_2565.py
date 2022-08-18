import sys


def solution():
    lineNum = int(sys.stdin.readline().strip())
    lineList = []

    for _ in range(lineNum):
        lineList.append(list(map(int, sys.stdin.readline().strip().split(' '))))
    lineList = sorted(lineList)
    crossNumList = [1] * lineNum

    for i in range(1, lineNum):
        for j in range(i):
            if lineList[i][1] > lineList[j][1]:
                crossNumList[i] = max(crossNumList[i], crossNumList[j] + 1)

    sys.stdout.write(str(lineNum-max(crossNumList)) + '\n')

    return


if __name__ == '__main__':
    solution()
