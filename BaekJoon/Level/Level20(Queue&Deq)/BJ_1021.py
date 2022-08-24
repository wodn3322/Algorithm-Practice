import sys

from collections import deque


def solution():
    length, targetNum = map(int, sys.stdin.readline().strip().split(' '))
    targetList = list(map(int, sys.stdin.readline().strip().split(' ')))
    dequeList = deque([i + 1 for i in range(length)])
    actionCount = 0
    for target in targetList:
        while True:
            if dequeList.index(target) == 0:
                dequeList.popleft()
                break
            else:
                if dequeList.index(target) < (len(dequeList) / 2):
                    dequeList.rotate(-1)
                else:
                    dequeList.rotate(1)
                actionCount += 1
    sys.stdout.write(str(actionCount) + '\n')

    return


if __name__ == '__main__':
    solution()
