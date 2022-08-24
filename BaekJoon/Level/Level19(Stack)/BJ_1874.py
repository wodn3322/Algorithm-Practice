import sys


def solution():
    numCount = int(sys.stdin.readline().strip())
    numList = [0] * numCount
    for i in range(numCount):
        numList[i] = int(sys.stdin.readline().strip())

    stackList = []
    waitList = []
    answerList = []
    for i in range(numCount):
        waitList.append(i + 1)
        answerList.append('+')
        while numList[len(stackList)] == waitList[-1]:
            lastNum = waitList.pop()
            stackList.append(lastNum)
            answerList.append('-')
            if len(waitList) == 0:
                break
        if i == numCount - 1 and len(stackList) != numCount:
            sys.stdout.write('NO\n')
            return

    for answer in answerList:
        sys.stdout.write(answer + '\n')

    return


if __name__ == '__main__':
    solution()
