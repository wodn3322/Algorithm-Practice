import sys
from collections import deque


def solution():
    caseNum = int(sys.stdin.readline().strip())
    for _ in range(caseNum):
        wordNum, importance = map(int, sys.stdin.readline().strip().split(' '))
        wordList = deque(list(map(int, sys.stdin.readline().strip().split(' '))))
        printCount = 1
        while True:
            maxImportance = max(wordList)
            if importance == 0 and wordList[0] == maxImportance:
                sys.stdout.write(str(printCount) + '\n')
                break

            if wordList[0] == maxImportance:
                wordList.popleft()
                if importance != 0:
                    importance -= 1
                else:
                    importance = len(wordList) - 1
                printCount += 1
            else:
                wordList.rotate(-1)
                if importance != 0:
                    importance -= 1
                else:
                    importance = len(wordList) - 1

    return


if __name__ == '__main__':
    solution()
