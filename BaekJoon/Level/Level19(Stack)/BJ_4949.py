import sys


def solution():
    stringList = []
    leftpsList = ['(', '[']
    rightpsList = [')', ']']
    while True:
        inputString = sys.stdin.readline().rstrip('\n')
        if inputString == '.':
            break
        else:
            stringList.append(list(inputString.rstrip('.')))

    answerList = []
    for string in stringList:
        midBreak = False
        psStack = []
        for s in string:
            if s in leftpsList:
                psStack.append(s)
            elif s in rightpsList:
                if len(psStack)!= 0:
                    lastPS = psStack[-1]
                    if lastPS == '(' and s == ')':
                        psStack.pop()
                    elif lastPS == '[' and s == ']':
                        psStack.pop()
                    else:
                        answerList.append('no')
                        midBreak = True
                        break
                else:
                    answerList.append('no')
                    midBreak = True
                    break
        if  midBreak ==False:
            if len(psStack) == 0 :
                answerList.append('yes')
            else:
                answerList.append('no')

    for answer in answerList:
        sys.stdout.write(answer + '\n')

    return


if __name__ == '__main__':
    solution()
