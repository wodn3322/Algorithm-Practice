import sys


def solution():
    numCount = int(sys.stdin.readline().strip())
    numList = [0] * numCount

    for i in range(numCount):
        numList[i] = int(sys.stdin.readline().strip())

    numList.sort()

    gcpSet = set()
    for i in range(2, round((numList[1] - numList[0]) ** (1 / 2)) + 1):
        if (numList[1] - numList[0]) % i == 0 and (numList[1] - numList[0]) // i > 1:
            gcpSet.add(i)
            gcpSet.add((numList[1] - numList[0]) // i)
    gcpSet.add((numList[1] - numList[0]))

    maxGcp = 0

    for i in gcpSet:
        checkBreak = True
        for j in range(1, numCount - 1):
            if (numList[j + 1] - numList[j]) % i != 0:
                checkBreak = False
                break
        if checkBreak:
            if maxGcp < i:
                maxGcp = i

    answerList = []

    for i in range(2, round(maxGcp ** (1 / 2) + 1)):
        if maxGcp // i > 1 and maxGcp % i == 0:
            answerList.append(i)
            answerList.append(maxGcp // i)
    answerList.append(maxGcp)

    answerList = list(set(answerList))
    answerList.sort()

    for i in answerList:
        sys.stdout.write(str(i) + ' ')

    return


if __name__ == '__main__':
    solution()
