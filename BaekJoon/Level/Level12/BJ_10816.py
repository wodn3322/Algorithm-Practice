import sys


def solution():
    aCardNum = int(sys.stdin.readline())
    # aCardList = list(sys.stdin.readline().strip().split(' '))
    aCardDict = {}
    for i in list(sys.stdin.readline().strip().split(' ')):
        if aCardDict.get(i):
            aCardDict[i] += 1
        else:
            aCardDict[i] = 1
    bCardNum = int(sys.stdin.readline())
    bCardList = list(sys.stdin.readline().strip().split(' '))
    answerList = [0] * bCardNum

    for i in range(bCardNum):
        if aCardDict.get(bCardList[i]):
            answerList[i] = aCardDict[bCardList[i]]
        else:
            answerList[i] = 0

    for i in answerList:
        sys.stdout.write(str(i) + ' ')

    return


if __name__ == '__main__':
    solution()

# 참고자료
# https://chancoding.tistory.com/45
