import sys


def solution():
    commandNum = int(sys.stdin.readline().strip())
    commandList = []
    stackList = []
    answerList = []

    for _ in range(commandNum):
        commandList.append(sys.stdin.readline().strip().split(' '))

    for command in commandList:
        if len(command) == 2:
            stackList.append(int(command[1]))
        else:
            if command[0] == 'pop':
                if len(stackList) == 0:
                    answerList.append(-1)
                else:
                    popNum = stackList.pop()
                    answerList.append(popNum)
            elif command[0] == 'size':
                answerList.append(len(stackList))
            elif command[0] == 'empty':
                if len(stackList) == 0:
                    answerList.append(1)
                else:
                    answerList.append(0)
            elif command[0] == 'top':
                if len(stackList) == 0:
                    answerList.append(-1)
                else:
                    answerList.append(stackList[-1])

    for answer in answerList:
        sys.stdout.write(str(answer) + '\n')

    return


if __name__ == '__main__':
    solution()
