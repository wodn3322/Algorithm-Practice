import sys


def solution():
    n, k = map(int, sys.stdin.readline().strip().split(' '))

    personList = [i + 1 for i in range(n)]

    answerList = []
    loopCount = 0
    while personList:
        loopCount+=k
        while loopCount> len(personList):
            loopCount-=len(personList)
        answerList.append(personList[loopCount-1])
        personList.remove(personList[loopCount-1])
        loopCount-=1
    sys.stdout.write('<')
    for i in range(n):
        sys.stdout.write(str(answerList[i]))
        if i != n-1:
            sys.stdout.write(', ')
    sys.stdout.write('>')

    return


if __name__ == '__main__':
    solution()
