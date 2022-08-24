import sys

from collections import deque


def solution():
    caseNum = int(sys.stdin.readline().strip())
    answerList = []
    for _ in range(caseNum):
        inpustAction = list(sys.stdin.readline().strip())
        numLength = int(sys.stdin.readline().strip())
        if numLength != 0:
            numList = deque(list(map(int, sys.stdin.readline().strip()[1:-1].split(','))))
        else:
            sys.stdin.readline()
            numList = deque([])
            # answerList.append('error')

        rCount = 0
        checkBreak = False
        for action in inpustAction:
            if action == 'R':
                rCount+=1
                # numList.reverse()
            elif action == 'D':
                if len(numList) != 0:
                    if rCount%2 ==0:
                        numList.popleft()
                    else:
                        numList.pop()
                else:
                    answerList.append('error')
                    checkBreak = True
                    break
        if checkBreak == False:
            if rCount%2==1:
                numList.reverse()
            answerList.append(list(numList))

    for answer in answerList:
        if answer == 'error':
            sys.stdout.write(answer + '\n')
        else:
            sys.stdout.write('[')
            for i in range(len(answer)):
                sys.stdout.write(str(answer[i]))
                if i != len(answer) - 1:
                    sys.stdout.write(',')
            sys.stdout.write(']\n')

    return


if __name__ == '__main__':
    solution()

