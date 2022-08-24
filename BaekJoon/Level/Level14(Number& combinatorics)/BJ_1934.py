import sys


def solution():
    caseNum = int(sys.stdin.readline().strip())
    caseList = [[]] * caseNum
    for i in range(caseNum):
        caseList[i] = list(map(int, sys.stdin.readline().strip().split(' ')))

    def uclid(a, b):
        remain = max(a, b) % min(a, b)
        if remain == 0:
            return min(a, b)
        if min(a, b) % remain != 0:
            return uclid(remain, min(a, b))
        else:
            return remain

    answerList = [0] * caseNum
    for i in range(caseNum):
        greatestCommon = uclid(caseList[i][0], caseList[i][1])
        answerList[i] = int(caseList[i][0] * caseList[i][1] / int(greatestCommon))

    for i in answerList:
        sys.stdout.write(str(i) + '\n')

    return


if __name__ == '__main__':
    solution()
