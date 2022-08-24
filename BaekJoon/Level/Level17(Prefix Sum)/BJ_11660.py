import sys


def solution():
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    table = []
    caseList = []
    answerList = [0] * m

    for _ in range(n):
        table.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    for _ in range(m):
        caseList.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    cumlativeList = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                cumlativeList[i][j] = table[i][j]
            elif j == 0:
                cumlativeList[i][j] = table[i][j] + cumlativeList[i - 1][j]
            else:
                cumlativeList[i][j] = cumlativeList[i][j - 1] + table[i][j] + cumlativeList[i - 1][j] - cumlativeList[i - 1][j - 1]

    for i in range(m):
        sum = 0
        if caseList[i][0] != 1 and caseList[i][1] != 1:
            sum = cumlativeList[caseList[i][2] - 1][caseList[i][3] - 1] - cumlativeList[caseList[i][2] - 1][caseList[i][1] - 2] - \
                  cumlativeList[caseList[i][0] - 2][caseList[i][3] - 1] + cumlativeList[caseList[i][0] - 2][caseList[i][1] - 2]
        elif caseList[i][0] == 1 and caseList[i][1] != 1:
            sum = cumlativeList[caseList[i][2] - 1][caseList[i][3] - 1] - cumlativeList[caseList[i][2] - 1][caseList[i][1] - 2]
        elif caseList[i][0] != 1 and caseList[i][1] == 1:
            sum = cumlativeList[caseList[i][2] - 1][caseList[i][3] - 1] - cumlativeList[caseList[i][0] - 2][caseList[i][3] - 1]
        elif caseList[i][0] == 1 and caseList[i][1] == 1:
            sum = cumlativeList[caseList[i][2] - 1][caseList[i][3] - 1]
        answerList[i] = sum

        # 시간 초과
        # for y in range(caseList[i][1]-1,caseList[i][3]):
        #     if caseList[i][0]!=1:
        #         sum += (cumlativeList[y][caseList[i][2]-1]-cumlativeList[y][caseList[i][0]-2])
        #     else:
        #         sum += cumlativeList[y][caseList[i][2]-1]

    for answer in answerList:
        sys.stdout.write(str(answer) + '\n')

    return


if __name__ == '__main__':
    solution()
