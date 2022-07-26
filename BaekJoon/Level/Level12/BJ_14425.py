import sys


def solution():
    stringNum, wordNum = map(int, sys.stdin.readline().split(' '))
    stringList = [''] * stringNum
    wordList = [''] * wordNum

    for i in range(stringNum):
        stringList[i] = sys.stdin.readline().strip()
    for i in range(wordNum):
        wordList[i] = sys.stdin.readline().strip()

    answerCount = 0
    for word in wordList:
        if word in stringList:
            answerCount += 1

    print(answerCount)

    return


if __name__ == '__main__':
    solution()
