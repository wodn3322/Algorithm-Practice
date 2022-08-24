import sys


def solution():
    caseNum = int(sys.stdin.readline().strip())
    caseDict = {}
    for i in range(caseNum):
        caseDict[i] = {}
        dressNum = int(sys.stdin.readline().strip())
        for j in range(dressNum):
            name, type = map(str, sys.stdin.readline().strip().split(' '))
            if type not in caseDict[i]:
                caseDict[i][type] = [name]
            else:
                caseDict[i][type].append(name)
    answerList = [0] * caseNum

    for i in range(caseNum):
        kindNum = 1
        for k in caseDict[i]:
            kindNum *= (len(caseDict[i][k]) + 1)
        answerList[i] = kindNum - 1

    for i in range(caseNum):
        sys.stdout.write(str(answerList[i]) + '\n')

    return


if __name__ == '__main__':
    solution()
