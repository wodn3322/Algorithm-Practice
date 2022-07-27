import sys


def solution():
    ringNum = int(sys.stdin.readline().strip())
    ringList = list(map(int, sys.stdin.readline().strip().split(' ')))

    firstRingGc = set()

    for i in range(1, round(ringList[0] ** (1 / 2)) + 1):
        if ringList[0] // i >= 1 and ringList[0] % i == 0:
            firstRingGc.add(i)
            firstRingGc.add(ringList[0] // i)
    answerList = [''] * (ringNum - 1)
    for i in range(1, ringNum):
        maxGcp = 0
        for g in firstRingGc:
            if ringList[i] % g == 0 and maxGcp < g:
                maxGcp = g
        answerList[i - 1] = str(ringList[0] // maxGcp) + '/' + str(ringList[i] // maxGcp) + '\n'

    for i in answerList:
        sys.stdout.write(i)

    return


if __name__ == '__main__':
    solution()
