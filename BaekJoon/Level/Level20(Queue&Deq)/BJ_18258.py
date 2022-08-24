import sys


def solution():
    commandCount = int(sys.stdin.readline().strip())
    commandList = []

    # for _ in range(commandCount):
    #     commandList.append(sys.stdin.readline().strip().split(' '))

    answerList = []
    queueList = []
    popCount = 0
    for _ in range(commandCount):
        command = sys.stdin.readline().strip().split(' ')
        if len(command) == 2:
            queueList.append(command[1])
        elif command[0] == 'pop':
            if len(queueList)-popCount==0:
                sys.stdout.write(str(-1)+'\n')
            else:
                sys.stdout.write(str(queueList[popCount])+'\n')
                popCount+=1
        elif command[0] == 'size':
            sys.stdout.write(str(len(queueList)-popCount) + '\n')
        elif command[0] == 'empty':
            if len(queueList)-popCount==0:
                sys.stdout.write(str(1)+'\n')
            else:
                sys.stdout.write(str(0)+'\n')
        elif command[0] == 'front':
            if len(queueList)-popCount == 0:
                sys.stdout.write(str(-1)+'\n')
            else:
                sys.stdout.write(str(queueList[popCount])+'\n')
        elif command[0] == 'back':
            if len(queueList)-popCount == 0:
                sys.stdout.write(str(-1)+'\n')
            else:
                sys.stdout.write(str(queueList[-1])+'\n')

    # for i in answerList:
    #     sys.stdout.write(str(i) + '\n')

    # for command in commandList:
    #     if len(command) == 2:
    #         queueList.append(command[1])
    #     else:
    #         if command[0] == 'pop':
    #             if len(queueList) == 0:
    #                 answerList.append(-1)
    #             else:
    #                 answerList.append(queueList.pop())
    #         elif command[0] == 'size':
    #             answerList.append(len(queueList))
    #         elif command[0] == 'empty':
    #             if len(queueList) == 0:
    #                 answerList.append(1)
    #             else:
    #                 answerList.append(0)
    #         elif command[0] == 'front':
    #             if len(queueList) == 0:
    #                 answerList.append(-1)
    #             else:
    #                 answerList.append(queueList[0])
    #         elif command[0] == 'back':
    #             if len(queueList) == 0:
    #                 answerList.append(-1)
    #             else:
    #                 answerList.append(queueList[-1])
    #
    # for i in answerList:
    #     sys.stdout.write(str(i) + '\n')

    return


if __name__ == '__main__':
    solution()
