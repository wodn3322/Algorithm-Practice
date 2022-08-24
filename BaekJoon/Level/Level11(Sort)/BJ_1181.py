import sys


def solution():
    wordCount = int(sys.stdin.readline())
    wordList = [''] * wordCount
    for i in range(wordCount):
        wordList[i] = sys.stdin.readline().strip()

    wordList = sorted(list(set(wordList)))
    wordList.sort(key=lambda x: len(x))

    for word in wordList:
        print(word)

    return


if __name__ == '__main__':
    solution()
