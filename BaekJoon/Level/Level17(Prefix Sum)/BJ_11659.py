import sys


def solution():
    numLength, caseLength = map(int, sys.stdin.readline().strip().split(' '))

    numList = list(map(int, sys.stdin.readline().strip().split(' ')))
    caseList = []

    for _ in range(caseLength):
        caseList.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    cumlativeSumList = [0] * (numLength + 1)

    for i in range(numLength):
        cumlativeSumList[i + 1] = cumlativeSumList[i] + numList[i]

    answerList = [0] * caseLength
    for i in range(caseLength):
        answerList[i] = cumlativeSumList[caseList[i][1]] - cumlativeSumList[caseList[i][0] - 1]

    for answer in answerList:
        sys.stdout.write(str(answer) + '\n')
    return


if __name__ == '__main__':
    solution()
