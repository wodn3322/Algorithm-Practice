import sys


def solution():
    triangleNum = int(sys.stdin.readline().strip())
    lineNumList = []

    for _ in range(triangleNum):
        lineNumList.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    for i in range(triangleNum):
        if i == 0:
            continue
        else:   
            for j in range(len(lineNumList[i])):
                if 0 < j < len(lineNumList[i]) - 1:
                    lineNumList[i][j] = max(lineNumList[i][j] + lineNumList[i - 1][j - 1], lineNumList[i][j] + lineNumList[i - 1][j])
                elif j == 0:
                    lineNumList[i][j] = lineNumList[i][j] + lineNumList[i - 1][j]
                elif j == len(lineNumList[i]) - 1:
                    lineNumList[i][j] = lineNumList[i][j] + lineNumList[i - 1][j - 1]
    sys.stdout.write(str(max(lineNumList[-1])) + '\n')

    return


if __name__ == '__main__':
    solution()
