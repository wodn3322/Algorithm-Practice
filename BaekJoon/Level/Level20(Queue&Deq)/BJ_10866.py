import sys

from collections import deque

def solution():
    commandCount = int(sys.stdin.readline().strip())
    dequeList = deque([])

    for _ in range(commandCount):
        command = sys.stdin.readline().strip().split(' ')
        if command[0]=='push_front':
            dequeList.appendleft(command[1])
        elif command[0]=='push_back':
            dequeList.append(command[1])
        elif command[0] == 'pop_front':
            if len(dequeList)==0:
                sys.stdout.write(str(-1) + '\n')
            else:
                sys.stdout.write(str(dequeList.popleft())+'\n')
        elif command[0] == 'pop_back':
            if len(dequeList) == 0:
                sys.stdout.write(str(-1) + '\n')
            else:
                sys.stdout.write(str(dequeList.pop())+'\n')
        elif command[0] == 'size':
            sys.stdout.write(str(len(dequeList))+'\n')
        elif command[0] == 'empty':
            if len(dequeList)==0:
                sys.stdout.write(str(1) + '\n')
            else:
                sys.stdout.write(str(0) + '\n')
        elif command[0] == 'front':
            if len(dequeList)==0:
                sys.stdout.write(str(-1) + '\n')
            else:
                sys.stdout.write(str(dequeList[0]) + '\n')
        elif command[0] == 'back':
            if len(dequeList)==0:
                sys.stdout.write(str(-1) + '\n')
            else:
                sys.stdout.write(str(dequeList[-1]) + '\n')

    return


if __name__ == '__main__':
    solution()
