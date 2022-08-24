import sys


def solution():
    caseNum = int(sys.stdin.readline().strip())
    caseList = [[]] * caseNum
    for i in range(caseNum):
        caseList[i] = list(map(int, sys.stdin.readline().strip().split(' ')))

    # print(caseList[0][0])
    answerList = [0] * caseNum
    for i in range(caseNum):
        totalPath = 1
        divideNum = 1
        for j in range(0, caseList[i][0]):
            totalPath *= (caseList[i][1] - j)
            divideNum *= (1 + j)
        answerList[i] = totalPath // divideNum

    for answer in answerList:
        sys.stdout.write(str(answer) + '\n')

    return


if __name__ == '__main__':
    solution()
