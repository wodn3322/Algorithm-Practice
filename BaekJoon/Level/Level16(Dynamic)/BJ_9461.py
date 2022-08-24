import sys


def solution():
    caseNum = int(sys.stdin.readline().strip())
    caseList = [0] * caseNum
    answerList = [0] * caseNum

    for i in range(caseNum):
        caseList[i] = int(sys.stdin.readline().strip())

    dataList = [0] * 100
    dataList[0] = 1
    dataList[1] = 1
    dataList[2] = 1
    dataList[3] = 2
    dataList[4] = 2

    for i in range(caseNum):
        if dataList[caseList[i] - 1] != 0:
            answerList[i] = dataList[caseList[i] - 1]
        else:
            for j in range(5, caseList[i]):
                dataList[j] = dataList[j - 2] + dataList[j - 3]
            answerList[i] = dataList[caseList[i] - 1]

    for answer in answerList:
        sys.stdout.write(str(answer) + '\n')

    return


if __name__ == '__main__':
    solution()
