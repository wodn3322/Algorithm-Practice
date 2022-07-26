import sys


def solution():
    listenCount, seeCount = map(int, sys.stdin.readline().split())
    listenList = [''] * listenCount
    seeList = [''] * seeCount

    for i in range(listenCount):
        listenList[i] = sys.stdin.readline().strip()

    for i in range(seeCount):
        seeList[i] = sys.stdin.readline().strip()

    seeList = set(seeList)

    answerList = []

    for i in listenList:
        if i in seeList:
            answerList.append(i)
    answerList.sort()

    sys.stdout.write(str(len(answerList)) + '\n')
    for person in answerList:
        sys.stdout.write(person + '\n')

    return


if __name__ == '__main__':
    solution()
