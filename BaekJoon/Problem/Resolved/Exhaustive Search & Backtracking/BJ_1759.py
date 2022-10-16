import sys


def solution():
    l, c = map(int, sys.stdin.readline().strip().split(' '))
    answerList = []
    charList = sys.stdin.readline().strip().split(' ')
    charList.sort()
    checkVow = ['a', 'e', 'i', 'o', 'u']

    word = []

    def BruteForce(v, j, n):
        if len(word) == l:
            if v >= 1 and j >= 2:
                answerList.append(''.join(word))
            return

        for i in range(n, c):
            if charList[i] not in word:
                word.append(charList[i])
                if charList[i] in checkVow:
                    BruteForce(v + 1, j, i)
                else:
                    BruteForce(v, j + 1, i)
                word.pop()

    BruteForce(0, 0, 0)
    for answer in answerList:
        sys.stdout.write(answer + '\n')

    # vowels = []
    # consonants = []
    # for i in charList:
    #     if i in checkVow:
    #         vowels.append(i)
    #     else:
    #         consonants.append(i)

    return


if __name__ == '__main__':
    solution()
