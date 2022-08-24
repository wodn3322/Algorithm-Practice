import sys


def solution():
    caseCount = int(sys.stdin.readline())
    dotList = [[]] * caseCount
    caseList = []
    answerList = [0] * caseCount
    for i in range(caseCount):
        dotList[i] = list(map(int, sys.stdin.readline().split(' ')))
        testNum = int(sys.stdin.readline().strip())
        tempList = []
        for _ in range(testNum):
            tempList.append(list(map(int, sys.stdin.readline().strip().split())))
        caseList.append(tempList)

    for i in range(caseCount):
        for c in caseList[i]:
            distanceForPrince = ((c[0] - dotList[i][0]) ** 2 + (c[1] - dotList[i][1]) ** 2) ** (1 / 2)
            distanceForRose = ((c[0] - dotList[i][2]) ** 2 + (c[1] - dotList[i][3]) ** 2) ** (1 / 2)
            if (distanceForPrince < c[2] and distanceForRose > c[2]) or (
                    distanceForPrince > c[2] and distanceForRose < c[2]):
                answerList[i] += 1

    for i in answerList:
        sys.stdout.write(str(i) + '\n')

    return


if __name__ == '__main__':
    solution()
